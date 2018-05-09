import calendar


class YearlessDate(object):
    "An object representing a date in a year (but not a year itself).  Suitable especially for birthdays, anniversaries etc."
    def __init__(self, day, month):
        self.day = int(day)
        self.month = int(month)
        self._validate()
        
    def _validate(self):
        "Checks that the values of day and month are valid"
        # Get valid max month days for the month (we use 2008 since it's a leap year)
        try:
            week, month_days = calendar.monthrange(2008, self.month)
        except calendar.IllegalMonthError:
            raise Exception('Cannot create DateInYear object with a month value of %d.' % self.month)

        if self.day < 1 or self.day > month_days:
             raise Exception('Cannot create DateInYear object - invalid day value %d for month %s.' % (self.day, self.month_name))

    @property
    def month_name(self):
        "Returns the full name of the month"
        return calendar.month_name[self.month]
    
    def __str__(self):
        return "%d %s" % (self.day, self.month_name)
    
    def __eq__(self, other):
        if not isinstance(other, YearlessDate):
            return False
        return (self.day == other.day) and (self.month == other.month)
    
    def __gt__(self, other):
        if self.month != other.month:
            return self.month > other.month
        return self.day > other.day
    
    def __ne__(self, other):
        return not self == other
    
    def __le__(self, other):
        return not self > other
        
    def __ge__(self, other):
        return (self > other) or self == other

    def __lt__(self, other):
        return not self >= other