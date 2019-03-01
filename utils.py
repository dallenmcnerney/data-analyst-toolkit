from datetime import datetime as dt

'''Stopwatch class
Creates a stopwatch object. Has split and total functionality.
Example usage: 
st = Stopwatch()
st.start
st.split()
st.last
st.start
st.total()
'''


class Stopwatch:
    def __init__(self):
        self.__start_time = dt.now()
        self.__last_time = self.__start_time
        self.start = self.__time_text(self.__start_time)
        self.last = self.__time_text(self.__last_time)

    @staticmethod
    def __time_text(time):
        return dt.strftime(time, '%m/%d/%Y %H:%M:%S')

    @staticmethod
    def __time_difference_text(td):
        days, hours, minutes, seconds = td.days, td.seconds // 3600, (td.seconds % 3600) // 60, (td.seconds % 60)
        day_text = hours_text = minutes_text = seconds_text = ''
        if days > 0:
            day_text = ('%s day(s) ' % days)
        if hours > 0:
            hours_text = ('%s hour(s) ' % hours)
        if minutes > 0:
            minutes_text = ('%s minute(s) ' % minutes)
        if seconds > 0:
            seconds_text = ('%s second(s) ' % seconds)
        return ''.join([day_text, hours_text, minutes_text, seconds_text]).strip()

    @staticmethod
    def __time_diff(prev_time):
        current_time = dt.now()
        time_diff = current_time - prev_time
        return current_time, time_diff

    def split(self):
        current_time, time_diff = self.__time_diff(self.__last_time)
        self.__last_time = current_time
        self.last = self.__time_text(self.__last_time)
        print(self.__time_difference_text(time_diff))

    def total(self):
        current_time, time_diff = self.__time_diff(self.__start_time)
        print(self.__time_difference_text(time_diff))
