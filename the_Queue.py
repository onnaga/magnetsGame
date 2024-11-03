class theQueue:
    def __init__(self):
        self.queue=[]
    def pushMap(self,map):
        self.queue.append(map)

    def RemoveMapFromQueue(self):
        self.queue.pop(0)
    def printThePath(self):
        for i in self.queue:
            for m in i.grid:
                for n in m :
                    print(f'{n} ',end='')
                print ()
            print("(----------------------------------------------------------------)")