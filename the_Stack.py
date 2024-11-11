import copy



class theStack:
    def __init__(self):
        
        self.stack=[]
    def pushMap(self,node , parent):
        # node.neighbors.add(parent)
        if(node.viseted == False):
            node.parent= parent
            self.stack.append(copy.deepcopy(node))
            print(f"pushMap :\n { self.stack[-1].grid}")
        

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

    def RemoveMapFromStack(self):
        
        print(f"creted CreatedFromMove Before POP : \n { self.stack[-1].CreatedFromMove}")

        print(f"RemoveMapFromStack Before POP : \n { self.stack[-1].grid}")
        self.stack[-1].viseted = True
        
        self.stack.pop()

        print(f"RemoveMapFromStack After POP : { self.stack[-1].grid}")
        print(f"creted CreatedFromMove Before POP : \n { self.stack[-1].CreatedFromMove}")

    
    # def printThePath(self):
    #     for node in self.queue:
    #         for m in node.grid:
    #             for n in m :
    #                 print(f'{n} ',end='')
    #             print ()
    #         print("(----------------------------------------------------------------)")