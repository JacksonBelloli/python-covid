import threading
import time


class Thread (threading.Thread):
    def __init__(self, function):
        threading.Thread.__init__(self)
        self.function = function

    def run(self):
        self.function()
