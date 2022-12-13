import numpy as np
import pandas as pd 

def read_data():
    with open("input.txt") as input:
        data = input.read().split("\n\n")
    
    data = [d.split('\n') for d in data]
    
    
    stacks = pd.Series(data[0]).str.split('',expand=True).transpose().values.tolist()
    stacks = [[box for box in s[::-1] if box !=" "] for s in stacks if s[-1].isnumeric()]
    
    operations = pd.Series(data[1]).str.split(' ',expand=True)[[1,3,5]]
    
    return stacks, operations

def part_1():
    stacks, operations = read_data()
    
    for i,v in operations.iterrows():
        m,f,t  = v
        for i in range(int(m)):
            stacks[int(t)-1].append(stacks[int(f)-1].pop())
            
    return "".join([s[-1] for s in stacks])
    
def part_2():
    stacks, operations = read_data()
    
    for i,v in operations.iterrows():
        m,f,t  = v
        stacks[int(t)-1] += stacks[int(f)-1][-int(m):]
        stacks[int(f)-1] =  stacks[int(f)-1][:-int(m)]
        
    return "".join([s[-1] for s in stacks])
    
print(part_1())
print(part_2())
