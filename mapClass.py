import BoxClass
import random

# Example file showing a circle moving on screen
import pygame

class map :
    # initialize the mesh using the constructor  

    def __init__(self,hight=3, width=3 ,numberOfEmptyPlaces=3) :
        self.viseted =False
        self.hight = hight
        self.width = width
        self.numberOfEmptyPlaces = numberOfEmptyPlaces
        self.MapMatrix =[[0 for xx in range(width)] for yy in range(hight)] 
        self.EmptyPlaces = self.SetEmptyPlaces()

    #reject the places lass than tow 

        if(numberOfEmptyPlaces <2 ):
            print("sorry you cant start the game with less than tow Empty places")
            return 

        if(numberOfEmptyPlaces ==2):
            self.numberOfMagnets = 1
            self.numberOfIrons = 1
            
        # detect the number of Magnets and the Irons
        else:
            self.numberOfMagnets = int(numberOfEmptyPlaces /2)
            self.numberOfIrons = numberOfEmptyPlaces - self.numberOfMagnets
        
        self.SetBoxes()

        
    

    # Set Empty Places
    def  SetEmptyPlaces(self):
        arr =[] 
        
        for i in range(self.numberOfEmptyPlaces):
            row = random.randrange(0,self.hight)
            column = random.randrange(0,self.width)
            # check if there is a cell , to not put tow in same cell
            for emptyPlace in arr : 
                if(row == emptyPlace[0] and column == emptyPlace[1]):
                    return self.SetEmptyPlaces()
            arr.append([row,column])
            self.MapMatrix[row][column]=1
        return arr



    #choos the places to set every box at the start
    def SetBoxes(self):


        self.Red =[]
        self.Purple= []
        self.Gray = []
        self.AllBoxes = []


        for i in range(self.numberOfMagnets):
            row = random.randrange(0,self.hight)
            column = random.randrange(0,self.width)
            # set the red magnets 
            if(i%2 == 0 ):
                theBox =BoxClass.Box(row,column,'Red')
                if (self.BoxNotConflict(theBox,'R')):
                    self.MapMatrix[row][column] = 'R'
                    self.Red.append(theBox)
                    self.AllBoxes.append(theBox)

            # set the purble magnets
            else:
                theBox =BoxClass.Box(row,column,'Purple')
                if (self.BoxNotConflict(theBox,'P')):
                    self.MapMatrix[row][column] = 'P'
                    self.Purple.append(theBox)
                    self.AllBoxes.append(theBox)

        for i in range(self.numberOfIrons):
                row = random.randrange(0,self.hight)
                column = random.randrange(0,self.width)
                theBox =BoxClass.Box(row,column,'Gray')
                if (self.BoxNotConflict(theBox,'G')):
                    self.MapMatrix[row][column] ='G'
                    self.Gray.append(theBox)
                    self.AllBoxes.append(theBox)


    #print the mesh
    def printMesh(self) : 
        self.grid = [[0 for xx in range(self.width)] for yy in range(self.hight)] 
        Gray =[]
        Red =[]
        Purple =[]
        for emptyPlace in self.EmptyPlaces : 
            self.grid[emptyPlace[0]][emptyPlace[1]]='1'
        for i in self.Gray :
            self.grid[i.row][i.column]='G'
            Gray.append([i.row ,i.column]) 
        for i in self.Red :
            self.grid[i.row][i.column]='R'
            Red.append([i.row ,i.column])
        for i in self.Purple :
            self.grid[i.row][i.column]='P'
            Purple.append([i.row ,i.column])
        

        for i in self.grid:
            for n in i :
                print(f'{n} ',end='')
            print ()


    #print the mesh in pygame
    # def printMesh(self ,screen) : 
        
    #     grid = [[0 for xx in range(self.width)] for yy in range(self.hight)]
    #     row=0
        
    #     for i in grid:
    #         col=0
    #         for n in i :
    #             player_pos=pygame.Vector2(80*row+screen.get_width()/3, 80*col+screen.get_height()/3)
    #             pygame.draw.circle(screen, "blue", player_pos, 10)
    #             col+=1
    #         row+=1
        
    #     Gray =[]
    #     Red =[]
    #     Purple =[]
    #     for emptyPlace in self.EmptyPlaces : 

    #         grid[emptyPlace[0]][emptyPlace[1]]='1'
    #         player_pos=pygame.Vector2(80*emptyPlace[0]+screen.get_width()/3, 80*emptyPlace[1]+screen.get_height()/3)
    #         pygame.draw.circle(screen, "white", player_pos, 33)
    #     for i in self.Gray :
    #         grid[i.row][i.column]='G'
    #         Gray.append([i.row ,i.column]) 
    #         player_pos=pygame.Vector2(80*i.row+screen.get_width()/3, 80*i.column+screen.get_height()/3)
    #         pygame.draw.circle(screen, "gray", player_pos, 30)
    #     for i in self.Red :
    #         grid[i.row][i.column]='R'
    #         Red.append([i.row ,i.column])
    #         player_pos=pygame.Vector2(80*i.row+screen.get_width()/3, 80*i.column+screen.get_height()/3)
    #         pygame.draw.circle(screen, "red", player_pos, 30)
    #     for i in self.Purple :
    #         grid[i.row][i.column]='P'
    #         Purple.append([i.row ,i.column])
    #         player_pos=pygame.Vector2(80*i.row+screen.get_width()/3, 80*i.column+screen.get_height()/3)
    #         pygame.draw.circle(screen, "purple", player_pos, 30)
        


    

    def gameSolved(self):
        
        # loop in all boxes
        for i in self.AllBoxes:
            Solved =False
            print (f"-----------------------SOlved = {Solved}---------------------------")
            # loop in all Goals for every Box
            for emptyPlace in  self.EmptyPlaces:
                # if the box in goal loop to another box
                if([i.row,i.column]==emptyPlace):
                    print (f"i.row = {i.row} , i.col : {i.column} , empty place : {emptyPlace}")
                    Solved = True 
                    break
            # if the nested loop ended with solved = False then the Box isnt in the goal then we return false
            print (f"-----------------------SOlved = {Solved}---------------------------")
            if(Solved == False):
                
                return False
        # if the for end without return then its solved
        print (f"-----------------------SOlved BOFOR WIN = {Solved}---------------------------")

        return Solved

    def BoxNotConflict(self ,TheBox , type):
        print( f'THE MATRIX IS : {self.MapMatrix[TheBox.row][TheBox.column]}  - THE BOX : [{TheBox.row},{TheBox.column}] ')
        print( f'THE BOOLEAN IS  : {self.MapMatrix[TheBox.row][TheBox.column]!=0}')

        if(self.MapMatrix[TheBox.row][TheBox.column]!=0):
            print (f" --------------------------------- box conflicted BOOl is : {self.MapMatrix[TheBox.row][TheBox.column]} -----------------------" )
            TheBox.MoveUp(self.hight,self.width,self.AllBoxes) or TheBox.MoveDown(self.hight,self.width,self.AllBoxes) or TheBox.MoveRight(self.hight,self.width,self.AllBoxes) or TheBox.MoveLeft(self.hight,self.width,self.AllBoxes)
            if(self.MapMatrix[TheBox.row][TheBox.column]!=0):
                print (f"ERROR : sorry you must re run  the code becouse there is conflict in the grid " )
                exit(1)
            
            print (f" s********************************* box conflicted and FIXED ********************************" )
            self.MapMatrix[TheBox.row][TheBox.column] = type
            return True
        else:
            return True





