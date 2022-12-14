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

def compute_registers(data):
    registers =[]
    register = 1
    for row in data:
        if row[0] == "noop":
            registers.append(register)
        else:
            registers.append(register)
            registers.append(register)
            register += int(row[1])
    return registers

def part_1(file = "input.txt", testing = False):
    data = read_data(file)
    
    registers = compute_registers(data)
    
    return sum(i*registers[i-1] for i in range(20,len(registers)+1,40))

assert part_1("test.txt") == 13140
print(part_1())

def part_2(file = "input.txt", testing = False):
    data = read_data(file)
    
    registers = compute_registers(data)
    
    registers = np.array(registers)
    cycles = np.array([i%40 for i in range(registers.size)])
    
    screen_image = np.where(abs(registers-cycles)<=1, "#"," ")
    screen_image = screen_image.reshape((len(registers)//40,40))
    for row in screen_image.tolist():
        print("".join(row))
        
    return 

part_2("test.txt")
part_2()
