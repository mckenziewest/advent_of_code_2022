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
    monkey_list = []
    
    for monkey in data:
        rows = monkey.split('\n')
        holding = [np.int64(item) for item in rows[1].split(":")[1].split(",")]
        monkey_list.append([holding])
        
        op_split = rows[2].split()
        op = op_split[-2]
        if op_split[-1] == 'old':
            if op == "*":
                op = "**"
                val = 2
            elif op == "+":
                op = "*"
                val = 2
        else:
            val = np.int64(op_split[-1])
            
        monkey_list[-1].append([op,val])
        
        test_value = np.int64(rows[3].split()[-1])
        send = [int(rows[k].split()[-1]) for k in [4,5]]
        monkey_list[-1] += [test_value,send[0],send[1]]
        monkey_list[-1].append(0)
    return monkey_list

def complete_round(monkey_list,worry_drop=True,do_print = False):
    mult = lambda a,b: np.prod((a,b))
    add = lambda a,b: np.sum((a,b))
    exp = lambda a,b: np.power(a,b)
    operations_dict = {"*":mult,"+":add,"**":exp}
    
    monkey_mods = np.prod([m[2] for m in monkey_list])
    for monkey in monkey_list:
        for item in monkey[0]:
            action = monkey[1]
            op = operations_dict[action[0]]
            item = op(item,action[1]) 
            if worry_drop:
                item //= 3
            else:
                item = np.mod(item,monkey_mods)
            
            div_no = int(np.mod(item, monkey[2]) != 0)
            monkey_list[monkey[3+div_no]][0].append(item)     
            
            monkey[5]+=1
        monkey[0] = []
    return monkey_list

def part_1(file = "input.txt",num_runs = 20):
    data = read_data(file)
    
    data = process_data(data)
    for i in range(num_runs):
        data = complete_round(data)
    
    item_counts = [d[-1] for d in data]
    item_counts.sort()
    
    return item_counts[-2]*item_counts[-1]

assert part_1("test.txt") == 10605
print(part_1("test.txt"))
print(part_1())

def part_2(file = "input.txt",num_runs = 100):
    
    data = read_data(file)
    data = process_data(data)
    
    for i in range(num_runs):
        data = complete_round(data,False,i==999)

    item_counts = [d[-1] for d in data]
    item_counts.sort()
    
    return item_counts[-2]*item_counts[-1]

assert part_2("test.txt",10000) == 2713310158
print(part_2("test.txt",20))
print(part_2(num_runs = 10000))
