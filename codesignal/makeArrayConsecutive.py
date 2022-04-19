"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size.
Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1.
He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.
"""

def solution(statues):

    sorted_statues = sorted(statues)
    pointer = 0
    
    while pointer != len(sorted_statues) - 1:
        if (sorted_statues[pointer + 1] - sorted_statues[pointer]) > 1:
            sorted_statues.insert(pointer + 1, sorted_statues[pointer] + 1)
        pointer += 1
            
    return len(sorted_statues) - len(statues)
