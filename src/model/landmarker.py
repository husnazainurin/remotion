
import cv2
import mediapipe as mp
import time

from pathlib import Path
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class HandLandmarkerProcessor:

    HAND_CONNECTIONS = [
        # Thumb
        (0, 1), (1, 2), (2, 3), (3, 4),

        # Index finger
        (0, 5), (5, 6), (6, 7), (7, 8),

        # Middle finger
        (5, 9), (9, 10), (10, 11), (11, 12),

        # Ring finger
        (9, 13), (13, 14), (14, 15), (15, 16),

        # Little finger
        (13, 17), (17, 18), (18, 19), (19, 20),

        # Palm
        (0, 17)
    ]

    def __init__(self, model_path=None):

        # Resolve model path
        if model_path is None:
            model_path = (
                Path(__file__).resolve().parent
                / "mediapipe"
                / "hand_landmarker.task"
            )

        model_path = str(model_path)

        # MediaPipe configuration
        options = vision.HandLandmarkerOptions(
            base_options=python.BaseOptions(
                model_asset_path=model_path
            ),
            running_mode=vision.RunningMode.VIDEO,
            num_hands=1,
            min_hand_detection_confidence=0.5,
            min_hand_presence_confidence=0.5,
            min_tracking_confidence=0.5
        )

        # Initialize landmarker once
        self.landmarker = vision.HandLandmarker.create_from_options(
            options
        )

        self.previous_timestamp = 0

    def process_frame(self, frame):

        """
        Receive a BGR video frame.
        Detect hand landmarks and draw them on the frame.

        Returns:
            annotated_frame: BGR image with skeleton
            result: MediaPipe detection result
        """

        # Mirror the frame
        frame = cv2.flip(frame, 1)

        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        # Create MediaPipe image
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        # Generate monotonically increasing timestamp
        timestamp = int(time.monotonic() * 1000)

        timestamp = max(
            timestamp,
            self.previous_timestamp + 1
        )

        self.previous_timestamp = timestamp

        # Detect landmarks
        result = self.landmarker.detect_for_video(
            mp_image,
            timestamp
        )

        # Draw detected hand
        if result.hand_landmarks:

            landmarks = result.hand_landmarks[0]

            self.draw_hand_landmarks(
                frame,
                landmarks
            )

            display_text = "Hand Detected"

        else:
            display_text = "No Hand Detected"

        # Display detection status
        cv2.putText(
            frame,
            display_text,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2
        )

        return frame, result

    def draw_hand_landmarks(self, frame, landmarks):

        height, width, _ = frame.shape

        points = []

        # Convert normalized coordinates to pixels
        for landmark in landmarks:

            x = int(landmark.x * width)
            y = int(landmark.y * height)

            points.append((x, y))

        # Draw skeleton connections
        for start_idx, end_idx in self.HAND_CONNECTIONS:

            start_point = points[start_idx]
            end_point = points[end_idx]

            cv2.line(
                frame,
                start_point,
                end_point,
                (0, 255, 0),
                2
            )

        # Draw landmark points
        for point in points:

            cv2.circle(
                frame,
                point,
                5,
                (0, 0, 255),
                -1
            )

    def close(self):

        self.landmarker.close()
