import numpy as np

try:
    import pyglet
except ImportError as e:
    raise ImportError(
        f"{e}. HINT: you can install pyglet directly via 'pip install pyglet'. "
        "But if you really just want to install all Gymnasium dependencies and not have to think about it, "
        "'pip install -e .[all]' or 'pip install gymnasium[all]' will do it."
    ) from e


class Pacman_SimpleImageViewer(object):
    def __init__(self, display=None, scale=5):
        self.window = None
        self.isopen = False
        self.display = display
        self.scale = scale

    def imshow(self, arr):
        height, width, _channels = arr.shape
        if self.window is None:
            self.window = pyglet.window.Window(
                width=self.scale * width * 4,
                height=self.scale * height * 4,
                display=self.display,
                vsync=False,
                resizable=True,
            )
            self.width = width
            self.height = height
            self.isopen = True

            @self.window.event
            def on_resize(width, height):
                self.width = width
                self.height = height

            @self.window.event
            def on_close():
                self.isopen = False

        assert len(arr.shape) == 3, "You passed in an image with the wrong number shape"

        resized_image = np.zeros(
            (height * self.scale, width * self.scale, _channels)
        ).astype("uint8")
        for y in range(height):
            for x in range(width):
                for ys in range(self.scale):
                    for xs in range(self.scale):
                        resized_image[y * self.scale + ys][x * self.scale + xs] = arr[
                            y
                        ][x]
        arr = resized_image
        image = pyglet.image.ImageData(
            arr.shape[1], arr.shape[0], "RGB", arr.tobytes(), pitch=arr.shape[1] * -3
        )
        self.window.clear()
        self.window.switch_to()
        self.window.dispatch_events()
        image.blit(0, 0, width=self.window.width, height=self.window.height)
        self.window.flip()

    def close(self):
        if self.isopen:
            self.window.close()
            self.isopen = False

    def __del__(self):
        self.close()
