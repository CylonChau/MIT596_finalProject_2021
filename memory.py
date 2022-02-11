#--*-- coding:utf-8 --*--
import sys

# inital param
M = 4
N = 20
QUEUE_LIST=[1,0,1,0,2,4,1,0,0,8,7,5,4,3,2,9,4,7,2,3]

class page:
    def __init__(self,num,time):      
        self.num = num  
        
        self.time = time

class main:
    # inital buffer
    def __init__(self):
        self.b = [page(-1,M-i-1) for i in range(0,M)]
        self.c = [[-1 for i in range(0,N)] for j in range(0,M)]

        self.queue = []
        self.k = -1
        self.flag =-1
        self.process()

    def print_string(self):
        print("|---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")

    
    def get_max(self,b):
        max = -1
        flag = 0
        for i in range(0,M):
            if b[i].time >max:
                max = b[i].time
                flag = i
        return flag 

    def equation(self,fold,b):
        for i in range(0,M):
            if fold == b[i].num:
                return i
        return -1
    # OPT 
    def opt(self,fold,b,index,a):
        max = -1
        val = self.equation(fold,b)
        if val >= 0:
            pass
        else:
            self.queue.append(fold)
            self.k += 1

            for j in range(0,M):
                for k in range(index+1,N):
                    if b[j].num==a[k]:
                        b[j].time = k-j
                    else:
                        b[j].time = 20

            for i in range(0, M):
                if b[i].num ==-1:
                    val = i
                    break;
                else:
                    if b[i].time > max:
                        max = b[i].time
                        val = i
            b[val].num = fold
    # LRU
    def lru(self, fold, b):
        val = self.equation(fold, b)
        if val >= 0:
            b[val].time = 0
            for i in range(0, M):
                if i != val:
                    b[i].time += 1
        else:
            self.queue.append(fold)
            self.k += 1
            val = self.get_max(b)
            b[val].num = fold
            b[val].time = 0
            for i in range(0, M):
                if (i != val):
                    b[i].time += 1

    # FIFO
    def fifo(self, fold, b):
        val = self.equation(fold, b)
        if val >= 0:
            pass
        else:
            self.queue.append(fold)
            self.k += 1
            self.flag += 1
            self.flag %= 3
            self.b[self.flag].num = fold


    # print memory
    def Myprint(self,a):
        self.print_string()
        for j in range(0, N):
            print("|%2d" % (a[j]), end=" ")
        print("|")
        self.print_string()
        for i in range(0, M):
            for j in range(0, N):
                if self.c[i][j] == -1:
                    print("|%2c" % (32), end=" ")
                else:
                    print("|%2d" % (self.c[i][j]), end=" ")
            print("|")
        self.print_string()
        
        print("\nPage Faults：%6d\nHints Number：%6d\nPage Faults Percentage：%16.6f" % (self.k + 1, (len(QUEUE_LIST) - self.k - 1),  (self.k + 1) / N) )
    # main process
    def process(self):
        a = QUEUE_LIST

        for i in range(0, N):
            self.fifo(a[i], self.b)
            self.c[0][i] = a[i]

            for j in range(0, M):
                self.c[j][i] = self.b[j].num
        print("fifo algorithms：")
        self.Myprint(a)
        self.b = [page(-1, M - i - 1) for i in range(0, M)]
        self.c = [[-1 for i in range(0, N)] for j in range(0, M)]
        self.queue = []
        self.k = -1
        for i in range(0, N):
            self.lru(a[i], self.b)
            self.c[0][i] = a[i]

            for j in range(0, M):
                self.c[j][i] = self.b[j].num
        
        print("LRU algorithms：")
        self.Myprint(a)

        # opt 
        
        self.b = [page(-1, M - i - 1) for i in range(0, M)]
        
        self.c = [[-1 for i in range(0, N)] for j in range(0, M)]
       
        self.queue = []
        self.k = -1
        for i in range(0, N):
            self.opt(a[i], self.b, i,a)
            self.c[0][i] = a[i]

            
            for j in range(0, M):
                self.c[j][i] = self.b[j].num

        
        print("OPT algorithms:")
        self.Myprint(a)



if __name__ == "__main__":
    M = input("Please input Page number default 3: ")
    M = int(M) if M.isdigit() else 3

    if M < 3 or M > 5:
        print("Page number is minimum of 3 frames maximum of 5 frames.")
        sys.exit()
    main()