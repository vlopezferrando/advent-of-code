#
# Check how I live coded this: https://youtu.be/-p4maXM-KWg
#

FLOW = {}
NEIGHBOURS = {}

# Read input
for line in open("16.in"):
    row = line.replace("=", " ").replace(";", "").replace(",", "").split()
    valve, flow, neighs = row[1], int(row[5]), row[10:]
    FLOW[valve] = flow
    NEIGHBOURS[valve] = neighs

D = {
    a: {b: 1 if b in NEIGHBOURS[a] else 0 if a == b else 1000 for b in FLOW}
    for a in FLOW
}

# Floyd algorithm
for k in FLOW:
    for i in FLOW:
        for j in FLOW:
            if i != j and i != k and j != k:
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]

# Generate a graph with valves of flow > 0 and AA
valves = {v for v, f in FLOW.items() if f > 0 or v == "AA"}
G = {a: [(b, D[a][b]) for b in valves if D[a][b] > 0] for a in valves}

# Print input for C++ program
print(len(G))
for i, v in enumerate(sorted(G.keys())):
    print(FLOW[v])
for i, (v, ns) in enumerate(sorted(G.items())):
    distances = {n: d for n, d in ns}
    for j, w in enumerate(sorted(G.keys())):
        try:
            print(distances[w], end=" ")
        except:
            print(0, end=" ")
    print()
