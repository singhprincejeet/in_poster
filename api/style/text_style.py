from PIL import ImageFont

class TextStyle:

  def __init__(self, size, align, color):
    self.size = size
    self.align = align
    self.color = color


  def draw(self, canvas, value, position):
    font = self.get_font()
    coordinates = self.get_coordinates(canvas, value, font, position)
    canvas.text(
      coordinates,
      value,
      fill=self.color,
      font=font,
      align=self.align,
    )

  def get_coordinates(self, canvas, input, font, position):
    text_width, text_height = canvas.textsize(input, font=font)
    x = self.get_x_coordinate(text_width, position[0])
    y = self.get_y_coordinate(text_height, position[1])
    return (x, y)


  def get_x_coordinate(self, text_width, position):
    return {
        'left': 0,
        'center': (self.border_size() - text_width)/2,
        'right': self.border_size() - text_width
    }.get(position)


  def get_y_coordinate(self, text_height, position):
    return {
        'top': 0,
        'center': (self.border_size() - text_height)/2,
        'bottom': self.border_size() - text_height
    }.get(position)

  def get_font(self):
    return ImageFont.truetype('assets/fonts/TravelingTypewriter.ttf', size=self.size)


  def get_align(self):
    return self.align


  def get_color(self):
    return self.color
