class Robot:
    def up(self):
        return 0, -1
    def down(self):
        return 0, 1
    def right(self):
        return 1, 0
    def left(self):
        return -1, 0
    def sit(self):
        return 0, 0
    def clean(self):
        return "clean"
