from functools import wraps


def ensure_integer(position=None, variable_name=None):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if position is not None and len(args) > position:
                val = args[position]
            elif variable_name is not None and variable_name in kwargs:
                val = kwargs[variable_name]
            else:
                raise Exception("Please provide a temperature value to add")

            if not isinstance(val, int):
                raise TypeError("Temperature must be integer")
            if val < 0 or val > 110:
                raise ValueError("Temperature must range in between 0 and 110")

            return func(*args, **kwargs)
        return wrapper
    return decorator

class TempTracker:

    def __init__(self):
        self.holder = []
        self.counter = 0
        self.max = 0
        self.min = 0
        self.sum = 0

    @ensure_integer(1, 'temp')
    def insert(self, temp):
        """
        Records new temperature
        """
        self.holder.append(temp)
        self.sum += temp
        self.counter += 1
        self.max = temp if temp > self.max else self.max
        self.min = temp if temp < self.min or self.counter == 1 else self.min

    def get_max(self):
        """
        Returns highest temperature we have seen so far
        """
        return self.max

    def get_min(self):
        """
        Returns lowest temperature we have seen so far
        """
        return self.min

    def get_mean(self, decimal_points=2):
        """
        Returns mean of all temperatures we have seen so far
        """
        try:
            return round(self.sum / self.counter, decimal_points)
        except ZeroDivisionError:
            return 0

