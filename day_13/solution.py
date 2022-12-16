# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:36:33 2022

@author: WESTMR
"""
import ast

def read_data(file):
    with open(file) as the_file:
        data=the_file.read().split('\n\n')
        
    return [[ast.literal_eval(l_or_r) for l_or_r in d.split('\n')] for d in data ]

def compare_value(left,right,verbose=False):
    if len(left)==0 or len(right)==0:
        return len(right)>=len(left)
    elif type(left[0])==int and type(right[0])==int:
        if left[0] > right[0]:
            return False
        elif left[0]<right[0]:
            return True
        else:
            return compare_value(left[1:],right[1:])
    elif type(left[0])==int and type(right[0])==list:
        left[0] = [left[0]]
        return compare_value(left,right)
    elif type(right[0])==int and type(left[0])==list:
        right[0] = [right[0]]
        return compare_value(left,right)
    elif type(left[0])==list and type(right[0])==list:
        if verbose:
            print('\t',left[0],right[0])
            print('\t',compare_value(left[0],right[0]))
        if compare_value(left[0],right[0]):
            return compare_value(left[1:],right[1:])
        else:
            return False
    
def part_1(file='input.txt',verbose=False):
    pairs = read_data(file)
    
    if verbose:
        the_sum = 0
        for i in range(len(pairs)):
            print("*******")
            print(pairs[i])
            val = (compare_value(*pairs[i],verbose))
            print(i+1,val)
            the_sum += i+1 
        return the_sum
    
    return sum([i+1 for i in range(len(pairs)) if compare_value(*pairs[i])])


print(part_1('test.txt',True))
#print(part_1())