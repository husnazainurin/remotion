from pathlib import Path
import sys

# Locate project root
ROOT_DIR = Path(__file__).resolve().parents[2]

# Add project root to Python path
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.model.landmarker import HandLandmarkerProcessor


def load_hand_landmarker():
    return HandLandmarkerProcessor()