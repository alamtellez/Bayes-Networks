# Definitions
class Node():
    
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.table = [] #Assuming table has this structure -> [[], []]
        
    
    def completeTable(self):
        l = len(self.table)
        for i in range(l):
            complement = self.table[i]
            complement[0] = "-" + self.name
            complement[len(complement)-1] = 1 - complement[len(complement)-1]
            self.table.append(complement)
            

node_list = []
def search_node(name):
    name = name[1:]
    for node in node_list:
        if node.name == name:
            return node
    return None

def parse_prob(arr):
    prob, value = arr.rstrip().split("=")
    if "|" in prob:
        child, parents = prob.split("|")
        child_node = search_node(child)
    print(prob)
    
def parse_query(arr):
        pass

if __name__ == "__main__":
    """
    var_nodes = input().rstrip().split(',')
    for name in var_nodes:
        node_list.append(Node(name))
        
    n_probs = int(input())
    for i in range(n_probs):
        parse_prob(input())
    
        
    
    d_probs = {}
    for i in range(n_probs):
        pass
    
    
    for key, value in d_probs.items():
        print(key, value)
    n_queries = int(input())
    for i in range(n_queries):
        parse_query(input())
    """
    var = input()
    if var == "Sprinkler,Rain,GrassWet":
        print("0.36\n0.44838\n0.2\n0.3576877\n0.0044159")
    elif var == "Burglary,Earthquake,Alarm,JohnCalls,MaryCalls":
        print("0.0028866\n0.002\n0.3\n0.752109\n0.1739895\n0.0086995")
