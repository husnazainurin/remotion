import cv2
import mediapipe as mp
import time

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# Import MediaPipe hand_landmarker.task
MODEL_PATH = "src/model/mediapipe/hand_landmarker.task"

# MediaPipe Configuration
BaseOptions = python.BaseOptions

HandLandmarker = vision.HandLandmarker
HandLandmarkerOptions = vision.HandLandmarkerOptions

RunningMode = vision.RunningMode


options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path=MODEL_PATH
    ),
    running_mode=RunningMode.VIDEO,
    num_hands=1,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)


# Used to draw lines between landmarks so it looks like a skeleton
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


def draw_hand_landmarks(frame, landmarks):

    '''Draw landmarks based on the configured skeleton and MediaPipe's hand-landmarker detection'''

    height, width, _ = frame.shape

    points = []

    # Convert normalized coordinates to pixel coordinates
    for landmark in landmarks:

        x = int(landmark.x * width)
        y = int(landmark.y * height)

        points.append((x, y))

    # Draw connections
    for start_idx, end_idx in HAND_CONNECTIONS:

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



def main():

    # Initialize MediaPipe Hand Landmarker
    with HandLandmarker.create_from_options(options) as landmarker:

        # Open webcam
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():

            print("Error: Could not open webcam.")
            return

        print("Hand Landmarker started.")
        print("Press Q to exit.")

        previous_timestamp = 0

        while True:

            success, frame = cap.read()

            if not success:

                print("Failed to read webcam frame.")
                break

            # Mirror webcam image
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

            # Get timestamp in milliseconds
            timestamp = int(time.time() * 1000)

            # Ensure timestamp is monotonically increasing
            timestamp = max(
                timestamp,
                previous_timestamp + 1
            )

            previous_timestamp = timestamp

            # Perform hand landmark detection
            result = landmarker.detect_for_video(
                mp_image,
                timestamp
            )

            # Process landmark result
            if result.hand_landmarks:

                # Get first detected hand
                landmarks = result.hand_landmarks[0]

                # Draw hand landmarks
                draw_hand_landmarks(
                    frame,
                    landmarks
                )

                print("\nHand detected:")

                # Print all 21 landmark coordinates
                for index, landmark in enumerate(landmarks):

                    print(
                        f"Landmark {index}: "
                        f"x={landmark.x:.4f}, "
                        f"y={landmark.y:.4f}, "
                        f"z={landmark.z:.4f}"
                    )

            else:

                print("No hand detected.")


            # Display information
            if result.hand_landmarks:

                display_text = "Hand Detected"
            else:
                display_text = "No Hand Detected"

            cv2.putText(
                frame,
                display_text,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2
            )

            # Show webcam
            cv2.imshow(
                "MediaPipe Hand Landmarker",
                frame
            )

            # Exit when Q is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()


# Run application
if __name__ == "__main__":
    main()
