import streamlit as st
from pathlib import Path
import sys

from streamlit_webrtc import (
    webrtc_streamer,
    VideoProcessorBase
)

# Locate project root
ROOT_DIR = Path(__file__).resolve().parents[2]

# Add project root to Python path
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


from src.model.landmarker import HandLandmarkerProcessor


st.title("ReMOTION - Hand Tracking")


class VideoProcessor(VideoProcessorBase):

    def __init__(self):

        # Initialize the reusable landmarker
        self.processor = HandLandmarkerProcessor()

    def recv(self, frame):

        # Receive live video frame from Streamlit
        img = frame.to_ndarray(format="bgr24")

        # Process frame using MediaPipe
        annotated_frame, result = self.processor.process_frame(
            img
        )

        # Return processed video frame
        return frame.from_ndarray(
            annotated_frame,
            format="bgr24"
        )


webrtc_streamer(
    key="hand_tracking",
    video_processor_factory=VideoProcessor,
    media_stream_constraints={
        "video": True,
        "audio": False
    },
    async_processing=True
)
