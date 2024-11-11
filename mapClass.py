import BoxClass
import random
import logic_magnets
import numpy as np
# Example file showing a circle moving on screen

class map :
    # initialize the mesh using the constructor  

    def __init__(self,hight=3, width=3 ,numberOfEmptyPlaces=3 ) :
        self.viseted =False
        self.hight = hight
        self.width = width
        self.CreatedFromMove= False
        
        # self.neighbors=set()
        self.numberOfEmptyPlaces = numberOfEmptyPlaces
        self.MapMatrix =[[0 for xx in range(width)] for yy in range(hight)] 
        self.EmptyPlaces = self.SetEmptyPlaces()
        self.parent=False

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

        
    

    def CountTheHash(self):
        Hash =0
        p=1009
        for i in self.AllBoxes:
            index =(i.row* self.hight)+i.column
            Type =0
            if(i.type[0]=='G'):
                Type =4
            elif(i.type[0]=='P'):
                Type=5
            elif(i.type[0]=='R'):
                Type=6
            Hash +=Type*(p**index)
        return Hash

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


        self.AllBoxes = []

        indexOfMagnet=0
        for i in range(self.numberOfMagnets):
            indexOfMagnet+=1
            row = random.randrange(0,self.hight)
            column = random.randrange(0,self.width)
            # set the red magnets 
            if(i%2 == 0 ):
                theBox =BoxClass.Box(row,column,f'Red{indexOfMagnet}')
                if (self.BoxNotConflict(theBox,'R')):
                    self.MapMatrix[row][column] = 'R'
                    
                    self.AllBoxes.append(theBox)

            # set the purble magnets
            else:
                theBox =BoxClass.Box(row,column,f'Purple{indexOfMagnet}')
                if (self.BoxNotConflict(theBox,'P')):
                    self.MapMatrix[row][column] = 'P'
                    
                    self.AllBoxes.append(theBox)

        for i in range(self.numberOfIrons):
                row = random.randrange(0,self.hight)
                column = random.randrange(0,self.width)
                theBox =BoxClass.Box(row,column,'Gray')
                if (self.BoxNotConflict(theBox,'G')):
                    self.MapMatrix[row][column] ='G'
                    
                    self.AllBoxes.append(theBox)


    #print the mesh
    def printMesh(self) : 
        self.grid = np.array([[0 for xx in range(self.width)] for yy in range(self.hight)],dtype='|U21')

        for emptyPlace in self.EmptyPlaces : 
            self.grid[emptyPlace[0]][emptyPlace[1]]='1'
        
        for i in self.AllBoxes:
            # if(i.type == 'Gray') :
            #     self.grid[i.row,i.column]='G'
            
            # elif(i.type[0] == 'R') :
                self.grid[i.row,i.column]=i.type[0]
            
            # elif(i.type[0] == 'P')  :
            #     self.grid[i.row,i.column]='P'
            

        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(self.grid)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # for i in self.grid:
        #     for n in i :
        #         print(f'{n} ',end='')
        #     print ()














    def gameSolved(self):
        
        # loop in all boxes
        for i in self.AllBoxes:
            Solved =False
            # loop in all Goals for every Box
            for emptyPlace in  self.EmptyPlaces:
                # if the box in goal loop to another box
                if([i.row,i.column]==emptyPlace):
                    Solved = True 
                    break
            # if the nested loop ended with solved = False then the Box isnt in the goal then we return false
            if(Solved == False):
                
                return False
        # if the for end without return then its solved

        return Solved

    def BoxNotConflict(self ,TheBox , type):
        print( f'THE MATRIX IS : {self.MapMatrix[TheBox.row][TheBox.column]}  - THE BOX : [{TheBox.row},{TheBox.column}] ')
        print( f'THE BOOLEAN IS  : {self.MapMatrix[TheBox.row][TheBox.column]!=0}')

        if(self.MapMatrix[TheBox.row][TheBox.column]!=0):
            print (f" --------------------------------- box conflicted BOOl is : {self.MapMatrix[TheBox.row][TheBox.column]} -----------------------" )
            TheBox.MoveUp(self.hight,self.width,self.AllBoxes) or TheBox.MoveDown(self.hight,self.width,self.AllBoxes) or TheBox.MoveRight(self.hight,self.width,self.AllBoxes) or TheBox.MoveLeft(self.hight,self.width,self.AllBoxes)
            if(self.MapMatrix[TheBox.row][TheBox.column]!=0):
                print (f"ERROR : sorry you must re run  the code becouse there is conflict in the grid " )
                logic_magnets.main()
            print (f" s********************************* box conflicted and FIXED ********************************" )
            self.MapMatrix[TheBox.row][TheBox.column] = type
            return True
        else:
            return True





