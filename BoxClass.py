class Box :
    def __init__(self,row,column,type):
        self.row = row 
        self.column=column
        self.type =type
    


    # recurcively detect that the BOX AND THE BOXES ABOVE can move Up  
    def cantMoveUp(self , hight , AllBoxes ,Purple = False ):
        if(self.row == 0):
            return True
        for i in AllBoxes :
            
            if(i.column==self.column and i.row == self.row-1 and False):#False was purple
                return i.cantMoveUp(hight,AllBoxes)
            elif(i.column==self.column and i.row == self.row-1 ):
                return True
        return False


    # recurcively detect that the BOX AND THE BOXES DOWN can move DOWN  
    def cantMoveDown(self , hight , AllBoxes ,Purple = False):
        if(self.row == hight-1):
            return True
        for i in AllBoxes : 
            if(i.column==self.column and i.row == self.row+1 and False ):#False was purple
                return i.cantMoveDown(hight,AllBoxes)
            elif(i.column==self.column and i.row == self.row+1 ):
                return True
        return False



    # recurcively detect that the BOX AND THE BOXES NEAR can move LEFT  
    def cantMoveLeft(self , width , AllBoxes , Purple = False):
        if(self.column == 0):
            return True
        for i in AllBoxes :
            
            if(i.row==self.row and i.column == self.column-1  and False):#False was purple
                return i.cantMoveLeft(width,AllBoxes)
            elif(i.row==self.row and i.column == self.column-1 ):
                return True
        return False


    # recurcively detect that the BOX AND THE BOXES NEAR can move RIGHT  
    def cantMoveRight(self , width , AllBoxes , Purple = False ):
        if(self.column == width):
            return True
        for i in AllBoxes :
            
            if(i.row==self.row and i.column == self.column+1 and False ):#False was purple
                return i.cantMoveRight(width,AllBoxes)
            elif(i.row==self.row and i.column == self.column+1):
                return True
        return False


#       MOVING UP 
    def MoveUp(self,hight ,width ,AllBoxes ,moveAnotherBoxes=False):
        if(self.cantMoveUp(hight=hight , AllBoxes=AllBoxes,Purple=self.type =='Purple')):
            print(f"YOU CANT MOVE UP type:{self.type} , [{self.row}, {self.column}] ")
            return False
        else:
            self.row = self.row-1
            if(self.type == 'Gray' or not moveAnotherBoxes):
                return True

            
        # Move the Red magnets 
        if(self.type == 'Red' and moveAnotherBoxes):
            for i in AllBoxes :
                # check in the Same column
                if(i.column == self.column):
                    # If the magnet is close to the other boxes we dont do any thing
                    if(self.row == i.row +1 or self.row == i.row -1):
                        continue
                    elif(self.row >i.row +1):
                        i.MoveDown(hight,width,AllBoxes)
                    elif(self.row <i.row -1) : 
                        i.MoveUp(hight,width,AllBoxes)
                    else:
                        print(f'Move Up function Red the Same Box : [{self.row},{self.column}]')

                    # check the Same ROW 
                if(i.row == self.row):
                    # If the magnet is close to the other boxes we dont do any thing
                    if(self.column == i.column +1 or self.column == i.column -1):
                        continue
                    elif(self.column >i.column +1):
                        i.MoveRight(hight,width,AllBoxes)
                    elif(self.column <i.column -1) : 
                        i.MoveLeft(hight,width,AllBoxes)
                    else:
                        print(f'Move Up function the Same Box : [{self.row},{self.column}]')
            return True
        # MOVE THE Purple Magnets
        if(self.type == 'Purple' and moveAnotherBoxes):
            for i in AllBoxes :
                # check in the Same column
                if(i.column == self.column):
                    # If the magnet is close to the other boxes we dont do any thing
                    if(i.row == 0 or i.row == hight -1):
                        continue
                    elif(self.row >i.row):
                        i.MoveUp(hight,width,AllBoxes)
                    elif(self.row <i.row) : 
                        continue
                    else:
                        print(f'Move Up function Purple the Same Box : [{self.row},{self.column}]')

                    # check the Same ROW 
                if(i.row == self.row):
                    # If the magnet is close to the other boxes we dont do any thing
                    if( i.column == width-1 or  i.column == 0 ):
                        continue
                    elif(self.column >i.column ):
                        i.MoveLeft(hight,width,AllBoxes)
                    elif(self.column <i.column ) : 
                        i.MoveRight(hight,width,AllBoxes)
                    else:
                        print(f'Move Up function the Same Box : [{self.row},{self.column}]')
            return True




