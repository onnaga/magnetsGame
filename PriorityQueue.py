import copy



class PQueue:
    def __init__(self):
        self.Pqueue=[]
    def pushMap(self,node , parent):
        # node.neighbors.add(parent)
        if(node.viseted == False):
            node.parent= parent
            self.Pqueue.append(copy.deepcopy(node))
            newItemIndex = len(self.Pqueue)-1
            previousItemIndex = newItemIndex-1
            while(previousItemIndex >= 0 and newItemIndex >=0 and self.Pqueue[previousItemIndex].cost >node.cost):
                varToCopy =copy.deepcopy(self.Pqueue[previousItemIndex])
                self.Pqueue[previousItemIndex] = self.Pqueue[newItemIndex]
                self.Pqueue[newItemIndex] =varToCopy
                previousItemIndex-=1
                newItemIndex-=1



            

            print(f"pushMap :\n { self.Pqueue[-1].grid}")
        

    def printParents(self , node):
        # if(node.parent):
        if(node.parent==False):
            print('-----------------------------------------')
            for i in node.grid:
                for n in i :
                    print(f'{n} ',end='')
                print ()
            return
        else:
            self.printParents(node=node.parent)
            print('-----------------------------------------')
            for i in node.grid:
                for n in i :
                    print(f'{n} ',end='')
                print ()
            return

    def RemoveMapFromQueue(self):
        
        print(f"creted CreatedFromMove Before POP : \n { self.Pqueue[0].CreatedFromMove}")

        print(f"RemoveMapFromQueue Before POP : \n { self.Pqueue[0].grid}")
        self.Pqueue[0].viseted = True
        
        self.Pqueue.pop(0)

        print(f"RemoveMapFromQueue After POP : { self.Pqueue[0].grid}")
        print(f"creted CreatedFromMove Before POP : \n { self.Pqueue[0].CreatedFromMove}")

    
    # def printThePath(self):
    #     for node in self.queue:
    #         for m in node.grid:
    #             for n in m :
    #                 print(f'{n} ',end='')
    #             print ()
    #         print("(----------------------------------------------------------------)")