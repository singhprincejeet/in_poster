from PIL import Image, ImageDraw, ImageOps
from time import time

class Generator:
  def __init__(self, body_text, footer_text):
    self.body_text = body_text
    self.footer_text = footer_text

  def generate(self):
    background_image = Image.new('RGB', (self.background_size(), self.background_size()), color = 'white')
    border_image = self.generate_border_image()
    self.paste_image(background_image, border_image)
    image_src = '/tmp/output_{0}.png'.format(int(time()*1000))
    background_image.save(image_src)
    return image_src


  def paste_image(self, background_image, border_image):
    offset = (self.background_size() - self.border_size()-1)//2
    background_image.paste(border_image, (offset, offset))


  def generate_border_image(self):
    image = Image.new('RGB', (self.border_size(), self.border_size()), color = 'white')
    canvas = ImageDraw.Draw(image)
    self.add_text(canvas, self.body_text, ("center", "center"))
    self.add_text(canvas, self.footer_text, ("center", "bottom"))
    return image


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
    return 600

  def border_size(self):
    return 550
