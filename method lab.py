class Time(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)
    def __add__(self, other):
        return str(self.hour+other.hour) + ":" + str(self.minute+other.minute) + ":" + str(self.second+other.second)
# the way that i bulit my add part was the word "other" was helping me add the other stuff from the other function
