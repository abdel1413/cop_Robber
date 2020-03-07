#from copRobGamProf import*
from tkinter import *


root = Tk()
root.title("===CopRobGame===")
root.configure(background = "#00faff")

can = Canvas(width = 600,height = 600,bg = '#41f49d')
def layOut(e):
    Title = Label(root,text = "=== Welcome to CopRobGame===",font ='Arial 25 bold',bg = 'f4c542')
    Title.grid(row = 0 ,column = 3)


def cPrint(e):
    print("You picked: ", e.x, e.y)


def placeVertex(can, x, y, label):

    size = 40
    x1 = x - size/2
    y1 = y - size/2
    x2 = x + size/2
    y2 = y + size/2
    rect = can.create_oval(x1,y1,x2,y2,fill='yellow')
    rectText = can.create_text(x,y, text = label)
    can.tag_bind(rect, '<ButtonPress-1>',lambda e:CreateEdge(x,y))
    can.tag_bind(rectText, '<ButtonPress-1>',lambda e:CreateEdge(x,y))

board = Canvas(width = 400, height = 400,bg = "#73f441")

label = Label(root,text = "xcoord :")
xCoord = Entry(root,width = 5)
label.grid(row = 0, column = 0,sticky = E)
xCoord.grid(row = 0,column = 1)

label2 = Label(root,text = "ycoord :",)
yCoord = Entry(root,width = 5)
label2.grid(row = 1, column =0 ,sticky = E)
yCoord.grid(row = 1,column = 1)

label3 = Label(root,text = "Enter Vertex:")
name   = Entry(root,width = 5)
label3.grid(row = 3, column = 0,sticky = E)
name.grid(row = 3,column = 1)

enter  = Button(text = "Click",fg = 'blue')
enter.bind('<Button-1>', lambda e: placeVertex(board,eval(xCoord.get()), eval(yCoord.get()),name.get()))
L = []
def CreateEdge(x,y):
    global L
    print(L)
    L.append((x,y))
    
    
def connect(can ,x,y):
    global L
    for i in L:
        for j in L[1:]:
           can.create_line(i[0],i[1],j[0],j[1])
    L.clear()
b = Button(root,text = 'CONNECT',bg = '#f1f442')
b.bind('<Button-1>',lambda e:connect(board,eval(xCoord.get()), eval(yCoord.get())))
b.place(x = 70, y = 150)


player = Label(root,text = 'Player',font = 'Arial 20 bold',bg = '#f48942')

player.place(x = 0,y = 200)
entry1 = Entry(root,width = 5)
entry1.place(x = 90,y = 235)

v_name = Label(root,text = "V_name:",font='Arial 17 bold' )
v_name.place(x= 0,y = 235)
entry2 = Entry(root,width = 5)
entry2.place(x = 90,y = 200)

box = Button(root,text = 'CLICK',fg = 'blue')
box.bind('<Button-1>',lambda e:PlacePlayer(board,eval(xCoord.get()), eval(yCoord.get,name.get()))) 
box.place(x = 90, y = 265)

def placeP():
    name = StringVar()
    name.set("place Cop at Vx")
    instruction = Label(root,textvariable = name,font = 'Arial 12 bold')
    instruction.bind('<Button-1>',lambda e:PlacePlayer(board,eval(xCoord.get()), eval(yCoord.get(),name.get()))) 
    instruction.place(x = 0 ,y = 140)

def PlacePlayer(can,event): 
   
    xy = event.widget.place_info()
    players=[]
    if placed == 1:
        cop =Label(can,text = 'C',bg = 'White')
        cop.place(x = (xy['x']),y = xy['Y'])
        players.append(cop)
        name.set('R at any vtx')
        cop_pos = event.widget.cget('Text')

    elif placed == 2:
        robber =Label(canvas,text = 'R',bg = 'White')
        player.place(x = (xy['x']),y = xy['y'])
        name.set("Cop,select vtx where you want to go")
        players.append(robber)
        robber_pos = event.widget.cget('text')


movelabel = Label(root,text = 'Move_P',font = 'Arial 20 bold',bg = '#f48942')
movelabel.place(x = 0,y = 350)
entrybox = Entry(root,width = 5)
entrybox.place(x = 90,y = 350)

v_label = Label(root,text = 'vertex',font = 'Arial 20 bold',bg = '#f48942')
v_label.place(x = 0,y = 390)
vertxbox =Entry(root,width = 5)
vertxbox.place(x = 90,y = 390)
movebutton = Button(root,text = 'CLICK',fg = 'blue')
movebutton.place(x = 90,y = 430)
movebutton.bind('<Button - 1>',lambda e : movePlayer(xy,pos))

enter.grid(row = 4,column = 1)
board.grid(row = 5,column = 3)
root.mainloop()

legalmove = 0
def movePlayer(xy,pos):
    for v in legalmoves:
        if placed%2 == 0:
            if cop_pos == v and pos in legalmove[v]:
                cop.place_forget()
                cop.place(x = int(xy['x']) - 10,y = xy['y'])
                cop_pos = pos
                legalmove += 1
                break  

        else:
            if robber_pos == v and pos in self.legalmove[v]:
                robber.place_forget()
                robber.place(x = int(xy['x'])-10,y = xy['y'])
                robber_pos = pos
                legalmove +=1
                if coprob.move == 0:
                   name.set('Robber won the game!!!')
                   movebottom.place_forget()
            else:
                if cop_pos == robber_pos:
                    name.set('Cop won the game!!')
                    movebottom.place_forget()
                    break
            
        
