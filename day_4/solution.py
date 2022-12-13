import numpy as np
import pandas as pd 

with open("input.txt") as input:
    data = input.read().split("\n")

data = pd.DataFrame(data)

data[["first","second"]] = data[0].str.split(",",expand=True)

data[[0,1]] = data["first"].str.split("-",expand=True)
data[[2,3]] = data["second"].str.split("-",expand=True)    

for i in range(4):
    data[i] = pd.to_numeric(data[i])
    
data["range_1"] = data.apply(lambda row: set(range(row[0],row[1]+1)),axis=1)
data["range_2"] = data.apply(lambda row: set(range(row[2],row[3]+1)),axis=1)

def part_1(data=data.copy()):
    
    data["1_contains_2"] = data.apply(lambda row: row["range_1"].issuperset(row["range_2"]),axis=1)
    data["2_contains_1"] = data.apply(lambda row: row["range_1"].issubset(row["range_2"]),axis=1)

    return sum(data["1_contains_2"] | data["2_contains_1"])
    
def part_2(data=data.copy()):
    
    data["if_overlap"] = data.apply(lambda row: len(row["range_1"].intersection(row["range_2"]))>0,axis=1)
    
    return sum(data["if_overlap"])
    
print(part_1())
print(part_2())
