from src import Clock


class Command:

    def __init__(self, name):
        self.start_time = -1
        self.start_frame = -1
        self.last_frame = 0
        self.value = 0

        self.name = ""

    def press(self, value):
        self.start_time = Clock.times
        self.start_frame = Clock.frame

    def release(self):
        self.start_time = -1


class _InputStream:

    def __init__(self):
        pass