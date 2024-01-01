

def isBlank(inStr):
    """
    Used to test if a string is actually empty
    """
    return not (inStr and inStr.strip())



def setupLogging(verbocity):
    """
    """
    base_loglevel = getattr(logging, (getenv('LOGLEVEL', 'WARNING')).upper())
    verbocity = min(verbocity, 2)
    loglevel = base_loglevel - (verbocity * 10)
    logging.basicConfig(level=loglevel,
                        format='%(message)s')
