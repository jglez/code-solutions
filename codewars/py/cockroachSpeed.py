"""
1km = 100,000cm
1hr = 3,600s

1. Multiply input, s, by 100,000 to convert km to cm
2. Divide cm by 3,600 to get cm/s
"""

def cockroach_speed(s):
    return s * 100000 // 3600
