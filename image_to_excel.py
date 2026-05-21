from get_pixels import GetPixel
import openpyxl as xl
from openpyxl.styles import PatternFill

class ImageToExcel():
    def __init__(self, image_path="example.jpg"):
        self.image_path = image_path

    def create_excel(self, output_name= "output.xlsx"):
        self.output_name = output_name
        self.wb = xl.Workbook()
        self.ws = self.wb.active

    def fill_excel(self):
        image = GetPixel(self.image_path)
        w, h = image.get_size()
        pixels = image.get_pixel()
        print("Coloring cells...")

        pixel_index = 0
        for row in range(1, h + 1):
            for col in range(1, w + 1):
                cell_color = pixels[pixel_index]
                cell = self.ws.cell(row=row, column=col)
                cell.fill = PatternFill(start_color= cell_color,
                                        end_color= cell_color,
                                         fill_type= "solid" 
                                         )
                pixel_index += 1
        image.close_image()
        print("Image convert successfully!")

    def save_file(self):
        self.wb.save(self.output_name)
        print(f"File saved as: {self.output_name}")
                


if __name__ == "__main__":
    new_image = ImageToExcel()
    new_image.create_excel()
    new_image.fill_excel()
    new_image.save_file()