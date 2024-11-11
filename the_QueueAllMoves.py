import copy



class theQueue:
    def __init__(self):
        
        self.queue=[]
    def pushMap(self,node , parent):
        # node.neighbors.add(parent)
        if(node.viseted == False):
            node.parent= parent
            self.queue.append(copy.deepcopy(node))
            print(f"pushMap :\n { self.queue[-1].grid}")
        

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
        
        print(f"creted CreatedFromMove Before POP : \n { self.queue[0].CreatedFromMove}")

        print(f"RemoveMapFromQueue Before POP : \n { self.queue[0].grid}")
        self.queue[0].viseted = True
        
        self.queue.pop(0)

        print(f"RemoveMapFromQueue After POP : { self.queue[0].grid}")
        print(f"creted CreatedFromMove Before POP : \n { self.queue[0].CreatedFromMove}")

    
    # def printThePath(self):
    #     for node in self.queue:
    #         for m in node.grid:
    #             for n in m :
    #                 print(f'{n} ',end='')
    #             print ()
    #         print("(----------------------------------------------------------------)")