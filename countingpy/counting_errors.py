

# Define an Error for invalid arguments
class InvalidCountingArgument(Exception):
    """
    Raised when there's a problem with the CLI arguments in the Counting module

    Attributes:
        argname -- Name of the argument that's incorrect
        argvalue -- Given or entered value of the argument that's incorrect
        message -- More details about what's wrong
    """
    
    def __init__(self, argname, argvalue, minvalue=0):
        self.argname = argname
        self.argvalue = argvalue
        self.message = f"Need a {argname} greater than {minvalue}, you gave {argvalue}."
        super().__init__(self.message)

class InvalidIndexException(Exception):
    """
    Raised when a given point is beyond the maximum area values.
    """
    def __init__(self, in_height, in_width, obj_height, obj_width):
        self.in_height = in_height
        self.in_width = in_width
        self.obj_height = obj_height
        self.obj_width = obj_width
        self.message = f"Your index ({in_height}, {in_width}) exceeded the maximum value of ({obj_height}, {obj_width})."
        super().__init__(self.message)


class InvalidValueException(Exception):
    """
    Raised when a given point is beyond the maximum area values.
    """
    def __init__(self, in_value):
        self.in_value = in_value
        self.message = f"Your value setting of {in_value} of type {type(in_value)} was invalid."
        super().__init__(self.message)


