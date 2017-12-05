from PIL import Image
import numpy as np


class ImageStitch:
    supported_modes = ["RGB", "L"]

    def __init__(self, dimension, rows=4, columns=4, mode="RGB"):
        if not isinstance(dimension, tuple):
            raise ValueError("dimension must be instance of tuple!")
        if mode not in ImageStitch.supported_modes:
            raise ValueError("Image modes supported is: %s, found: %s" % (ImageStitch.supported_modes, mode))

        self.counter = 0
        self.dimension = dimension
        self.rows = rows
        self.columns = columns
        self.buffer = Image.new(mode=mode, size=(dimension[0] * columns, dimension[1] * rows))

    @staticmethod
    def _np_to_pil(image):
        if len(image.shape) != 3:
            raise ValueError("Numpy arrays must have exactly three dimensions. Example: (84, 84, 1) or (84, 84, 3)")
        if image.shape[2] not in [1, 3]:
            raise ValueError("Numpy arrays must have 1 (grayscale) or 3 (rgb) as the third dimension")
        if image.dtype is not np.dtype('uint8'):
            raise ValueError("Numpy arrays must have dtype=np.uint8")
        if image.shape[2] == 1:
            # Reshape grayscale by removing the last dimension
            image = image.reshape(image.shape[:-1])

        image = Image.fromarray(image)
        return image

    @staticmethod
    def _np_check_normalization(numpy_arr):
        if numpy_arr.max() <= 1:
            # Indicates that its normalized between 0 and 1
            return numpy_arr * 255
        return numpy_arr

    def add(self, raw_image, row=None, column=None):
        if isinstance(raw_image, Image.Image):
            image = raw_image
        elif isinstance(raw_image, np.ndarray):
            raw_image = ImageStitch._np_check_normalization(raw_image)
            image = ImageStitch._np_to_pil(raw_image)

        else:
            raise ValueError("image input must be numpy.ndarray or PIL Image.")

        image = image.resize(self.dimension)

        if row is None or column is None:
            # Use the counter in this case
            column = int(self.counter / self.columns)
            row = self.counter % self.columns
            self.counter += 1

        x_start = self.dimension[0] * row
        y_start = self.dimension[1] * column

        self.buffer.paste(image, box=(x_start, y_start))

    def save(self, path):
        self.buffer.save(path)


if __name__ == "__main__":

    imarray = np.random.rand(100, 100, 3) * 255
    img = Image.fromarray(imarray.astype('uint8')).convert('RGB')
    img2 = np.zeros((84, 84, 3), dtype=np.uint8)
    img3 = np.random.rand(100, 100, 1) * 255
    img3 = img3.astype('uint8')

    stitch = ImageStitch((84, 84))
    stitch.add(img)
    stitch.add(img, row=1, column=1)
    stitch.add(img, row=2, column=2)
    stitch.add(img, row=3, column=3)
    stitch.save("./name.png")
