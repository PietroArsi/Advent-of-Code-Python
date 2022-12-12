import math

class Graph:
    def __init__(self, vertices):
        self.nodes = len(vertices)
        self.edges = {}
        for x in vertices:
            self.edges[x] = {}
            for y in vertices:
                self.edges[x][y] = -1

    def add_edge(self, u, v):
        self.edges[u][v] = 1
    
    def can_go(self, u, v):
        return self.edges[u][v] == 1

    def get_neighbours(self, u):
        neighbours = []
        if u[0]+1 < len(matrix) and self.can_go(u, (u[0]+1,u[1])):
            neighbours.append((u[0]+1,u[1]))
        if u[0]-1 >= 0 and self.can_go(u, (u[0]-1,u[1])):
            neighbours.append((u[0]-1,u[1]))
        if u[1]+1 < len(matrix[u[0]]) and self.can_go(u, (u[0],u[1]+1)):
            neighbours.append((u[0],u[1]+1))
        if u[1]-1 >= 0 and self.can_go(u, (u[0],u[1]-1)):
            neighbours.append((u[0],u[1]-1))
        return neighbours

start = (0,0)
finish = (0,0)
vertices = []

with open("2022/day12/input.txt") as f:
    lines = [list(x.strip()) for x in f.readlines()]
    matrix = [[]]
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            vertices.append((x, y))
            if lines[x][y] == "S":
                start = (x,y)
                matrix[-1].append(ord("a")-96)
            elif lines[x][y] == "E":
                finish = (x,y)
                matrix[-1].append(ord("z")-96)
            else:
                matrix[-1].append(ord(lines[x][y])-96)
        matrix.append([])

matrix.pop(len(matrix)-1)

# print(vertices)
g = Graph(vertices)

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        # down
        if x+1 >= 0 and x+1<len(matrix) and matrix[x+1][y]-matrix[x][y]<=1:
            g.add_edge((x,y), (x+1,y))
        # right
        if y+1 >= 0 and y+1<len(matrix[x]) and matrix[x][y+1]-matrix[x][y]<=1:
            g.add_edge((x,y), (x,y+1))
        # up
        if x-1 >= 0 and x-1<len(matrix) and matrix[x-1][y]-matrix[x][y]<=1:
            g.add_edge((x,y), (x-1,y))
        # left
        if y-1 >= 0 and y-1<len(matrix[x]) and matrix[x][y-1]-matrix[x][y]<=1:
            g.add_edge((x,y), (x,y-1))

dist = {}
precedente = {}

for x in vertices:
    dist[x] = math.inf
    precedente[x] = None

dist[start] = 0
q = list(vertices)

while len(q)>0:
    u = min(q, key= lambda x:dist[x])
    q.remove(u)

    if u == finish:
        result = dist[u]
        # print(result)
        break

    if dist[u] == math.inf:
        break

    neighbours = g.get_neighbours(u)

    for v in neighbours:
        alt = dist[u] + 1
        if alt < dist[v]:
            dist[v] = alt
            precedente[v] = u
            q.append(v)

print(dist[finish])