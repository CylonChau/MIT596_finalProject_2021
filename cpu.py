#--*-- coding:utf-8 --*--

import sys
from prettytable  import PrettyTable
from colorama import init, Fore, Back, Style


# output color

class Colored(object):

    def c0(self, s):
        return Back.LIGHTGREEN_EX + s + Back.RESET

    def c1(self, s):
        return Back.GREEN + s + Back.RESET

    def c2(self, s):
        return Back.YELLOW + s + Back.RESET

    def c3(self, s):
        return Back.CYAN + s + Back.RESET

    def c4(self, s):
        return Back.LIGHTCYAN_EX + s + Back.RESET

    def c5(self, s):
        return Back.MAGENTA + s + Back.RESET

    def c6(self, s):
        return Back.LIGHTRED_EX + s + Back.RESET

    def c7(self, s):
        return Back.LIGHTYELLOW_EX + s + Back.RESET

    def c8(self, s):
        return Back.LIGHTMAGENTA_EX + s + Back.RESET

    def cb(self, s):
        return Back.BLACK + s + Back.RESET

    def cx(self, s):
        return Back.BLUE + s + Back.RESET


# input function
def inPcb():
    i = 0
    while(i < n):
        print("**************************************")
        pName = input("Please input No.%d Process Name default Process %d: " % (i+1, i+1))
        pName = str(pName) if pName.isalpha() else "process %d" % (i+1)
        arriveTime = input("Please input Arrive Time default %d: " % (i+1))
        arriveTime = int(arriveTime) if arriveTime.isdigit() else i+1
        burstTime = input("Please input Brust Time default %d: "% (i+1))
        burstTime = int(burstTime) if burstTime.isdigit() else i+1

        """
        the col name is " Process name AT BT S E RT WT TT "
        
        AT = Arrival Time
        BT = Burst Time
        S = start
        E = end
        RT = Time from process arrival until its “first execution” on the CPU
        WT= Waiting Time
        TT = Time from process arrival to process completion.

        
        """
        pcb.append([pName, arriveTime, burstTime, 0, 0, 0, 0, 0])
        i += 1
 
 
# FCFS

