def validate_positive_number(value):
    """Validate that input is a positive number"""
    return value and value > 0

def validate_percentage(value):
    """Validate that input is a percentage (0-100)"""
    return value and 0 <= value <= 100

def validate_decimal_odds(value):
    """Validate that input is a valid decimal odds value"""
    return value and value > 0

def validate_timeframe(timeframe):
    """Validate that input is a valid timeframe"""
    valid_timeframes = ['1m', '5m', '15m', '30m', '1h', '4h', '1d', '1w']
    return timeframe in valid_timeframes

def validate_oi_data(long_oi, short_oi):
    """Validate Open Interest data"""
    return long_oi >= 0 and short_oi >= 0
