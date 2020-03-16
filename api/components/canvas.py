from PIL import ImageDraw

class Canvas:
  def __init__(self, image):
    self.image = image
    self.canvas = ImageDraw.Draw(image)

  def text(self, position, args):
    canvas.text(
      coordinates,
      text.get_value(),
      **args
    )

  