def FCFS():
    # inital table
    tb = PrettyTable()
    tb.field_names = ["Process Name", "AT", "BT", "S", "E", "RT", "WT", "TT"] 
    # inital Gantt Chart
    color = Colored()
    gctable = PrettyTable()
    
    # sort
    pcb.sort(key = lambda x:x[1], reverse = False )
    
    # compute startTime and compeleteTime
    for i in range(n):
        if(i == 0):
            # the col name is " Process name AT BT S E RT WT TT "
            startTime = int(pcb[i][1]) # arrive time
            pcb[i][3] = startTime # start
            pcb[i][4] = startTime + int(pcb[i][2]) # end startTime+BT
            pcb[i][5] = startTime  # RT last end time. frist is zero
            pcb[i][6] = pcb[i][3] - pcb[i][1] # startTime - ArrivalTime
            pcb[i][7] = pcb[i][4] - pcb[i][1] # end - ArrivalTime
 
        elif(i > 0 and  int(pcb[i - 1][4]) < int(pcb[i][1])):
            startTime = int(pcb[i][1])
            pcb[i][3] = startTime # start 
            pcb[i][4] = startTime + int(pcb[i][2]) # end
            pcb[i][5] = pcb[i - 1][4] # RT last end time. frist is zero
            pcb[i][6] = pcb[i][3] - pcb[i][1] # startTime - ArrivalTime
            pcb[i][7] = pcb[i][4] - pcb[i][1] # end - ArrivalTime
 
        else:
            startTime = pcb[i - 1][4]
            pcb[i][3] = startTime
            pcb[i][4] = startTime + int(pcb[i][2])
            pcb[i][5] = pcb[i - 1][4] # RT last end time. frist is zero
            pcb[i][6] = pcb[i][3] - pcb[i][1] # startTime - ArrivalTime
            pcb[i][7] = pcb[i][4] - pcb[i][1] # end - ArrivalTime
 
        i += 1
    # coupute RT
    for i in range(n):
        pcb[i][5] = float(pcb[i][4] - int(pcb[i][1]))
        pcb[i][6] = float(pcb[i][5] / int(pcb[i][2]))
        i += 1
    
    SzzTime = 0
    SdqzzTime = 0
    for i in range(n):
        SzzTime = float(SzzTime + float(pcb[i][5]))
        SdqzzTime = float(SdqzzTime + float(pcb[i][6]))
        AzzTime = float(SzzTime / n)
        AdqzzTime = float(SdqzzTime / n)
    
    pcb.sort(key = lambda x:x[3], reverse = False)
    
    print("FCFS Table is:")
    for i  in range(n):

        # the col name is " Process name AT BT S E RT WT TT "
       
        tb.add_row([
            str(pcb[i][0]),
            int(pcb[i][1]),
            int(pcb[i][2]),
            int(pcb[i][3]),
            int(pcb[i][4]),
            int(pcb[i][5]),
            round(pcb[i][6], 2),
            int(pcb[i][7]),
        ])
        i += 1

    print(tb)

    
    
    field_names = []
    for i in range(pcb[len(pcb)-1][4] + 1):
        field_names.append(i)

    gctable.field_names = field_names

   
    for i in range(n):
        if(i==0 or 5%i == 0):
            func = "color.cx"
        else:
            func = "color.c{}".format(i)

        col = []
        for j in range(pcb[len(pcb)-1][4] + 1):
            
            if(j>=pcb[i][3] and j <=pcb[i][4]):
                col.append(eval(func)("  "))
            else:
                col.append(color.cb("  "))

        gctable.add_row(col)
  
    print("FCFS Table is:")
    print(gctable)

 
 
