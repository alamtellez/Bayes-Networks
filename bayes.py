d = {}
var_nodes = input().rstrip().split(',')
n_probs = int(input())
pobabilities = []
queries = []
for i in range(n_probs):
    parse_prob(input())
n_queries = int(input())
for i in range(n_queries):
    parse_query(input())
