# edge_dict = {}
# for line in open("twitter.txt"):
#     name_a, name_b = line.strip().split(';')
#     if name_a in edge_dict:
#         edge_dict[name_a].append(name_b)
#     else:
#         edge_dict[name_a] = [name_b]
#

edges = []
for line in open("twitter.txt"):
    name_a, name_b = line.strip().split(';')
    # repeatedly add edges to the network (1000 times)
    for i in range(100):
        edges.append((name_a, name_b))

print(edges)