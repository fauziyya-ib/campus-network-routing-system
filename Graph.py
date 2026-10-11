class Graph:
    def __init__(self):
        self.vertices = {}
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Add a campus location to the graph."""
        if not hasattr(vertex, "name"):
            raise TypeError("Vertex must have a name attribute.")

        name = vertex.name

        if name in self.vertices:
            raise ValueError(f"Vertex '{name}' already exists.")

        self.vertices[name] = vertex
        self.adjacency_list[name] = {}

    def get_vertex(self, name):
        """Return a vertex by its name."""
        if name not in self.vertices:
            raise ValueError(f"Vertex '{name}' does not exist.")

        return self.vertices[name]

    def add_edge(self, source, destination, weight):
        """Connect two locations with a weighted, bidirectional edge."""
        source_name = self._get_name(source)
        destination_name = self._get_name(destination)

        if source_name not in self.vertices:
            raise ValueError(f"Vertex '{source_name}' does not exist.")

        if destination_name not in self.vertices:
            raise ValueError(
                f"Vertex '{destination_name}' does not exist."
            )

        if source_name == destination_name:
            raise ValueError("A location cannot connect to itself.")

        if isinstance(weight, bool) or not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number.")

        if weight < 0:
            raise ValueError("Weight cannot be negative.")

        if destination_name in self.adjacency_list[source_name]:
            raise ValueError("This connection already exists.")

        self.adjacency_list[source_name][destination_name] = weight
        self.adjacency_list[destination_name][source_name] = weight

    def _get_name(self, vertex):
        """Accept either a Vertex object or a location name."""
        if isinstance(vertex, str):
            return vertex

        if hasattr(vertex, "name"):
            return vertex.name

        raise TypeError("Provide a Vertex object or a location name.")

    def get_neighbors(self, vertex):
        """Return the neighbors and their connection weights."""
        name = self._get_name(vertex)

        if name not in self.vertices:
            raise ValueError(f"Vertex '{name}' does not exist.")

        return self.adjacency_list[name].copy()

    def get_vertices(self):
        """Return all campus vertices."""
        return list(self.vertices.values())

    def get_adjacency_list(self):
        """Return a copy of the adjacency list."""
        return {
            name: neighbors.copy()
            for name, neighbors in self.adjacency_list.items()
        }

    def get_degree(self, vertex):
        """Return the number of connections for a location."""
        name = self._get_name(vertex)

        if name not in self.vertices:
            raise ValueError(f"Vertex '{name}' does not exist.")

        return len(self.adjacency_list[name])

    def get_all_degrees(self):
        """Return the degree of every campus location."""
        return {
            name: len(neighbors)
            for name, neighbors in self.adjacency_list.items()
        }

    def get_adjacency_matrix(self):
        """Return the weighted adjacency matrix and vertex order."""
        names = list(self.vertices.keys())

        matrix = [
            [
                self.adjacency_list[source].get(destination, 0)
                for destination in names
            ]
            for source in names
        ]

        return names, matrix

    def display_adjacency_list(self):
        """Print the network connections."""
        for name, neighbors in self.adjacency_list.items():
            connections = ", ".join(
                f"{neighbor} (weight: {weight})"
                for neighbor, weight in neighbors.items()
            )

            print(f"{name}: {connections or 'No connections'}")