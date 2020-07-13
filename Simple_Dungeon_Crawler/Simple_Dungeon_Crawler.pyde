import random

health = 15

#Creates a 8 x 8 game grid for "drawing" the board

grid = [ [1]*8  for n in range(8)] # list comprehension
w = 70 # sets width of each cell

#Creates a 8 x 8 grid for storing the "values" in each cell 
cell = [ [""]*8  for n in range(8)]

#initialises the variables  
hearts = []
monsters= []
traps= []
blanks = []
    
#loops to create no of hearts/values
for i in range(0,6): #SET NO OF HEARTS
    hearts.append(" <3 ")
    
for i in range(0,25): #SET NO OF MONSTERS
    monsters.append(" ~www~")

for i in range(0,3): #SET NO OF TRAP
    traps.append("TRAP ")
                        
NoOfBlanks= 62 - len(hearts) - len(monsters) - len(traps)
    
for i in range(0,NoOfBlanks):
    blanks.append("     ")
    
#Merges the values and randomises the order
cellVals=hearts+monsters+blanks+traps
cellVals.append("START")
cellVals.append(" EXIT")
random.shuffle(cellVals)

#This loop helps to assign values to be written onto the cells from earlier list
counter=0
for i in range(0,8):
     
    for j in range(0,8):
        cell[i][j]=cellVals[counter]
        if cellVals[counter]=="START":
            StartX=i
            StartY=j
        if cellVals[counter]==" EXIT":
            ExitX=i
            ExitY=j
        print(counter)
        println(cell[i][j])
        counter=counter+1   

#Ensures the start cell is vieweable
grid[StartY][StartX]= -1

#Draws the board and instructions
def setup():
    size(800,600)
    
def draw():
    
    x,y = 0,0 # starting position

    for row in grid:
        for col in row:
          if col == 1:
              #fill(250,250,250) UNHIDE
              fill(128,128,128)
          else:
              fill(250,250,250)
          rect(x, y, w, w)
          x = x + w  # move right
        y = y + w # move down
        x = 0 # rest to left edge
    fill(128) 
    
    for i in range(0,8):
        for j in range(0,8):
            text(cell[i][j],((i)*w+12),((j)*w+40))
    

    text("LO-FI DUNGEON CRAWLER",600,20)
    text("----------------------------------------",600,35) 
    text("Distance To Exit",600,70)
    text("Health",600,140)
    #rect(590,280,170,280)
    text("INSTRUCTIONS",600,300)
    text("Use Dist To Exit",600,330)
    text("to find your way out",600,360)
    text("Move up/down/left/right",600,390)
    text("Beware monsters & traps",600,420)
    text(" ~www~ = -1 Life",600,450)
    text(" TRAP  = -2 Life",600,480)
    text("Hearts replenish life",600,510)
    text("   <3   = +1 Life",600,540)
                
                                                        
def mousePressed():
    global health
    background(255)
    println(mouseY/w)
    println(mouseX/w)
    println("XXXXX")
    if mouseY/w==7 and mouseX/w<>7:
        if grid[mouseY/w-1][mouseX/w]==-1 or grid[mouseY/w][mouseX/w+1] or grid[mouseY/w][mouseX/w-1]:
            grid[mouseY/w][mouseX/w] = -1 * grid[mouseY/w][mouseX/w]
            distanceToExitY=(ExitY-mouseY/w)
            distanceToExitX=(ExitX-mouseX/w)
            distanceToExit=(distanceToExitY**2+distanceToExitX**2)**0.5
            text(round(distanceToExit,1),700,70)
            for i in range(0,8):
                for j in range(0,8):
                    if i <> mouseY/w and j <> mouseX/w:
                        grid[i][j]=1
            if cell[mouseX/w][mouseY/w]==" ~www~":
                text("OUCH! That hurt",600,200)
                health=health-1
            if cell[mouseX/w][mouseY/w]=="TRAP ":
                text("AARGH! That REALLY hurt",600,200)
                health=health-2
            if cell[mouseX/w][mouseY/w]==" <3 ":
                text("Aaaahhhh...Nice!",600,200)
                health=health+1
            if cell[mouseX/w][mouseY/w]==" EXIT":
                text("YOU ESCAPED!!!",600,200)        
        else:
            text("Error Select Only Cell That Is",600,200)
            text("Up/Down/Left/Right",600,220)
            text("Relative To Current Position",600,240)
        if health <= 0:
            background(0)
            text("GAME OVER!",600,200)
            grid[ExitY][ExitX]=-1
        if health > 0: 
            text(health,660,140)
    
    if mouseY/w<>7 and mouseX/w==7:
        if grid[mouseY/w-1][mouseX/w]==-1 or grid[mouseY/w+1][mouseX/w] or grid[mouseY/w][mouseX/w-1]:
            grid[mouseY/w][mouseX/w] = -1 * grid[mouseY/w][mouseX/w]
            distanceToExitY=(ExitY-mouseY/w)
            distanceToExitX=(ExitX-mouseX/w)
            distanceToExit=(distanceToExitY**2+distanceToExitX**2)**0.5
            text(round(distanceToExit,1),700,70)
            for i in range(0,8):
                for j in range(0,8):
                    if i <> mouseY/w and j <> mouseX/w:
                        grid[i][j]=1
            if cell[mouseX/w][mouseY/w]==" ~www~":
                text("OUCH!",600,200)
                health=health-1
            if cell[mouseX/w][mouseY/w]=="TRAP ":
                text("AARGH!",600,200)
                health=health-2
            if cell[mouseX/w][mouseY/w]==" <3 ":
                text("YUMMM",600,200)
                health=health+1
            if cell[mouseX/w][mouseY/w]==" EXIT":
                text("YOU ESCAPED!!!",600,200)        
        else:
            text("Error Select Only Cell That Is",600,200)
            text("Up/Down/Left/Right",600,240)
            text("To Current Position",600,280)
        if health <= 0:
            background(0)
            text("GAME OVER!",600,200)
            grid[ExitY][ExitX]=-1
        if health > 0: 
            text(health,660,140)                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    if mouseY/w<>7 and mouseX/w<>7:
        if  grid[mouseY/w+1][mouseX/w] == -1 or grid[mouseY/w][mouseX/w+1] == -1 or grid[mouseY/w][mouseX/w-1] == -1 or grid[mouseY/w-1][mouseX/w] == -1:
            grid[mouseY/w][mouseX/w] = -1 * grid[mouseY/w][mouseX/w]
            distanceToExitY=(ExitY-mouseY/w)
            distanceToExitX=(ExitX-mouseX/w)
            distanceToExit=(distanceToExitY**2+distanceToExitX**2)**0.5
            text(round(distanceToExit,1),700,70)
            for i in range(0,8):
                for j in range(0,8):
                    if i <> mouseY/w and j <> mouseX/w:
                        grid[i][j]=1
            if cell[mouseX/w][mouseY/w]==" ~www~":
                text("OUCH!",600,200)
                health=health-1
            if cell[mouseX/w][mouseY/w]=="TRAP ":
                text("AARGH!",600,200)
                health=health-2
            if cell[mouseX/w][mouseY/w]==" <3 ":
                text("YUMMM",600,200)
                health=health+1
            if cell[mouseX/w][mouseY/w]==" EXIT":
                text("YOU ESCAPED!!!",600,200)
        else:
            text("Error Select Only Cell That Is",600,200)
            text("Up/Down/Left/Right",600,240)
            text("To Current Position",600,280)
        if health <= 0:
            background(0)
            text("GAME OVER!",600,200)
            grid[ExitY][ExitX]=-1
        if health > 0: 
            text(health,660,140)
