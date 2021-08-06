import threading
import time


class Thread (threading.Thread):
    def __init__(self, function, param):
        threading.Thread.__init__(self)
        self.function = function
        self.param = param

    def run(self):
        self.function(self.param)
