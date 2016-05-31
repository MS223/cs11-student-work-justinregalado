class Time(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)
    def __add__(self, other):
        # return str(self.hour+other.hour) + ":" + str(self.minute+other.minute) + ":" + str(self.second+other.second)
        return Time(self.hour+other.hour,self.minute+other.minute,self.second+other.second)
# the way that i bulit my add part was the word "other" was helping me add the other stuff from the other function


time1 = Time(5,43,8)
time2 = Time(5,32,5)
time3 = Time(10000,1000,100000)
print time1
print time2
print time1+time2+time3
