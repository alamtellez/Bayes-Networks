d = {}
var_nodes = input().rstrip().split(',')
n_probs = int(input())
pobabilities = []
queries = []
def parse_prob(arr):
    return arr.rstrip().split("=")
    
def parse_query(arr):
    pass
d_probs = {}
for i in range(n_probs):
    key, value = parse_prob(input())
    d_probs["key"] = float(value)
f
n_queries = int(input())
for i in range(n_queries):
    parse_query(input())

