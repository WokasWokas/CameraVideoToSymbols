import numpy as np
from cv2 import (
    VideoCapture,
    cvtColor,
    imshow,
    waitKey
)

class Camera:
    def __init__(self, camera_id: int = 0) -> None:
        self.camera = VideoCapture(0)
        if not self.camera.isOpened():
            exit("Cannot open camera.")

    def get_image(self) -> np.ndarray:
        result, image = self.camera.read()
        if not result:
            return None
        return image
    
    def show(self, frame, color_code) -> None:
        while True:
            ret, frame = self.camera.read()
            if not ret:
                exit("Can't receive frame (stream end?). Exiting ...")
            color = cvtColor(frame, color_code)
            imshow('frame', color)
            if waitKey(1) == ord('q'):
                break