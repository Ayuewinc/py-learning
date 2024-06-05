from time import time, localtime, sleep
import os

class Clock:

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
        
    def run(self):
        if self._second < 59:
            self._second += 1
        else:
            self._second = 0
            if self._minute < 59:
                self._minute += 1
            else:
                self._minute = 0
                if self._hour < 23:
                    self._hour +=1
                else:
                    self._hour = 0
    def showtime(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

if __name__ == '__main__':
#    clock = Clock(23, 59, 50)
    clock = Clock.now()
    while True:
        os.system("clear")
        print(clock.showtime())
        sleep(1)
        clock.run()

