from Vertex import (
    Vertex,
    dorms,
    library,
    cafeteria,
    art_science,
    peter_okocha,
)
from Graph import Graph


graph = Graph()

# Add all five campus locations.
for vertex in [
    dorms,
    library,
    cafeteria,
    art_science,
    peter_okocha,
]:
    graph.add_vertex(vertex)

# Add example connections with weights.
graph.add_edge(dorms, library, 5)
graph.add_edge(library, cafeteria, 3)
graph.add_edge(library, art_science, 4)
graph.add_edge(cafeteria, peter_okocha, 2)

print("ADJACENCY LIST")
graph.display_adjacency_list()

print("\nVERTEX DEGREES")
print(graph.get_all_degrees())

print("\nADJACENCY MATRIX")
names, matrix = graph.get_adjacency_matrix()
print("Locations:", names)

for row in matrix:
    print(row)

print("\nLIBRARY NEIGHBORS")
print(graph.get_neighbors("Library"))