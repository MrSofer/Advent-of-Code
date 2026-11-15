import math

PATH : str = "input.txt"
PAIRS_TO_CHECK = 1000
TOP_CIRCUITS = 3

def read_points(path:str) -> list[tuple]:

    with open(path, "r", encoding="utf-8") as file:
        content : str = file.read()
    return [tuple(map(int, line.split(","))) for line in content.splitlines()]

def pairs_by_distance(points) -> list[tuple[int, int]]:
    distances_list: list = [(math.dist(points[i],points[j]), i, j) for i in range(len(points)) for j in range(i+1, len(points))]
    distances_list.sort(key =lambda x: x[0])
    return [(i,j) for (_,i,j) in distances_list]

class Circuits:
    def __init__(self,n:int):
        self.circuit_of = {point: {point} for point in range(n)}
        self.remaining = n

    def union(self, a:int, b:int) -> None:

        if self.circuit_of[a] is self.circuit_of[b]:
            return

        for num in self.circuit_of[b]:
            self.circuit_of[a].add(num)
            self.circuit_of[num] = self.circuit_of[a]

        self.remaining -= 1

    def sizes(self) -> list[int]:
        circuits = {id(s): s for s in self.circuit_of.values()}.values()
        return sorted((len(c) for c in circuits), reverse=True)

    def all_connected(self) -> bool:
        return self.remaining == 1


def part_one(points,pairs,n_pairs:int,top:int) -> int:
    circuits = Circuits(len(points))
    for a,b in pairs[:n_pairs]:
        circuits.union(a,b)
    return math.prod(circuits.sizes()[:top])

def part_two(points,pairs) -> int:
    circuits = Circuits(len(points))
    for a,b in pairs:
        circuits.union(a,b)
        if circuits.all_connected():
            return points[a][0] * points[b][0]



if __name__ == "__main__":

    points = read_points(PATH)

    pairs = pairs_by_distance(points)

    print(part_one(points,pairs,PAIRS_TO_CHECK,TOP_CIRCUITS))
    print(part_two(points,pairs))