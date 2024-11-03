import mapClass
import pygame
import the_Queue
import NodeClass


# in pyGame
# def JumpingMove(map):
#     # pygame setup
#     pygame.init()
#     screen = pygame.display.set_mode((1280, 720))
#     screen.get_width()/3
#     clock = pygame.time.Clock()
#     running = True
#     down=0
#     right = 0
#     startPoint=pygame.Vector2(80+screen.get_width()/3-10, 80+33 +screen.get_height()/3)
#     endPoint=pygame.Vector2(80 +30+screen.get_width()/3, 80 +33+screen.get_height()/3)
#     while running:
#         pygame.event.clear()
#         # poll for events
#         # pygame.QUIT event means the user clicked X to close your window
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         # fill the screen with a color to wipe away anything from last frame
#         screen.fill("black")

#         # pygame.draw.circle(screen, "red", player_pos, 40)
#         map.printMesh(screen)
#         pygame.draw.line(screen, "green", startPoint, endPoint,3) 
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_w]:
#             startPoint.y-=80
#             endPoint.y-=80
#             down-= 1
#         if keys[pygame.K_s]:
#             startPoint.y+=80
#             endPoint.y+=80
#             down+= 1
#         if keys[pygame.K_a]:
#             startPoint.x-=80
#             endPoint.x-=80
#             right-= 1
#         if keys[pygame.K_d]:
#             startPoint.x+=80
#             endPoint.x+=80
#             right+= 1
#         if keys[pygame.K_RETURN]:
#             print("???????????????????????????????????????????????ENTER PrESSED ???????????????????????????????????????????????")
#             row =down
#             column =right
#             iteration =0
#             for i in map.AllBoxes:
#                 if(i.row == row and i.column ==column and i.type!='Gray'):
#                     if keys[pygame.K_SPACE]:
#                         print('--------------------------------------------------------------------------------')
#                         pygame.event.clear()
#                         event = pygame.event.wait()
#                         Row1= event.key
#                         pygame.event.clear()
#                         event = pygame.event.wait()
#                         Col1=event.key
#                         i.MoveToCell(map.AllBoxes,map.hight,map.width , Row1,Col1)
#                 elif(iteration==len(map.AllBoxes)-1):
#                     print(f"the row is {i.row} col: {i.column}  ")
#                     print("YOU CANT MOVE THIS cell its not magnet")
#                     iteration+=1
#             if(map.gameSolved()):
#                 print("YOU WIN" )
#                 return


#         # flip() the display to put your work on screen
#         pygame.display.flip()
#     pygame.quit()

queue =  the_Queue.theQueue() 
# in CMD
def JumpingMove(map):
    map.printMesh()
    row =int(input('ENTER THE ROW :'))
    column =int (input('ENTER THE column :'))
    iteration =0
    print(f"the row is {row} col: {column}  ")
    for i in map.AllBoxes:
        print(f" i.row is {i.row  } i. col : {i.column} \n ")

        print(f" the bool 1 is {i.row == row } col bool: {i.column ==column} \n ")
        if(i.row == row and i.column ==column and i.type!='Gray'):
            print('--------------------------------------------------------------------------------')
            Row1= int(input("ENTER the Row Moving to :"))
            Col1=int (input("ENTER the Row Moving to :"))
            i.MoveToCell(map.AllBoxes,map.hight,map.width , Row1,Col1 )
        elif(iteration==len(map.AllBoxes)-1):
            print(f"the row is {i.row} col: {i.column}  ")
            print("YOU CANT MOVE THIS cell its not magnet")
        iteration+=1
    queue.pushMap(map=NodeClass.Node(map.grid))

    if(map.gameSolved()):
        print("YOU WIN" )
        queue.printThePath()
        print ('---------------------------------------')
        map.printMesh()
        return
    JumpingMove(map=map)


def move(map):
    map.printMesh()
    row =int(input('ENTER THE ROW :'))
    column =int (input('ENTER THE column :'))
    iteration =0
    print(f"the row is {row} col: {column}  ")
    for i in map.AllBoxes:
        print(f" i.row is {i.row  } i. col : {i.column} \n ")

        print(f" the bool 1 is {i.row == row } col bool: {i.column ==column} \n ")
        if(i.row == row and i.column ==column and i.type!='Gray'):
            val= input("ENTER: w TO UP - a TO LEFT - s TO DOWN - d TO RIGHT ")
            match val:
                case "w":
                    # self,hight ,width ,AllBoxes ,moveAnotherBoxes=False
                    i.MoveUp( map.hight , map.width , map.AllBoxes,True)
                case "d":
                    i.MoveRight( map.hight , map.width , map.AllBoxes,True)
                case "s":
                    i.MoveDown( map.hight , map.width , map.AllBoxes,True)
                case "a":
                    i.MoveLeft( map.hight , map.width , map.AllBoxes,True)
                case _:
                    print("Please Enter value from four value Above")
            break
        elif(iteration==len(map.AllBoxes)-1):

            print(f"the row is {i.row} col: {i.column}  ")
            print("YOU CANT MOVE THIS cell its not magnet")
        iteration+=1
    print()
    if(map.gameSolved()):
        print("YOU WIN" )
        return
    move(map=map)

def main():
    typeOfPlay =2
    # int(input("ENTER 1 for Play step by step .... tow for play from cell to cell"))

    hight= int(input("ENTER: hight of grid "))
    width= int(input("ENTER:width of grid "))
    number_of_empty= int(input("ENTER: number_of_empty places "))
    print(f"type : {typeOfPlay}")
    if(typeOfPlay==1):
        map = mapClass.map(hight=hight,width=width,numberOfEmptyPlaces=number_of_empty)
        move(map=map)
    elif(typeOfPlay==2):
        map = mapClass.map(hight=hight,width=width,numberOfEmptyPlaces=number_of_empty)
        JumpingMove(map=map)
    else:
        print("the type ypu enter is not 1 nor 2")




if __name__ == '__main__':
    main()
