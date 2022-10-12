from functools import cache

d = "Ñ@#W$9876543210!abc;:=-,._"

def count(arr: list) -> int:
    if arr.__len__() == 1: return 1
    first, i = arr[0], 1
    while not arr[i] != first:
        if arr.__len__() - 1 == i:
            return i + 1
        i += 1
    return i  

class Image:
    def __init__(self, pallete: list[list[tuple[int,int,int]]]):
        self.palette = pallete
        self._compressed = []
        self._compressed_size = (0, 0)

        self._set_size()
        #self._compress()
        #self._set_compressed_size()
    
    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    @property
    def size(self):
        return self._size

    @property
    def compressed(self):
        return self._compressed
    
    @property
    def compressed_height(self):
        return self._compressed_size[0]
    
    @property
    def compressed_width(self):
        return self._compressed_size[1]

    def _set_size(self) -> None:
        self._size = (len(self.palette[0]), len(self.palette))

    def _set_compressed_size(self) -> None:
        self._compressed_size = (len(self._compressed[0]), len(self.compressed) - 1)

    def _compress(self) -> None:
        for y in self.palette:
            compressed = []
            i, j = 0, 0
            while i != y.__len__():
                elem = y[i]
                j = count(y[i:])
                compressed.append((elem, j))
                i += j
            self.compressed.append(compressed)

    def getpixel(self, x: int, y: int) -> tuple[int, int, int]:
        if self.height <= y or self.width <= x:
            raise IndexError("Index out of bound!")
        return self.palette[y][x]
    
    def get_avarage_from_pixel(self, x: int, y: int) -> int:
        return sum(self.getpixel(x, y)) // 3

def pixel_to_letter(pixel: tuple[int,int,int]) -> str:
    avarage = sum(pixel) // 3
    #if avarage >= 255: 
    #    avarage = 260
    #elif avarage < 10:
    #    avarage = 10
    return d[-((avarage + avarage % 10) // 10)]

@cache
def image_to_pixel(image: Image, acc: int) -> str:
    result = ''
    for y in range(0, image.height, acc * 2):
        for x in range(0, image.width, acc):
            result += pixel_to_letter(image.getpixel(x, y))
        result += '\n'
    return result
