#Made by Z (zhijingeu@yahoo.com)
#This is a very simple dungeon explorer game with mostly text graphics built in Py.Processing
#Last Edited 14 Jul 2020

import random
#initialising a few variables to be used later
rand=0
#TO DO in future updates - create a Player class with "health" attribute instead of using health as a global variable
health = 3

#Creates a 8 x 8 array for "drawing" the board. Values stored on 'grid' array are meant to turn cells visible/invisible

grid = [ [1]*8  for n in range(8)] 
w = 70 # sets width of each cell

#Creates a 8 x 8 array for storing the "values" in each cell. Values stored on 'cell' array are meant to affect player health
cell = [ [""]*8  for n in range(8)]

#initialises the variables  
hearts = []
monsters= []
traps= []
blanks = []
    
#Creates the values to populate the cell array later
for i in range(0,8): #SET NO OF HEARTS
    hearts.append(" <3 ")
    
for i in range(0,24): #SET NO OF MONSTERS
    monsters.append(" ~www~")

for i in range(0,3): #SET NO OF TRAP
    traps.append("TRAP ")
                        
NoOfBlanks= 62 - len(hearts) - len(monsters) - len(traps)
    
for i in range(0,NoOfBlanks):
    blanks.append("     ")
    
#Merges the values and randomises the order and stores it into a list
cellVals=hearts+monsters+blanks+traps
cellVals.append("START")
cellVals.append(" EXIT")
random.shuffle(cellVals)

#This loop helps to assign values from the cellVals list into the cell array
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

#Ensures the starting cell is visible when game begins
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
    global health # not best programming practice I know but I had to reference these 2 variables (one for health level and another rand var for flavour text) which were declared outside this function
    global rand 
    rand=round(random.random()*10,0) # normalised random variable so it's between 0 to 10
    background(255)
    
    # tests if surrounding cells have been selected or not (i.e so that tge player can only select cells adjacent to an already "uncovered" cell)
    # handles the edge case where otherwise it would be out of index
    if mouseY/w==7 and mouseX/w<>7:  
        if grid[mouseY/w-1][mouseX/w]==-1 or grid[mouseY/w][mouseX/w+1] or grid[mouseY/w][mouseX/w-1]:
            grid[mouseY/w][mouseX/w] = -1 * grid[mouseY/w][mouseX/w]
    
    if mouseY/w<>7 and mouseX/w==7: 
        if grid[mouseY/w-1][mouseX/w]==-1 or grid[mouseY/w+1][mouseX/w] or grid[mouseY/w][mouseX/w-1]:
            grid[mouseY/w][mouseX/w] = -1 * grid[mouseY/w][mouseX/w]                                                                                             
    #handles all other regular cases                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    if mouseY/w<>7 and mouseX/w<>7:
        if  grid[mouseY/w+1][mouseX/w] == -1 or grid[mouseY/w][mouseX/w+1] == -1 or grid[mouseY/w][mouseX/w-1] == -1 or grid[mouseY/w-1][mouseX/w] == -1:
            grid[mouseY/w][mouseX/w] = -1 * grid[mouseY/w][mouseX/w]
    
    if grid[mouseY/w][mouseX/w] == -1:
        distanceToExitY=(ExitY-mouseY/w)
        distanceToExitX=(ExitX-mouseX/w)
        distanceToExit=(distanceToExitY**2+distanceToExitX**2)**0.5
        text(distanceToExit,700,70)
        for i in range(0,8):
            for j in range(0,8):
                if i <> mouseY/w and j <> mouseX/w:
                    grid[i][j]=1
        if cell[mouseX/w][mouseY/w]==" ~www~":
            if rand<=5:
                text("OUCH!",600,200)
            if rand>5:
                text("x_x",600,200)
            health=health-1
        if cell[mouseX/w][mouseY/w]=="TRAP ":
            if rand<=5:
                text("AAARGH!",600,200)
            if rand>5:
                text(":'(",600,200)
            health=health-2
        if cell[mouseX/w][mouseY/w]==" <3 ":
            if rand<=5:
                text("UmU",600,200)
            if rand>5:
                text(":)",600,200)
            health=health+1
        if cell[mouseX/w][mouseY/w]=="     ":
            if rand<=2:
                text("!_!",600,200)
            if rand>2 and rand<=4:
                text("^-^",600,200)
            if rand>4 and rand<=6:
                text("*Phew*",600,200)
            if rand>6 and rand<=8:
                text("~_~",600,200)
            if rand>8:
                text("Doobedoobedoo",600,200)
        if cell[mouseX/w][mouseY/w]==" EXIT":
            background(0)
            text("YOU ESCAPED!!!",600,200)
    
    if grid[mouseY/w][mouseX/w] <> -1:
        text("Error Select Only Cell That Is",600,180)
        text("Up/Down/Left/Right",600,200)
        text("To Current Position",600,220)
    
    if health <= 0:
        background(0)
        text("GAME OVER!",600,200)
        grid[ExitY][ExitX]=-1
    
    if health > 0: 
        text(health,660,140)
