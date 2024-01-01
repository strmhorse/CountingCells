

# Define an Error for invalid arguments
class InvalidCountingArgument(Exception):
    """
    Raised when there's a problem with the CLI arguments in the Counting module

    Attributes:
        argname -- Name of the argument that's incorrect
        argvalue -- Given or entered value of the argument that's incorrect
        message -- More details about what's wrong
    """
    
    def __init__(self, argname, argvalue, message):
        self.argname = argname
        self.argvalue = argvalue
        self.message = message
        super().__init__(self.message)


