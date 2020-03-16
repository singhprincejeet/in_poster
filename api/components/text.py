class Text:
    def __init__(self, value, text_style):
        self.value = value
        self.text_style = text_style

    def draw(self, canvas, position):
        self.text_style.draw(canvas, self.value, position)

    def get_font(self):
        return self.text_style.get_font()


    def get_value(self):
        return self.value


    def get_align(self):
        return self.text_style.get_align()


    def get_color(self):
        return self.text_style.get_color()
