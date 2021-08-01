from collections import defaultdict

class Graph:

  def __init__(self):

    #menyimpan grafik
    self.graph = defaultdict(list)

  #fungsi nambah node
  def addEdge(self,u,v):
    self.graph[u].append(v)

  #fungsi untuk menggunakan dfs
  def DFSUtil(self, v, visited):

    #tandai node dan tampilan
    visited.add(v)
    print(v, end= '')

    #perulangan grafik
    for neighbour in self.graph[v]:
      if neighbour not in visited:
        self.DFSUtil(neighbour,visited)

  #fungsi Dfs
  def DFS(self, v):

    #membuat garis
    visited= set()

    #memanggil fungsi DFS dan tampilkan
    self.DFSUtil(v, visited)

#membuat grafik dari diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("depth first search(mulai dari node 2)")
g.DFS(2)

