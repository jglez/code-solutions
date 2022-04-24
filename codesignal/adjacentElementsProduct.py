"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example:
    For inputArray = [3, 6, -2, -5, 7, 3], the output should be: solution(inputArray) = 21.
    7 and 3 produce the largest product.
"""

def solution(inputArray):
    
    max_product = inputArray[0] * inputArray[1]
    
    for index, item in enumerate(inputArray):
        if index == len(inputArray) - 1:
            break
        if inputArray[index] * inputArray[index + 1] > max_product:
            max_product = inputArray[index] * inputArray[index + 1]
        
    return max_product
