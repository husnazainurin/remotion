import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av

st.markdown("Hand Strengtening ")

def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
  img = frame.to_ndarray(format="bgr24")
  # Add OpenCV or model processing here
  return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(
    key="live-cam",
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False},
)