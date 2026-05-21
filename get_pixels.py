from PIL import Image

class GetPixel():
    def __init__(self, name="example.jpg"):
        self.name = name
    
    def get_size(self):
        self.image = Image.open(self.name)
        self.width, self.height = self.image.size
        print(f"Image size: ({self.width}, {self.height})")
        return self.width, self.height

    def get_pixel(self):
        self.pixels = []
        for y in range(self.height):
            for x in range(self.width):
                R, G, B = self.image.getpixel((x, y))
                color = f"{R:02x}{G:02x}{B:02x}".upper()
                self.pixels.append(color)
        print("Image successfully analyzed")
        print(f"Your image has {len(self.pixels)} pixels")
        return self.pixels
    
    def close_image(self):
        self.image.close()

if __name__ == "__main__":
    new_image = GetPixel()
    new_image.get_size()
    new_image.get_pixel()
    new_image.close_image()