

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


