

# 0 0 0 P
# 0 0 1 1
# R 1 1 G
# 0 G 0 0


4414309911705308380353971382985790
6621464867020807927235642450678037
8828619822340568494699714104720714

import mapClass
import the_QueueAllMoves
import copy
import numpy as np
import GraphClass
import random
import sys
import the_Stack

sys.setrecursionlimit(600000)
queue =  the_QueueAllMoves.theQueue() 
the_stack =  the_Stack.theStack() 
viseted = set()
# in CMD
# def bfsSearch(map):
    
#     print(f"Set length : {len(viseted)}  ")
#     for i in map.AllBoxes:
#         # if( map.CreatedFromMove == i.type ):
#         #     print(f"CreatedFromMove : {map.CreatedFromMove}  ")
#         #     continue
#         map.printMesh()
#         row =i.row
#         column =i.column
#         if(i.type!='Gray'):
#             print('--------------------------------------------------------------------------------')
#             for Row1 in range(map.hight):
#                 for Col1 in range(map.width):
#                     # return true when it can move to empty cell
#                     parent = copy.deepcopy(map)
#                     print('--------------------------------------------------------------------------------')
#                     moved= i.MoveToCell(map.AllBoxes,map.hight,map.width , Row1,Col1 )
#                     map.printMesh()
#                     # print (f">>>>>>>>>>>>>>>>>>>>>> the Parent : {np.array_equal(parent.grid , map.grid)} ")
                    
#                     if(moved):
#                         TheHash = map.CountTheHash()
#                         print(not TheHash in  viseted)
#                         print(f"the hash {TheHash}")
#                         print(map.grid)
                        

#                         print(not TheHash in  viseted)
                        
#                         if(not TheHash in  viseted  ):
#                             map.CreatedFromMove=i.type
#                             queue.pushMap(node=map ,parent=parent )
#                             viseted.add(TheHash)
#                             print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> queue {len(queue.queue)}   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
#                             print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Set {len(viseted)}   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
#                             print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  {len(viseted) - len(queue.queue)}   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
#                             if(map.gameSolved()):
#                                 queue.printParents(map)
#                                 return
#                         else:
#                             print ('adddddddddd')
#     print ('---------------------------------------')
#     print ('---------------------------------------')
#     print ('---------------------------------------')
#     print ('---------------------------------------')
#     print ('---------------------------------------')
#     print ('---------------------------------------')
#     print ('------------------ Rounds ---------------------')
    
#     queue.RemoveMapFromQueue()
#     print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> queue {len(queue.queue)}   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
#     bfsSearch(map=copy.deepcopy(queue.queue[0]) )

# in CMD
def dfsSearch(map):
    
    print(f"Set length : {len(viseted)}  ")
    for i in map.AllBoxes:
        # if( map.CreatedFromMove == i.type ):
        #     print(f"CreatedFromMove : {map.CreatedFromMove}  ")
        #     continue
        map.printMesh()
        row =i.row
        column =i.column
        if(i.type!='Gray'):
            print('--------------------------------------------------------------------------------')
            for Row1 in range(map.hight):
                for Col1 in range(map.width):
                    # return true when it can move to empty cell
                    parent = copy.deepcopy(map)
                    print('--------------------------------------------------------------------------------')
                    moved= i.MoveToCell(map.AllBoxes,map.hight,map.width , Row1,Col1 )
                    map.printMesh()
                    # print (f">>>>>>>>>>>>>>>>>>>>>> the Parent : {np.array_equal(parent.grid , map.grid)} ")
                    
                    if(moved):
                        TheHash = map.CountTheHash()
                        print(not TheHash in  viseted)
                        print(f"the hash {TheHash}")
                        print(map.grid)
                        

                        print(not TheHash in  viseted)
                        
                        if(not TheHash in  viseted  ):
                            map.CreatedFromMove=i.type
                            the_stack.pushMap(node=map ,parent=parent )
                            viseted.add(TheHash)
                            print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stack {len(the_stack.stack)}   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Set {len(viseted)}   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  {len(viseted) - len(the_stack.stack)}   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            if(map.gameSolved()):
                                the_stack.printParents(map)
                                return
                            dfsSearch(map=copy.deepcopy(the_stack.stack[-1]))
                        else:
                            print ('adddddddddd')
    print ('---------------------------------------')
    print ('---------------------------------------')
    print ('---------------------------------------')
    print ('---------------------------------------')
    print ('---------------------------------------')
    print ('---------------------------------------')
    print ('------------------ Rounds ---------------------')
    
    the_stack.RemoveMapFromStack()
    print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> queue {len(the_stack.stack)}   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    

def main():

    hight= int(input("ENTER: hight of grid "))
    width= int(input("ENTER:width of grid "))
    number_of_empty= int(input("ENTER: number_of_empty places "))
    map = mapClass.map(hight=hight,width=width,numberOfEmptyPlaces=number_of_empty)
    map.printMesh()
    
    # ------------bfsSearch------------
    # queue.pushMap(node=map ,parent=False)
    # viseted.add(map.CountTheHash())
    # bfsSearch(map=map)

    # ------------bfsSearch------------
    the_stack.pushMap(node=map ,parent=False)
    viseted.add(map.CountTheHash())
    dfsSearch(map=map)




if __name__ == '__main__':
    main()
