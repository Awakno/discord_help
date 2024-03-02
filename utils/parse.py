import re

def parse_timespan(timespan: str) -> int:
    """
    Function to parse timespan string to seconds
    
    ### Usage:
    args: timespan -> string
    return int 
    
    ### Example:
    parse_timespan("1h") -> 3600
    parse_timespan("1h30m") -> 5400
    
    ### Note:
    only english support
    s = second\n
    m = minute\n
    h = hour\n
    d = day\n
    y = year\n
    mo = month\n
    
    
    
    """
    
    date = {
        "s": 1,
        "m": 60,
        "h": 3600,
        "d": 86400,
        "y": 31536000,
        "mo": 2592000
    }
    total_seconds = 0
    # check if format is correct
    matches = re.finditer(r'(\d+)([a-zA-Z]+)', timespan)
    # calculate total seconds
    for match in matches:
        # get value and unit
        value, unit = match.groups()
        unit = unit.lower()
        # convert to seconds
        total_seconds += date.get(unit, 1) * int(value)
    # return total seconds
    return total_seconds


    