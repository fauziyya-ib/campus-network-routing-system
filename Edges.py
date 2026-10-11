Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Edge:
    def __init__(self, start, end, weight=1):
        if not isinstance(start, Vertex) or not isinstance(end, Vertex):
            raise TypeError("Edges must connect Vertex objects")
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self):
        return f"{self.start} --({self.weight})--> {self.end}"

    def __eq__(self, other):
        return (isinstance(other, Edge) and
                self.start == other.start and
                self.end == other.end and
                self.weight == other.weight)

    def __hash__(self):
        return hash((self.start, self.end, self.weight))


edge1 = Edge(dorms, library, 5)          
edge2 = Edge(library, cafeteria, 3)      
edge3 = Edge(cafeteria, art_science, 4)  
edge4 = Edge(art_science, peter_okocha, 7)
edge5 = Edge(dorms, cafeteria, 6)        
edge6 = Edge(library, art_science, 2)    
edge7 = Edge(cafeteria, peter_okocha, 5) 
