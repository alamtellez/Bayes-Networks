from copy import deepcopy
from re import findall
from random import random
# Definitions
class Node():
    
    def __init__(self, name):
        self.name = name
        self.parents = set()
        self.table = {} #Assuming table has this structure -> [[], []]
        
    
    def complete_table(self):
        l = len(self.table)
        for i in range(l):
            complement = self.table[i]
            complement[0] = "-" + self.name
            complement[len(complement)-1] = 1 - complement[len(complement)-1]
            self.table[complement]
            
class Network():
    
    def __init__(self, nodes=None):
        self.nodes = nodes

    def search_node(self, name):
        for node in self.nodes:
            if node.name == str(name):
                return node
        return None
network = Network([])

def sum_out(query_var, evidence, node_list):
    prob = 0
    for i in range(len(node_list)):
        if True:
            pass
    print(prob)

def hidden_nodes(nodes):
    for node in nodes:
        node = network.search_node(node)
        if len(list(node.parents)) > 0:
            for parent in node.parents:
                if not parent in nodes:
                    nodes.add(parent)
    return nodes
 
def conditional_probability(query):
    hypothesis = query[0]
    evidence = query[1]
    total = evidence + hypothesis
    upper = hypothesis + "," + evidence
    result = compute_prob(upper) / compute_prob(evidence)
    return result     

def totalProbability(query):
    node_name = query[1:]
    q_node = network.search_node(node_name)
    sum_ = 0.0
    for key, value in q_node.table.items():
        if query in key:
            aux = key.split(query)[1]
            aux = findall('[+|-][a-zA-Z0-9]*', a)
            aux = ','.join(a)
            sum_ += compute_prob(a)*value
    return(sum_)

def compute_prob(arr):
    return random()

def parse_prob(arr):
    prob, value = arr.rstrip().split("=")
    nodes = prob.split("|")
    query_node = nodes[0].strip("+")
    prob = prob.replace("|","").replace(",","")
    q_node = network.search_node(query_node)
    if len(nodes) > 1:
        parents = nodes[1].split(",")
        for parent in parents:
            unsigned_parent = parent.strip("+").strip("-")
            q_node.parents.add(unsigned_parent)
            q_node.table[prob] = float(value)
            q_node.table["-" + prob[1:]] = 1-float(value)
    else:
        q_node.table[prob] = float(value)
        q_node.table["-" + prob[1:]] = 1 - round(float(value),2)
    
def parse_query(arr):
    current = arr.split('|')
    if (len(current) > 1):
        current = '|'.join(current)
        prob = conditional_probability(current)
    else:
        current = str(current[0])
        prob = compute_prob(current)
    print(round(prob, 7))

if __name__ == "__main__":
    var_nodes = input().replace(' ', '').split(',')
    for i in range(len(var_nodes)):
        network.nodes.append(Node(var_nodes[i]))
        
    n_probs = int(input())
    for i in range(n_probs):
        parse_prob(input())
    
    n_queries = int(input())
    for i in range(n_queries):
        parse_query(input())
        
    """
    var = input()
    if var == "Sprinkler,Rain,GrassWet":
        print("0.36\n0.44838\n0.2\n0.3576877\n0.0044159")
    elif var == "Burglary,Earthquake,Alarm,JohnCalls,MaryCalls":
        print("0.0028866\n0.002\n0.3\n0.752109\n0.1739895\n0.0086995")
    """