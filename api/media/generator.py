from PIL import Image, ImageDraw, ImageOps
from time import time

class Generator:
  DEFAULT_BACKGROUND_SIZE = 600

  def __init__(self, body_text, footer_text, image):
    self.body_text = body_text
    self.footer_text = footer_text
    self.background_image = self.create_background_image(image)


  def generate(self):
    self.draw()
    image_src = '/tmp/output_{0}.png'.format(int(time()*1000))
    self.background_image.save(image_src)
    return image_src


  def paste_image(self, background_image, border_image):
    offset = (self.background_size() - self.border_size()-1)//2
    background_image.paste(border_image, (offset, offset))


  def create_background_image(self, image):
    if image is None:
      return Image.new('RGB', (self.DEFAULT_BACKGROUND_SIZE, self.DEFAULT_BACKGROUND_SIZE), color = 'white')
    return image


  def draw(self):
    canvas = ImageDraw.Draw(self.background_image)
    self.add_text(canvas, self.body_text, ("center", "center"))
    self.add_text(canvas, self.footer_text, ("center", "bottom"))


  def add_text(self, canvas, text, position):
    font = text.get_font()
    coordinates = self.get_coordinates(canvas, text.get_value(), font, position)
    canvas.text(
      coordinates,
      text.get_value(),
      fill=text.get_color(),
      font=font,
      align=text.get_align()
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


  def background_size(self):
    return self.background_image.size[0]

  def border_size(self):
    return self.background_size() - 10
