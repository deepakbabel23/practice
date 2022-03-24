class Node:
    def __init__(self, name) -> None:
        self.name = name

class Graph:
    def __init__(self, name="test_graph") -> None:
        self.adjacency_list = {}
        self.name = name
    
    def add_vertex(self, name):
        self.adjacency_list[name] = []
        pass
    
    def remove_vertex(self, name):
        for vertex in self.adjacency_list[name]:
            self.adjacency_list[vertex].remove(name)
        del self.adjacency_list[name]

    def add_edge(self, from_vertex, to_vertex, type="bidirectional"):
        self.adjacency_list[from_vertex].append(to_vertex)
        self.adjacency_list[to_vertex].append(from_vertex)

    def remove_edge(self, from_vertex, to_vertex):
        self.adjacency_list[from_vertex].remove(to_vertex)
        self.adjacency_list[to_vertex].remove(from_vertex)
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,"\t",self.adjacency_list[vertex])

if __name__=="__main__":
    print("start of graph")
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_vertex('F')

    graph.add_edge('A','B',type="bidirectional")
    graph.add_edge('A','C',type="bidirectional")
    graph.add_edge('A','D',type="bidirectional")
    graph.add_edge('B','C',type="bidirectional")
    graph.add_edge('B','E',type="bidirectional")
    graph.add_edge('D','F',type="bidirectional")
    graph.add_edge('E','F',type="bidirectional")

    graph.print_graph()
    graph.remove_edge('A','B')
    graph.remove_edge('B','C')
    print("updated graph after removing edge A-B & B-C")
    graph.print_graph()
    print("original graph after undoing:")
    graph.add_edge('A','B')
    graph.add_edge('B','C')
    graph.print_graph()

    print("now removing vertex:B")
    graph.remove_vertex('B')
    graph.print_graph()

    """
          D -------  A 
          |          | \
          F -- E --  B--C
    """