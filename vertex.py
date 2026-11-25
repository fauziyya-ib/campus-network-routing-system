class Vertex:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if not isinstance(other, Vertex):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


dorms = Vertex("Dorms")
library = Vertex("Library")
cafeteria = Vertex("Cafeteria")
art_science = Vertex("Art and Science")
peter_okocha = Vertex("Peter Okocha Hall")
