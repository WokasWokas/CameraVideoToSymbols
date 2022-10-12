from voxel import image_to_pixel, Image
from PIL import Image as img
from camera import Camera
from show import ImageApp
from os import system

def cycle(camera: Camera, app: ImageApp) -> None:
    frame = camera.get_image()
    if frame is None: return ''
    frame = Image(frame.tolist())
    app.update_label(image_to_pixel(frame, 1))

def show_image(path: str, app: ImageApp) -> None:
    image = img.open(path)
    palette = [[image.getpixel((x, y)) for x in range(image.width)] for y in range(image.height)]
    image = Image(palette)
    image = image_to_pixel(image, 1)
    print(image)
    app.update_label(image)


if __name__ == "__main__":
    cam = Camera()

    app = ImageApp()

    #app.title("Camera 0")
    
    #app.bind("<Button-2>", lambda event: app.loop_func(cycle, cam, app))

    show_image("hyxWMpne_mc.jpg", app)

    app.start()
