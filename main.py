from vertex import Vertex
from Edges import Edge
from Graph import Graph
from Dijkstra import Dijkstra


# Check whether the campus network is connected
def is_connected(graph):

    vertices = graph.get_vertices()

    if not vertices:
        return True

    visited = set()
    stack = [vertices[0].name]

    while stack:

        current = stack.pop()

        if current not in visited:

            visited.add(current)

            for neighbor in graph.get_neighbors(current):
                if neighbor not in visited:
                    stack.append(neighbor)

    return len(visited) == len(vertices)


# Create campus locations
dorms = Vertex("Dorms")
library = Vertex("Library")
cafeteria = Vertex("Cafeteria")
art_science = Vertex("Art and Science")
peter_okocha = Vertex("Peter Okocha Hall")


# Create the graph
campus_graph = Graph()


# Add locations to the graph
vertices = [
    dorms,
    library,
    cafeteria,
    art_science,
    peter_okocha
]

for vertex in vertices:
    campus_graph.add_vertex(vertex)


# Create network connections
edges = [
    Edge(dorms, library, 5),
    Edge(library, cafeteria, 3),
    Edge(cafeteria, art_science, 4),
    Edge(art_science, peter_okocha, 7),
    Edge(dorms, cafeteria, 6),
    Edge(library, art_science, 2),
    Edge(cafeteria, peter_okocha, 5)
]


# Add connections to the graph
for edge in edges:
    campus_graph.add_edge(edge.start, edge.end, edge.weight)


# Create Dijkstra object
dijkstra = Dijkstra()


# Main application menu
while True:

    print("\n================================")
    print(" CAMPUS NETWORK ROUTING APP")
    print("================================")
    print("1. View Campus Locations")
    print("2. View Network Connections")
    print("3. Check Network Connectivity")
    print("4. View Adjacency Matrix")
    print("5. Find Shortest Path")
    print("6. Exit")

    choice = input("\nEnter your choice: ").strip()


    if choice == "1":

        print("\nAvailable locations:")

        for vertex in campus_graph.get_vertices():
            print(f"- {vertex.name}")


    elif choice == "2":

        print("\nNetwork Connections:")
        campus_graph.display_adjacency_list()


    elif choice == "3":

        print("\nChecking network connectivity...")

        if is_connected(campus_graph):
            print("\nThe campus network is connected.")
            print("Every location can reach every other location.")
        else:
            print("\nThe campus network is not connected.")


    elif choice == "4":

        names, matrix = campus_graph.get_adjacency_matrix()

        print("\nWeighted Adjacency Matrix:")

        print(" " * 25 + " ".join(names))

        for name, row in zip(names, matrix):
            print(f"{name:25}", row)


    elif choice == "5":

        print("\nAvailable locations:")

        for vertex in campus_graph.get_vertices():
            print(f"- {vertex.name}")

        start_name = input("\nEnter starting location: ").strip()
        destination_name = input("Enter destination: ").strip()

        try:

            start = campus_graph.get_vertex(start_name)
            destination = campus_graph.get_vertex(destination_name)

            print("\nCalculating shortest route...")

            distances = dijkstra.find_shortest_path(
                campus_graph, start
            )

            path = dijkstra.get_path(start, destination)

            if path:

                print("\nShortest Path:")
                print(" -> ".join(path))

                print(
                    f"\nTotal Distance: "
                    f"{distances[destination.name]}"
                )

                # Display the shortest-path tree
                print("\nShortest-Path Tree:")
                print(f"Root: {start.name}")

                for child, parent in dijkstra.previous.items():
                    print(f"{parent} -> {child}")

            else:

                print("\nNo route exists between these locations.")


        except ValueError as error:

            print(f"\nError: {error}")


    elif choice == "6":

        print("\nThank you for using Campus Network Routing App.")
        print("================================")
        break


    else:

        print("\nInvalid choice. Please select 1, 2, 3, 4, 5 or 6.")