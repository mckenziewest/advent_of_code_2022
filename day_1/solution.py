import numpy as np
import pandas as pd 

with open("input.txt") as input:
    data = input.read().split("\n\n")

def part_1(data=data.copy()):
    sum_vals = [sum(int(n) for n in d.split('\n') if n!='') for d in data]
    
    return max(sum_vals)
    
def part_2(data=data.copy()):
    sum_vals = [sum(int(n) for n in d.split('\n') if n!='') for d in data]
    sum_vals.sort()
    return sum(sum_vals[-3:])
    
print(part_1())
print(part_2())
