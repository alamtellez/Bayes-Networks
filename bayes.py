# Definitions
class Node():
    
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.table = {} #Assuming table has this structure -> [[], []]
        
    
    def complete_table(self):
        l = len(self.table)
        for i in range(l):
            complement = self.table[i]
            complement[0] = "-" + self.name
            complement[len(complement)-1] = 1 - complement[len(complement)-1]
            self.table[complement]
            
    
def sum_out(query_var, evidence, node_list):
    prob = 0
    for i in range(len(node_list)):
        #Looking for variables that need to be summed out
        if True:
            pass
    print(prob)
            


network = []
def search_node(name):
    name = name[1:]
    for node in network:
        if node.name == name:
            return node
    return None

def parse_prob(arr):
    prob, value = arr.rstrip().split("=")
    print(prob)
    nodes = prob.split("|")
    query_node = nodes[0].strip("+")
    if len(nodes) > 1:
        parents = nodes[1].split(",")
        for parent in parents:
            unsigned_parent = parent.strip("+").strip("-")
            for q_node in network:
                if q_node.name == query_node:
                    exists = False
                    if len(q_node.parents)>0:
                        for parent in q_node.parents:
                            if parent.name == unsigned_parent:
                                exists = True
                        if not exists:
                            for parent in network:
                                if parent.name == unsigned_parent:
                                    q_node.parents.append(parent)
                    else:
                        for parent_node in network:
                            if parent_node.name == unsigned_parent:
                                q_node.parents.append(parent_node)
        for node in network:
            if node.name == query_node:
                node.table[prob] = float(value)
                node.table["-" + prob[1:]] = 1-float(value)
    
def parse_query(arr):
        pass

if __name__ == "__main__":
    var_nodes = input().rstrip().split(',')
    for name in var_nodes:
        network.append(Node(name))
        
    n_probs = int(input())
    for i in range(n_probs):
        parse_prob(input())
    
    """
    for node in network:
        print("------------------------")
        print(node.name)
        for prob, value in node.table.items():
            print(prob, value)
    """
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