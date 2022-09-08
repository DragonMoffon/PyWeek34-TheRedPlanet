from arcade import Sprite, load_texture, Window
import arcade.gl as gl


class App(Window):

    def __init__(self):
        super().__init__(800, 600, "FelipeHC_Test")
        self._test_sprite = Sprite(texture=load_texture(":resources:/images/tiles/boxCrate.png"),
                                   center_x=self.width//2, center_y=self.height//2)

    def on_draw(self):
        self.clear()
        self._test_sprite.draw(pixelated=True)


if __name__ == '__main__':
    app = App()
    app.run()