#       MOVING DOWN 
    def MoveDown(self,hight ,width ,AllBoxes ,moveAnotherBoxes=False):
        if(self.cantMoveDown(hight=hight , AllBoxes=AllBoxes,Purple=self.type =='Purple')):
            print(f"YOU CANT MOVE Down type:{self.type} , [{self.row}, {self.column}] ")
            return False
        else:
            self.row = self.row+1
            if(self.type == 'Gray' or not moveAnotherBoxes):
                return True
        # Move the Red magnets 
        if(self.type == 'Red' and moveAnotherBoxes):
            for i in AllBoxes :
                # check in the Same column
                if(i.column == self.column):
                    # If the magnet is close to the other boxes we dont do any thing
                    if(self.row == i.row +1 or self.row == i.row -1):
                        continue
                    elif(self.row >i.row +1):
                        i.MoveDown(hight,width,AllBoxes)
                    elif(self.row <i.row -1) : 
                        i.MoveUp(hight,width,AllBoxes)
                    else:
                        print(f'Move Down function Red the Same Box : [{self.row},{self.column}]')

                    # check the Same ROW 
                if(i.row == self.row):
                    # If the magnet is close to the other boxes we dont do any thing
                    if(self.column == i.column +1 or self.column == i.column -1):
                        continue
                    elif(self.column >i.column +1):
                        i.MoveRight(hight,width,AllBoxes)
                    elif(self.column <i.column -1) : 
                        i.MoveLeft(hight,width,AllBoxes)
                    else:
                        print(f'Move DOWN function RED the Same Box : [{self.row},{self.column}]')
            return True
        # MOVE THE Purple Magnets
        if(self.type == 'Purple' and moveAnotherBoxes):
            for i in AllBoxes :
                # check in the Same column
                if(i.column == self.column):
                    # If the magnet is close to the other boxes we dont do any thing
                    if(i.row == 0 or i.row == hight -1):
                        continue
                    elif(self.row >i.row):
                        continue
                    elif(self.row <i.row) : 
                        i.MoveDown(hight,width,AllBoxes)
                    else:
                        print(f'Move Down function Purple the Same Box : [{self.row},{self.column}]')

                    # check the Same ROW 
                if(i.row == self.row):
                    # If the magnet is close to the other boxes we dont do any thing
                    if( i.column == width-1 or  i.column == 0 ):
                        continue
                    elif(self.column >i.column ):
                        i.MoveLeft(hight,width,AllBoxes)
                    elif(self.column <i.column ) : 
                        i.MoveRight(hight,width,AllBoxes)
                    else:
                        print(f'Move Down function the Same Box : [{self.row},{self.column}]')
            return True




#       MOVING LEFT 
    def MoveLeft(self,hight ,width ,AllBoxes ,moveAnotherBoxes=False):
        
        if(self.cantMoveLeft(width=width , AllBoxes=AllBoxes,Purple=self.type =='Purple')):
            print(f"YOU CANT MOVE Left type:{self.type} , [{self.row}, {self.column}] ")
            return
        else:
            self.column = self.column-1
            if(self.type == 'Gray' or not moveAnotherBoxes):
                return True
        # Move the Red magnets 
        if(self.type == 'Red' and moveAnotherBoxes):
            for i in AllBoxes :
                # check in the Same column
                if(i.column == self.column):
                    # If the magnet is close to the other boxes we dont do any thing
                    if(self.row == i.row +1 or self.row == i.row -1):
                        continue
                    elif(self.row >i.row +1):
                        i.MoveDown(hight,width,AllBoxes)
                    elif(self.row <i.row -1) : 
                        i.MoveUp(hight,width,AllBoxes)
                    else:
                        print(f'Move Left function Red the Same Box : [{self.row},{self.column}]')

                    # check the Same ROW 
                if(i.row == self.row):
                    # If the magnet is close to the other boxes we dont do any thing
                    if(self.column == i.column +1 or self.column == i.column -1):
                        continue
                    elif(self.column >i.column +1):
                        i.MoveRight(hight,width,AllBoxes)
                    elif(self.column <i.column -1) : 
                        i.MoveLeft(hight,width,AllBoxes)
                    else:
                        print(f'Move Left function the Same Box : [{self.row},{self.column}]')
            return True
        # MOVE THE Purple Magnets
        if(self.type == 'Purple' and moveAnotherBoxes):
            for i in AllBoxes :
                # check in the Same column
                if(i.column == self.column):
                    # If the magnet is close to the other boxes we dont do any thing
                    if(i.row == 0 or i.row == hight -1):
                        continue
                    elif(self.row >i.row):
                        i.MoveUp(hight,width,AllBoxes)
                    elif(self.row <i.row) : 
                        i.MoveDown(hight,width,AllBoxes)
                    else:
                        print(f'Move Up function Purple the Same Box : [{self.row},{self.column}]')

                    # check the Same ROW 
                if(i.row == self.row):
                    # If the magnet is close to the other boxes we dont do any thing
                    if( i.column == width-1 or  i.column == 0 ):
                        continue
                    elif(self.column >i.column ):
                        i.MoveLeft(hight,width,AllBoxes)
                    elif(self.column <i.column ) : 
                        continue
                    else:
                        print(f'Move Left function the Same Box : [{self.row},{self.column}]')
            return True



