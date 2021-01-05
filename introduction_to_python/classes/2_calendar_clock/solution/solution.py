class Clock:
    def __init__(self, hrs, mins, secs):
        self.hrs = hrs
        self.mins = mins
        self.secs = secs
        if len(str(self.secs)) == 1:
            self.secs = str(self.secs)
            self.secs = "0" + self.secs 

    def __str__(self):
        return "{self.hrs}:{self.mins}:{self.secs}".format(self=self)
class Calendar:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{self.day}/{self.month}/{self.year}".format(self=self)

class CalendarClock(Clock, Calendar):
    def __init__(self, day, month, year, hrs, mins, secs ):
        Calendar.__init__(self, day, month, year)
        Clock.__init__(self, hrs, mins, secs)
        
    
    def __str__(self):
        return "{self.day}/{self.month}/{self.year}, {self.hrs}:{self.mins}:{self.secs}".format(self=self)

