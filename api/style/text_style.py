from PIL import ImageFont

class TextStyle:

    def __init__(self, size, align, color):
        self.size = size
        self.align = align
        self.color = color


    def get_font(self):
        return ImageFont.truetype('assets/fonts/TravelingTypewriter.ttf', size=self.size)


    def get_align(self):
        return self.align


    def get_color(self):
        return self.color
