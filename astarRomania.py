#
#   User: Rizky Andre Wibisono
#
# Modified by: Lucas Cavalcanti and Roberto Fernandes

import heapq
import random

class priorityQueue:
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)
    
    def border(self):
        return sorted(self.cities)

    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False

    def check(self):
        print(self.cities)


class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)


romania = {}

def makedict():
    file = open("romania.txt", 'r')
    for string in file:
        line = string.split(',')
        ct1 = line[0]
        ct2 = line[1]
        dist = int(line[2])
        romania.setdefault(ct1, []).append(ctNode(ct2, dist))
        romania.setdefault(ct2, []).append(ctNode(ct1, dist))


def make_huristik_dict():
    h = {}
    with open("romania_sld.txt", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h


def heuristic(node, values):
    return values[node]


def astar(start, end):
    path = {}
    distance = {}
    q = priorityQueue()
    h = make_huristik_dict()
    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []
    printoutput(start, end, path, distance, expandedList, q, 0)

    while (q.isEmpty() == False):
        current = q.pop()[1]
        expandedList.append(current)

        if (current == end):
            break

        for new in romania[current]:
            g_cost = distance[current] + int(new.distance)
            if (new.city not in distance or g_cost < distance[new.city]):
                distance[new.city] = g_cost
                f_cost = g_cost + heuristic(new.city, h)
                q.push(new.city, f_cost)
                path[new.city] = current
        printoutput(start, end, path, distance, expandedList, q, 1)

    printoutput(start, end, path, distance, expandedList, q, 2)


def printoutput(start, end, path, distance, expandedlist, q, stage):
    finalpath = []
    i = end

    if stage == 0:
        print("\nPrograma com busca heurística A* no mapa da Romênia\n")
        print("\t" + str(start) + " => Bucharest\n")
        print("=======================================================\n")
    elif stage > 0:
        print("Fronteira de Busca \t\t: " + str(q.border()))
        print("Cidades Expandidas \t\t: " + str(expandedlist) + "  #" + str(len(expandedlist)) + "\n")
    if stage == 2:
        while (path.get(i) != None):
            finalpath.append(i)
            i = path[i]
        finalpath.append(start)
        finalpath.reverse()
        print("\n=======================================================\n")
        print("Menor caminho \t: " + str(finalpath))
        print("Número de cidade visitas \t\t\t: " + str(len(finalpath)))
        print("Distância total percorrida \t\t\t: " + str(distance[end]) + "\n\n")


def main():
    makedict()
    src = "Bucharest"
    dst = "Bucharest"
    while src == dst: 
        s = random.choice(list(romania.items()))[0]
        src = str(s)
    astar(src, dst)


if __name__ == "__main__":
    main()
