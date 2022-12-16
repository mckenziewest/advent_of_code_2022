# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 10:56:07 2022

@author: WESTMR
"""
import networkx as nx


def read_data(file="test.txt"):
    with open(file) as the_file:
        data = the_file.read()
    
    row_lengths = data.find('\n')+1
    start_ind = data.find("S")
    start_loc = (start_ind//row_lengths, start_ind%row_lengths)
    
    end_ind = data.find("E")
    end_loc = (end_ind//row_lengths, end_ind%row_lengths)
    
    data=data.replace("S","a")
    data=data.replace("E","z")
    
    return data.split('\n'), start_loc, end_loc

def get_edges(data,node):
    val = ord(data[node[0]][node[1]])
    nearby_indices = [(node[0]+i,node[1]+j) for i,j in [(0,1),(1,0),(0,-1),(-1,0)]]
    max_a = len(data)
    max_b = len(data[0])
    nearby_indices = [(a,b) for a,b in nearby_indices if a>=0 and b>=0 and (a,b)!=node and a<max_a and b<max_b]
    
    can_go_to = [(a,b) for a,b in nearby_indices if ord(data[a][b])<= val+1]
    
    return([(node,new) for new in can_go_to])
    
    
def make_graph(data):
    G = nx.DiGraph()
    
    G.add_nodes_from([(r,c) for r in range(len(data)) for c in range(len(data[0]))])
    
    for vertex in G.nodes:
        G.add_edges_from(get_edges(data,vertex))
    
    return G
        
def part_1(file="input.txt"):
    data, start_loc, end_loc = read_data(file)

    G = make_graph(data)
    #return G
    return len(nx.shortest_path(G,source=start_loc,target=end_loc))-1

#G=part_1("test.txt")
print(part_1("test.txt"))
print(part_1())

def part_2(file="input.txt"):
    data, _, end_loc = read_data(file)
    
    poss_starts = [(i,j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j]=='a']
    
    G = make_graph(data)
    
    current_min = len(data)*len(data[0])
    for start_loc in poss_starts:
        try:
            this_path = len(nx.shortest_path(G,source=start_loc,target=end_loc))-1
            current_min = min(this_path,current_min)
        except:
            pass
    return current_min

#G=part_1("test.txt")
print(part_2("test.txt"))
print(part_2())