from voxel import image_to_pixel, Image
from camera import Camera
from show import App

def cycle(camera: Camera, app: App) -> None:
    frame = camera.get_image()
    if frame is None: return ''
    frame = Image(frame.tolist())
    app.update_label(image_to_pixel(frame, 4))


if __name__ == "__main__":
    cam = Camera()

    app = App()
    app.title("Camera 0")

    app.bind("<Button-2>", lambda event: app.loop_func(cycle, cam, app))

    app.start()