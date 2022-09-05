from arcade import Window, View


class TestView(View):

    def __init__(self, window):
        super().__init__(window)

    def update(self):
        self.window.call_count += 1
        print(f"update : view : {self.window.call_count}")

    def on_update(self, delta_time):
        self.window.call_count += 1
        print(f"on_update : view : {self.window.call_count}")


class App(Window):

    def __init__(self):
        super().__init__()
        self.call_count = 0
        self.test_view = TestView(self)

        self.show_view(self.test_view)

    def update(self):
        self.call_count += 1
        print(f"update : window : {self.call_count}")

    def on_update(self, delta_time):
        self.call_count += 1
        print(f"on_update: window : {self.call_count}")


if __name__ == '__main__':
    app = App()
    app.run()