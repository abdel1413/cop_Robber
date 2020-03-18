# COMMENTS:
# Modified by Kerry Ojakian from Aboulaye
#Testing Jeff 
 # TESTING
class CopRobGame:
    def __init__(self,move = 25):
        self.move = move
        self.graph = []
        self.edges =[]
        self.players ={'C':None, 'R':None}

       
         
    def createVertex(self,v):
        self.graph.append(v)
         
 
    def createEdge(self,e1,e2):
        self._e1 = e1
        self._e2 = e2
        sameedge = (self._e1,self._e2)
        sameedge2 = (self._e2,self._e1,)
        if (self._e1 != self._e2) and self._e1 in self.graph and self._e2 in self.graph and sameedge not in self.edges and sameedge2 not in self.edges:
            self.edges.append((self._e1 ,self._e2))
            return True
        else:
            return False
 
      
                 
    def placePlayer(self,P,N):
        self.players[P] = N
  

    def movePlayer(self,P,V):

        if V in self.graph:
            if (V, self.players[P]) in self.edges or (self.players[P],V) in self.edges:
                self.players[P] = V
                self.move = self.move-1
                return True
            else:
                return False

        
 
    def winCheck(self):
        if self.players['C'] == self.players['R']:
            return 'C'
        elif self.move <= 0:
            return 'R'
        else:   
            return 'X'
     
    def display(self):
        print("Players: ", self.players)
        print("Vertices: ", self.graph)
        print("Edges: ", self.edges)


 
 
def testCopRobber():
    G = CopRobGame(10)
    G.createVertex('a')
    G.createVertex('b')
    G.createVertex('c')
    G.createVertex('d')
    G.createEdge('a', 'b')
    G.createEdge('b', 'c')
    G.createEdge('c', 'a')
 
    print("Should return True: ", G.createEdge('c', 'd') ) # Returns True
    print("Should return False: ", G.createEdge('d', 'c') ) # Returns False
    G.placePlayer('C', 'c')
    G.placePlayer('R', 'a')
 
    print("Should print X: ", G.winCheck()) # Prints 'X'
    G.movePlayer('C', 'a')
    print("Should print C: ", G.winCheck()) # Prints 'C'
    G.display() # PRINTS WHAT FOLLOWS ...
 
    #Cop: a    Robber: a
    #Vertices: a, b, c, d
    #Edges: (a,b) (b,c) (c,a) (c,d)
 
    G.movePlayer('C', 'b')
    G.display()

    # TEST THIS OUT MORE!
    # TKINTER - Email with 3 tkinter - Look at Helper3
    
