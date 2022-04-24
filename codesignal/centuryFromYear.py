"""
Given a year, return the century it is in.
The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example:
    For year = 1905, the output should be
    solution(year) = 20;
    
    For year = 1700, the output should be
    solution(year) = 17.
"""

def solution(year):
    # Every 100 years is a century, so we divide the year by 100 
    
    # If the year divided by 100 does not divide evenly (if there is a decimal),
    # then we perform floor division, truncating the decimal, and add 1
    if year / 100 > year // 100:  
        return year // 100 + 1
    
    return year / 100  # Otherwise, divide by 100 and return
