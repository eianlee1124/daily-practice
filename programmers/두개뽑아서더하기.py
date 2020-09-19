#!/usr/bin/env python3



from itertools import combinations

def solution(numbers):    
    combinations_of_numbers = combinations(numbers, 2)
    return sorted(set(combinations_of_numbers))
    

