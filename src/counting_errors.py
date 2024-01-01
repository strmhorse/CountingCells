

# Define an Error for invalid arguments
class InvalidCountingArgument(Exception):
    """
    Raised when there's a problem with the exceptions
    """
    
    def __init__(self, argname, argvalue, message):
        self.argname = argname
        self.argvalue = argvalue
        super().__init__(self.message)


