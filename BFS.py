from collections import defaultdict

class graph:

   def __init__(self):

      #menyimpan grafik
      self .graph= defaultdict(list)

   #fungsi nambah node
   def addEdge(self,u,v):
          self.graph[u].append(v)

   #fungsi tampilkan BFS dari grafik
   def BFS (self, s):

      #tandai node yg tidak di pilih
      visited =[False] * (max(self.graph)+1)

      #buat antrian
      queue = []

      #tandai node yg dipilih dan masukan ke antrian
      queue.append(s)
      visited[s]= True

      while queue:

          #tampilkan antrian
          s = queue.pop(0)
          print(s, end='')

          #mengambil semua node y dekat belum di pilih,tandai dan pilih lalu masukan ke antrian
          for i in self.graph[s]:
              if visited [i] == False:
                  queue.append(i)
                  visited[i] = True

#buat grafik dari diagram
g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Breadth first search(mulai dari node 2)")
g.BFS(2)