#       MOVING RIGHT 
    def MoveRight(self,hight ,width ,AllBoxes ,moveAnotherBoxes=False):
        if(self.cantMoveRight(width=width , AllBoxes=AllBoxes,Purple=self.type =='Purple')):
            print(f"YOU CANT MOVE Right( type:{self.type} , [{self.row}, {self.column}] )")
            return False
        else:
            self.column = self.column+1
            if(self.type == 'Gray' or not moveAnotherBoxes):
                return True
        # Move the Red magnets 
        if(self.type == 'Red' and moveAnotherBoxes):
            for i in AllBoxes :
                # check in the Same column
                if(i.column == self.column):
                    # If the magnet is close to the other boxes we dont do any thing
                    if(self.row == i.row +1 or self.row == i.row -1):
                        continue
                    elif(self.row >i.row +1):
                        i.MoveDown(hight,width,AllBoxes)
                    elif(self.row <i.row -1) : 
                        i.MoveUp(hight,width,AllBoxes)
                    else:
                        print(f'Move Left function Red the Same Box : [{self.row},{self.column}]')

                    # check the Same ROW 
                if(i.row == self.row):
                    # If the magnet is close to the other boxes we dont do any thing
                    if(self.column == i.column +1 or self.column == i.column -1):
                        continue
                    elif(self.column >i.column +1):
                        i.MoveRight(hight,width,AllBoxes)
                    elif(self.column <i.column -1) : 
                        i.MoveLeft(hight,width,AllBoxes)
                    else:
                        print(f'Move Left function the Same Box : [{self.row},{self.column}]')
            return True
        # MOVE THE Purple Magnets
        if(self.type == 'Purple' and moveAnotherBoxes):
            for i in AllBoxes :
                # check in the Same column
                if(i.column == self.column):
                    # If the magnet is close to the other boxes we dont do any thing
                    if(i.row == 0 or i.row == hight -1):
                        continue
                    elif(self.row >i.row):
                        i.MoveUp(hight,width,AllBoxes)
                    elif(self.row <i.row) : 
                        i.MoveDown(hight,width,AllBoxes)
                    else:
                        print(f'Move Right function Purple the Same Box : [{self.row},{self.column}]')

                    # check the Same ROW 
                if(i.row == self.row):
                    # If the magnet is close to the other boxes we dont do any thing
                    if( i.column == width-1 or  i.column == 0 ):
                        continue
                    elif(self.column >i.column ):
                        continue
                        
                    elif(self.column <i.column ) : 
                        i.MoveRight(hight,width,AllBoxes)
                    else:
                        print(f'Move Left function the Same Box : [{self.row},{self.column}]')
            return True




#       MOVE TO CELL
    def MoveToCell(self ,AllBoxes,hight,width, Row ,Column ):
        print(f'----------------the ROW : {Row} , Column : {Column} -----------------')
        for i in AllBoxes:
            # if the cell tryng to move to is full 
            if(i.row ==Row and i.column ==Column):
                print('----------------YOU cant move to this cell-----------------')
                return True

        
        # set the new valus
        self.row = Row
        self.column = Column

        # Move the Red magnets 
        if(self.type == 'Red' ):
            for i in AllBoxes :
                # check in the Same column
                if(i.column == self.column):
                    # If the magnet is close to the other boxes we dont do any thing
                    if(self.row == i.row +1 or self.row == i.row -1):
                        continue
                    elif(self.row >i.row +1):
                        i.MoveDown(hight,width,AllBoxes)
                    elif(self.row <i.row -1) : 
                        i.MoveUp(hight,width,AllBoxes)
                    else:
                        print(f'Move Up function Red the Same Box : [{self.row},{self.column}]')

                    # check the Same ROW 
                if(i.row == self.row):
                    # If the magnet is close to the other boxes we dont do any thing
                    if(self.column == i.column +1 or self.column == i.column -1):
                        continue
                    elif(self.column >i.column +1):
                        i.MoveRight(hight,width,AllBoxes)
                    elif(self.column <i.column -1) : 
                        i.MoveLeft(hight,width,AllBoxes)
                    else:
                        print(f'Move Up function the Same Box : [{self.row},{self.column}]')
            return True
        # MOVE THE Purple Magnets
        if(self.type == 'Purple' ):
            for i in AllBoxes :
                # check in the Same column
                if(i.column == self.column):
                    # If the magnet is close to the other boxes we dont do any thing
                    if(i.row == 0 or i.row == hight -1):
                        continue
                    elif(self.row >i.row):
                        i.MoveUp(hight,width,AllBoxes)
                    elif(self.row <i.row) : 
                        continue
                    else:
                        print(f'Move Up function Purple the Same Box : [{self.row},{self.column}]')

                    # check the Same ROW 
                if(i.row == self.row):
                    # If the magnet is close to the other boxes we dont do any thing
                    if( i.column == width-1 or  i.column == 0 ):
                        continue
                    elif(self.column >i.column ):
                        i.MoveLeft(hight,width,AllBoxes)
                    elif(self.column <i.column ) : 
                        i.MoveRight(hight,width,AllBoxes)
                    else:
                        print(f'Move Up function the Same Box : [{self.row},{self.column}]')
            return True


