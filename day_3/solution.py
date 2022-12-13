import numpy as np
import pandas as pd 

with open("input.txt") as input:
    data = input.read().split("\n")
    
def priority(letter):
    if letter < "a":
        return ord(letter)-ord("A")+27
    else:
        return ord(letter)-ord("a")+1

def part_1(data=data.copy()):
    
    priorities = []
    
    for sack in data:
        A = set(sack[:len(sack)//2])
        B = set(sack[len(sack)//2:])
        
        priorities.append(priority(A.intersection(B).pop()))
    
    return sum(priorities)
    
def part_2(data=data.copy()):
    
    priorities = []
    for i in range(len(data)//3):
        sacks = [set(data[3*i+j]) for j in [0,1,2]]
        badge = sacks[0].intersection(sacks[1].intersection(sacks[2])).pop()    
        priorities.append(priority(badge))
    return sum(priorities)
    
print(part_1())
print(part_2())
