

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window

class RotatingImage(Image):

    def __init__(self, image_list):
        self.image_list = image_list
        self.image_idx = 0
        self.max_image_idx = len(self.image_list)
        super(RotatingImage, self).__init__(source=self.image_list[self.image_idx])
        self._keyboard = Window.request_keyboard(None, self)
        if not self._keyboard:
            return
        self._keyboard.bind(on_key_down=self.on_keyboard_down)

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.image_idx= (self.image_idx-1) % self.max_image_idx
        elif keycode[1] == 'right':
            self.image_idx= (self.image_idx+1) % self.max_image_idx
        else:
            return False
        self.source = self.image_list[self.image_idx]
        return True


class MyApp(App):
  def build(self):
    return RotatingImage(['hab/hab1.png', 'hab/hab2.png', 'hab/hab3.png', 'hab/hab4.png'])

MyApp().run()
