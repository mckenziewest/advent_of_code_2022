# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 08:35:39 2022

@author: WESTMR
"""

import numpy as np


def read_data(file = "input.txt"):
    with open(file) as the_file:
        data = the_file.read().split('\n')
    return [tuple(d.split()) for d in data]

def read_key(n):
    with open(f"test_key_part{n}.txt") as file:
        key = file.read()
    return int(key)

def add_tuples(tup_1,tup_2):
    return tuple(tup_1[i]+tup_2[i] for i in range(len(tup_1)))

def print_picture(H,T):
    for i in range(4,-1,-1):
        row = ""
        for j in range(6):
            if (i,j) == H:
                row += "H"
            elif (i,j) == T:
                row += "T"
            else:
                row += "."
        print(row)
            

def move_T(H,T):
    diagonal_moves = [(1,1),(1,-1),(-1,1),(-1,-1)]
    straight_moves = [(0,1),(0,-1),(-1,0),(1,0),(0,0)]
    touches_H = [add_tuples(H,v) for v in straight_moves]
    surrounds_H = [add_tuples(H,v) for v in diagonal_moves+straight_moves]
    if T in surrounds_H:
        return T
    else:
        for v in straight_moves + diagonal_moves:
            temp_T = add_tuples(T,v)
            if temp_T in touches_H:
                return temp_T
        for v in diagonal_moves:
            temp_T = add_tuples(T,v)
            if temp_T in surrounds_H:
                return temp_T

def part_1(file = "input.txt", testing = False):
    data = read_data(file)
    
    H_pos = (0,0)
    T_pos = (0,0)
    
    tail_visited = []
    
    movement = {"R":(0,1),"L":(0,-1),"U":(1,0),"D":(-1,0)}
    
    if testing:
        print_picture(H_pos,T_pos)
        print("\n\n")
    for direction, amount in data:
        for a in range(int(amount)):
            H_pos = add_tuples(H_pos,movement[direction])
            T_pos = move_T(H_pos,T_pos)
            tail_visited.append(T_pos)
            if testing:
                print_picture(H_pos,T_pos)
                print("\n\n")
    if testing:
        max_x = max([a for a,b in tail_visited])
        min_x = min([a for a,b in tail_visited])
        max_y = max([b for a,b in tail_visited])
        min_y = min([b for a,b in tail_visited])
        arr = np.zeros(shape=(max_x-min_x+1,max_y-min_y+1)).astype(str)
        for a,b in tail_visited:
            print(a,b)
            arr[max_x-a,b-min_y] = "#"
        arr = np.where(arr != "#", ".",arr)
        print(arr)
    return len(set(tail_visited)) 

part_1("test.txt")

assert read_key(1)==part_1("test.txt")
print(part_1())

def part_2(file = "input.txt", testing = False):
    data = read_data(file)
    
    H_pos = (0,0)
    knot_positions = [(0,0) for i in range(9)]
    
    tail_visited = []
    
    movement = {"R":(0,1),"L":(0,-1),"U":(1,0),"D":(-1,0)}
    
    for direction, amount in data:
        for a in range(int(amount)):
            H_pos = add_tuples(H_pos,movement[direction])
            knot_positions[0] = move_T(H_pos,knot_positions[0])
            for knot in range(1,9):
                knot_positions[knot] = move_T(knot_positions[knot-1],knot_positions[knot])
            tail_visited.append(knot_positions[-1])

    return len(set(tail_visited)) 

assert part_2("test.txt") == 1
assert part_2("test_2.txt") == 36
print(part_2())
