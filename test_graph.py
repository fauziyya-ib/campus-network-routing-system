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

# Add all seven campus connections with their correct weights.
graph.add_edge(dorms, library, 5)
graph.add_edge(dorms, cafeteria, 6)
graph.add_edge(library, cafeteria, 3)
graph.add_edge(library, art_science, 2)
graph.add_edge(cafeteria, art_science, 4)
graph.add_edge(cafeteria, peter_okocha, 5)
graph.add_edge(art_science, peter_okocha, 7)


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

print("\nINDIVIDUAL VERTEX DEGREES")
for name in names:
    print(f"{name}: {graph.get_degree(name)}")

print("\nGRAPH TESTS")

assert len(graph.get_vertices()) == 5
assert len(graph.get_adjacency_list()) == 5

assert graph.get_all_degrees() == {
    "Dorms": 2,
    "Library": 3,
    "Cafeteria": 4,
    "Art and Science": 3,
    "Peter Okocha Hall": 2,
}

assert graph.get_neighbors("Dorms") == {
    "Library": 5,
    "Cafeteria": 6,
}

assert graph.get_neighbors("Library") == {
    "Dorms": 5,
    "Cafeteria": 3,
    "Art and Science": 2,
}

# Check that the weighted adjacency matrix is symmetric.
for i in range(len(matrix)):
    for j in range(len(matrix)):
        assert matrix[i][j] == matrix[j][i]

# Check the total number of undirected edges.
total_degree = sum(graph.get_all_degrees().values())
assert total_degree // 2 == 7

print("All graph tests passed successfully!")
