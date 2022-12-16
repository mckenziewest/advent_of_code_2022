# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 08:35:39 2022

@author: WESTMR
"""

import numpy as np


def read_data(file = "input.txt"):
    with open(file) as the_file:
        data = the_file.read().split('\n\n')
    return data

def process_data(data):
    # Create a list that will soon contain a dictionary for every monkey.
    monkey_list = []
    
    for monkey in data:
        this_monkey = {}
        rows = monkey.split('\n')
        
        # Deteremine the items the monkey starts with.
        # Held items are listed in the second row as comma-separated integers after the ":".
        holding = [np.int64(item) for item in rows[1].split(":")[1].split(",")]
        this_monkey["holding"] = holding
        
        # Determine the worry operation given for the monkey.
        # The worry operation is the 3-rd row of the monkey data.  
        # This row can be split to access the individual compontents of the operation.
        op_split = rows[2].split()
        # The operation itself is the second to last item in the split.
        op = op_split[-2]
        # It is possible for the operation to reference the existing worry value.
        # In that case, we change the operation to match, either squaring or doubling the value instead.
        if op_split[-1] == 'old':
            if op == "*":
                op = "**"
                val = 2
            elif op == "+":
                op = "*"
                val = 2
        # If that last entry in the operation is an integer, we record it as a numpy int.
        # We're going to be doing this operation many times so using numpy will greatly increase the speed.
        else:
            val = np.int64(op_split[-1])
        # We record the worry change as a pair: string operation with integer.
        this_monkey["operation"] = [op,val]
        
        # Next we generate the information about where the monkey sends the item.
        # This information is in the fourth row of the monkey string.
        # The quotient we check is the final integer when split on spaces.
        test_value = np.int64(rows[3].split()[-1])
        # The monkey the item is passed to is the last string in the split of the
        # fifth row given true, and
        # sixth row given false.
        send = [int(rows[k].split()[-1]) for k in [4,5]]
        this_monkey["test"] = test_value
        this_monkey["sends"] = {True:send[0],False:send[1]}
        
        this_monkey["items seen"] = 0
        
        monkey_list.append(this_monkey)
    return monkey_list

def complete_round(monkey_list,worry_drop=True):
    mult = lambda a,b: np.prod((a,b))
    add = lambda a,b: np.sum((a,b))
    exp = lambda a,b: np.power(a,b)
    operations_dict = {"*":mult,"+":add,"**":exp}
    
    monkey_mods = np.prod([m["test"] for m in monkey_list])
    for monkey in monkey_list:
        for item in monkey["holding"]:
            action = monkey["operation"]
            op = operations_dict[action[0]]
            item = op(item,action[1]) 
            if worry_drop:
                item //= 3
            else:
                item = np.mod(item,monkey_mods)
            
            is_divisible = np.all(np.mod(item, monkey["test"]) == 0)
            monkey_list[monkey["sends"][is_divisible]]["holding"].append(item)     
            
            monkey["items seen"]+=1
        monkey["holding"] = []
    return monkey_list

def get_monkey_business(data):

    item_counts = [d["items seen"] for d in data]
    item_counts.sort()
    
    return item_counts[-2]*item_counts[-1]
    
def part_n(file="input.txt",part=1,num_runs=20):
    data = read_data(file)
    
    data = process_data(data)
    for i in range(num_runs):
        data = complete_round(data,part==1)
        
    return get_monkey_business(data)

assert part_n("test.txt",part=1,num_runs=20) == 10605
#print(part_n("test.txt",part=1,num_runs=20))
print(part_n(part=1,num_runs=20))

assert part_n("test.txt",part=2,num_runs=10000) == 2713310158
#print(part_n("test.txt",part=2,num_runs=20))
print(part_n(part=2,num_runs=10000))