# SJF
def SJF():

    tb = PrettyTable()
    tb.field_names = ["Process Name", "AT", "BT", "S", "E", "RT", "WT", "TT"] 
    # inital Gantt Chart
    color = Colored()
    gctable = PrettyTable()

    sjf_pcb = pcb
    i = 1
    k = 0
    
    sjf_pcb.sort(key = lambda x: x[1], reverse = False)


    


    # the col.1 name is " Process name AT BT S E RT WT TT 
    startTime0 = int(sjf_pcb[0][1]) # arrive time
    sjf_pcb[0][3] = startTime0 # start
    sjf_pcb[0][4] = startTime0 + sjf_pcb[0][2] # end startTime+BT
    sjf_pcb[0][5] = startTime0 # RT last end time. frist is zero
    sjf_pcb[0][6] = sjf_pcb[0][3] - sjf_pcb[0][1] # wt startTime - ArrivalTime
    sjf_pcb[0][7] = sjf_pcb[0][4] - sjf_pcb[0][1] # tt end - ArrivalTime
 

    # sort qune
    temp_pcb = sjf_pcb[1:len(sjf_pcb)] 
    temp_pcb.sort(key=lambda x: x[2], reverse=False)
    sjf_pcb[1:len(sjf_pcb)] = temp_pcb

  
    while(i < n):
        h = 1
        
        while(int(sjf_pcb[i][1]) >= int(sjf_pcb[i - 1][4])):
            if(i == n-1):   
                startTime = sjf_pcb[i][1]
                sjf_pcb[i][3] = startTime # s start
                sjf_pcb[i][4] = startTime + int(sjf_pcb[i][2]) # end start+bt
                sjf_pcb[i][5] = startTime0 # RT last end time. frist is zero
                sjf_pcb[i][6] = sjf_pcb[i][3] - sjf_pcb[i][1] # wt startTime - ArrivalTime
                sjf_pcb[i][7] = sjf_pcb[i][4] - sjf_pcb[i][1] # tt end - ArrivalTime

                k = 1      
                break
            else:      
                temp_sjf_pcb = sjf_pcb[i]
                sjf_pcb[i] = sjf_pcb[i + h]
                sjf_pcb[i + h] = temp_sjf_pcb
                h += 1
 
                
                if( h >= n - i - 1):
                    temp_pcb2 = sjf_pcb[i:len(sjf_pcb)]
                    temp_pcb2.sort(key=lambda x: x[1], reverse=False)  
                    sjf_pcb[i:len(sjf_pcb)] = temp_pcb2
 
                    sjf_pcb[i][3] = int(sjf_pcb[i][1])
                    sjf_pcb[i][4] = int(sjf_pcb[i][1]) + int(sjf_pcb[i][2])
                    sjf_pcb[i][5] = startTime0 # RT last end time. frist is zero
                    sjf_pcb[i][6] = sjf_pcb[i][3] - sjf_pcb[i][1] # wt startTime - ArrivalTime
                    sjf_pcb[i][7] = sjf_pcb[i][4] - sjf_pcb[i][1] # tt end - ArrivalTime
 
                    temp_pcb2 = sjf_pcb[i + 1:len(sjf_pcb)]
                    temp_pcb2.sort(key=lambda x: x[2], reverse=False) 
                    sjf_pcb[i + 1:len(sjf_pcb)] = temp_pcb2
                    h = 1
                    i += 1
                else:
                 continue
        if(k == 1):
            break
        else:
            startTime = sjf_pcb[i - 1][4]
            sjf_pcb[i][3] = startTime
            sjf_pcb[i][4] = startTime + int(sjf_pcb[i][2])
            sjf_pcb[i][5] = startTime0 # RT last end time. frist is zero
            sjf_pcb[i][6] = sjf_pcb[i][3] - sjf_pcb[i][1] # wt startTime - ArrivalTime
            sjf_pcb[i][7] = sjf_pcb[i][4] - sjf_pcb[i][1] # tt end - ArrivalTime
 
            i += 1
    
    sjf_pcb.sort(key=lambda x: x[3], reverse=False)


    print("\nSJF Table is:")
    for i  in range(n):

        # the col name is " Process name AT BT S E RT WT TT "
       
        tb.add_row([
            str(sjf_pcb[i][0]),
            int(sjf_pcb[i][1]),
            int(sjf_pcb[i][2]),
            int(sjf_pcb[i][3]),
            int(sjf_pcb[i][4]),
            int(sjf_pcb[i][5]),
            round(sjf_pcb[i][6], 2),
            int(sjf_pcb[i][7]),
        ])
        i += 1

    print(tb)

    field_names = []
    for i in range(sjf_pcb[len(sjf_pcb)-1][4] + 1):
        field_names.append(i)

    gctable.field_names = field_names

   
    for i in range(n):
        if(i==0 or 5%i == 0):
            func = "color.cx"
        else:
            func = "color.c{}".format(i)

        col = []
        for j in range(sjf_pcb[len(sjf_pcb)-1][4] + 1):
            
            if(j>=sjf_pcb[i][3] and j <=sjf_pcb[i][4]):
                col.append(eval(func)("  "))
            else:
                col.append(color.cb("  "))
        gctable.add_row(col)
    
    print("SJF Gantt Chart is:")
    print(gctable)
 
 
# main processing
if __name__ == '__main__':
        pcb = []
        n = input("Please input Process number default 3: ")
        n = int(n) if n.isdigit() else 3

        if n < 3 or n > 6:
            print("min of 3 processes and maximum 6 processes.")
            sys.exit()

        inPcb()
        print("Please select algorithms: \n 1. FCFS \n 2. SJF :\n")
        m = 1
        while(m == 1):
            option = input("Please select algorithms:(input 1 or 2 to select，other key exit): ")
            option = int(option) if option.isdigit() else 0
            if(option == 1):
                FCFS()
            elif(option == 2):
                SJF()
            else:
                print("exit.")
                m = 0