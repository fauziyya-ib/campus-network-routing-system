class Dijkstra:
    def __init__(self):
        self.distances = {}
        self.previous = {}

    def find_shortest_path(self, graph, start):
        vertices = graph.get_vertices()

        # Initialize all distances to infinity.
        self.distances = {
            vertex.name: float("inf")
            for vertex in vertices
        }

        self.previous = {}

        start_name = start.name if hasattr(start, "name") else start
        self.distances[start_name] = 0

        unvisited = set(self.distances.keys())

        while unvisited:
            current = min(
                unvisited,
                key=lambda vertex: self.distances[vertex]
            )

            if self.distances[current] == float("inf"):
                break

            unvisited.remove(current)

            for neighbor, weight in graph.get_neighbors(current).items():
                if neighbor in unvisited:
                    new_distance = self.distances[current] + weight

                    if new_distance < self.distances[neighbor]:
                        self.distances[neighbor] = new_distance
                        self.previous[neighbor] = current

        return self.distances

    def get_path(self, start, destination):
        start_name = start.name if hasattr(start, "name") else start
        destination_name = (
            destination.name if hasattr(destination, "name")
            else destination
        )

        if (
            destination_name not in self.distances
            or self.distances[destination_name] == float("inf")
        ):
            return []

        path = []
        current = destination_name

        while current is not None:
            path.append(current)

            if current == start_name:
                break

            current = self.previous.get(current)

        path.reverse()

        if not path or path[0] != start_name:
            return []

        return path