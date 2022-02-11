#--*-- coding:utf-8 --*--
import random
import copy
import sys

from prettytable  import PrettyTable

SCAN_DIRECTION = 1                    # 1表示向磁道号增加的方向扫描，0表示向磁道号减小的方向
LOOK_DIRECTION = 1
TRACK_MAX_COUNT = 0
TRACK_START = 0


def default_case(s):
    print("")
    print("Invalid selected, Please select algorithms: \n 1. FCFS \n 2. SSTF :\n 3. SCAN : \n 4. CSCAN : \n 5. CSCAN :")

#*********************FCFS**************************/
def FCFS(track_request):

    tb = PrettyTable()
    tb._validate_field_names = lambda *a, **k: None

    field_names = ["track request"]
    queue_FCFS = track_request.copy()
    queue_FCFS.insert(0,TRACK_START)

    traversed_queue = []
    current = TRACK_START

    for n in range(len(queue_FCFS)):
        field_names.append(str(queue_FCFS[n]))
        curr_temp = abs(queue_FCFS[n % TRACK_REQUEST_COUNT] - current)
        traversed_queue.append(curr_temp)
        current = queue_FCFS[n % TRACK_REQUEST_COUNT]


    tb.field_names = field_names
    col = ["tracking number"]
    for n in range(len(traversed_queue)):
        col.append(traversed_queue[n])

    tb.add_row(col)

    print("current point position is: %d" % TRACK_START)
    print("FCFS tracks traversed table: ")
    print(tb)
    caculate(traversed_queue)


 

def findNearest(current,track_request,visited):
    minDis = TRACK_MAX_COUNT
    minIndex = -1
    for i in range(len(track_request)):
        if visited[i] == False:
            dis = abs( current - track_request[i])
            if dis < minDis:
                minDis = dis
                minIndex = i
    visited[minIndex] = True
    return minIndex, minDis
 
def SSTF(track_request):
    visited = [False] * TRACK_REQUEST_COUNT
    queue_FCFS = []

    traversed_queue = []
    current = TRACK_START
    current1 = TRACK_START

    for i in range(len(track_request)+1):
        index, dis = findNearest(current, track_request, visited)
        queue_FCFS.append(current)
        current = track_request[index]

    tb = PrettyTable()
    tb._validate_field_names = lambda *a, **k: None
    field_names = ["track request"]


    for n in range(len(queue_FCFS)):
        field_names.append(str(queue_FCFS[n]))
        curr_temp = abs(queue_FCFS[n] - current1)
        traversed_queue.append(curr_temp)
        current1 = queue_FCFS[n]

    tb.field_names = field_names

    col = ["tracking number"]
    for n in range(len(queue_FCFS)):
        col.append(traversed_queue[n])

    tb.add_row(col)

    print("current point position is: %d" % TRACK_START)
    print("SSTF tracks traversed table: ")
    print(tb)
    caculate(traversed_queue)

#**********************SCAN********************
def SCAN(track_request):
    global SCAN_DIRECTION
    queue_SCAN = []
    queue_SCAN.insert(0, TRACK_START)

    track_request_copy = copy.deepcopy(track_request)
    track_request_copy.sort()

    traversed_queue = []
    current1 = TRACK_START


    while track_request_copy.__len__() != 0:
        if SCAN_DIRECTION == 1:
            for track in track_request_copy.copy():
                if TRACK_START <= track:
                    queue_SCAN.append(track)
                    track_request_copy.remove(track)
            SCAN_DIRECTION = 0
 
        if SCAN_DIRECTION == 0:
            track_request_copy.reverse()
            for track in track_request_copy.copy():
                if TRACK_START >= track:
                    queue_SCAN.append(track)
                    current = track
                    track_request_copy.remove(track)
            SCAN_DIRECTION = 1

    tb = PrettyTable()
    tb._validate_field_names = lambda *a, **k: None
    field_names = ["track request"]


    for n in range(len(queue_SCAN)):
        field_names.append(str(queue_SCAN[n]))
        curr_temp = abs(queue_SCAN[n] - current1)
        traversed_queue.append(curr_temp)
        current1 = queue_SCAN[n]


    tb.field_names = field_names

    col = ["tracking number"]
    for n in range(len(queue_SCAN)):
        col.append(traversed_queue[n])

    tb.add_row(col)
    print("current point position is: %d" % TRACK_START)
    print("SCAN tracks traversed table: ")
    print(tb)
    caculate(traversed_queue)
 
 
#**********************CSCAN********************
def CSCAN(track_request):
    global SCAN_DIRECTION
    queue_CSCAN = []
    queue_CSCAN.append(TRACK_START)
    track_request_copy = copy.deepcopy(track_request)
    track_request_copy.sort()
    traversed_queue = []
    traversed_queue.append(abs(queue_CSCAN[0] - TRACK_START))
    current = TRACK_START
    i = 0
    is_find = False
 
    if SCAN_DIRECTION == 1:
        while i < track_request_copy.__len__():
            if (TRACK_START <= track_request_copy[i] ) & (is_find == False):
                index = i
                i = 0
                is_find = True
            if is_find == True:
                queue_CSCAN.append(track_request_copy[index % TRACK_REQUEST_COUNT])
                curr_temp = abs(track_request_copy[index % TRACK_REQUEST_COUNT] - current)
                traversed_queue.append(curr_temp)
                current = track_request_copy[index % TRACK_REQUEST_COUNT]
                index += 1
            i +=1
 
    if SCAN_DIRECTION ==0:
        track_request_copy.reverse()
        while i < track_request_copy.__len__():
            if (TRACK_START >= track_request_copy[i] ) & (is_find == False):
                index = i
                i = 0
                is_find = True
            if is_find == True:
                queue_CSCAN.append(track_request_copy[index % TRACK_REQUEST_COUNT])
                index += 1
                curr_temp = abs(track_request_copy[index % TRACK_REQUEST_COUNT] - current)
                traversed_queue.append(curr_temp)
                current = track_request_copy[index % TRACK_REQUEST_COUNT]
            i +=1

    tb = PrettyTable()
    tb._validate_field_names = lambda *a, **k: None
    field_names = ["track request"]

    for n in range(len(queue_CSCAN)):
        field_names.append(str(queue_CSCAN[n]))

    tb.field_names = field_names


    col = ["tracking number"]
    for i in range(len(traversed_queue)):
        col.append(traversed_queue[i])
    tb.add_row(col)

    print("current point position is: %d" % TRACK_START)
    print("CSACN tracks traversed table: ")
    print(tb)
    caculate(traversed_queue)


#**********************LOOK********************
def LOOK(track_request):
    global LOOK_DIRECTION
    queue_LOOK = []
    queue_LOOK.insert(0, TRACK_START)

    track_request_copy = copy.deepcopy(track_request)
    track_request_copy.sort()

    traversed_queue = []
    current1 = TRACK_START

    while track_request_copy.__len__() != 0:
        if LOOK_DIRECTION == 1:
            for track in track_request_copy.copy():
                if TRACK_START <= track:
                    queue_LOOK.append(track)
                    track_request_copy.remove(track)
            LOOK_DIRECTION = 0
 
        if LOOK_DIRECTION == 0:
            track_request_copy.reverse()
            for track in track_request_copy.copy():
                if TRACK_START >= track:
                    queue_LOOK.append(track)
                    current = track
                    track_request_copy.remove(track)
            LOOK_DIRECTION = 1

    tb = PrettyTable()
    tb._validate_field_names = lambda *a, **k: None
    field_names = ["track request"]

    for n in range(len(queue_LOOK)):
        field_names.append(str(queue_LOOK[n]))
        curr_temp = abs(queue_LOOK[n % TRACK_REQUEST_COUNT] - current1)
        traversed_queue.append(curr_temp)
        current1 = queue_LOOK[n % TRACK_REQUEST_COUNT]

    tb.field_names = field_names

    col = ["tracking number"]
    for n in range(len(queue_LOOK)):
        col.append(traversed_queue[n])

    tb.add_row(col)
    print("current point position is: %d" % TRACK_START)
    print("SCAN tracks traversed table: ")
    print(tb)
    caculate(traversed_queue)


#**********************CLOOK********************
def CLOOK(track_request):
    global LOOK_DIRECTION
    queue_CLOOK = []
    queue_CLOOK.append(TRACK_START)
    track_request_copy = copy.deepcopy(track_request)
    track_request_copy.sort()
    traversed_queue = []
    traversed_queue.append(abs(queue_CLOOK[0] - TRACK_START))
    current = TRACK_START
    i = 0
    is_find = False

    if SCAN_DIRECTION == 1:
        while i < track_request_copy.__len__():
            if (TRACK_START <= track_request_copy[i]) & (is_find == False):
                index = i
                i = 0
                is_find = True
            if is_find == True:
                queue_CLOOK.append(track_request_copy[index % TRACK_REQUEST_COUNT])
                curr_temp = abs(track_request_copy[index % TRACK_REQUEST_COUNT] - current)
                traversed_queue.append(curr_temp)
                current = track_request_copy[index % TRACK_REQUEST_COUNT]
                index += 1
            i += 1

    if SCAN_DIRECTION == 0:
        track_request_copy.reverse()
        while i < track_request_copy.__len__():
            if (TRACK_START >= track_request_copy[i]) & (is_find == False):
                index = i
                i = 0
                is_find = True
            if is_find == True:
                queue_CLOOK.append(track_request_copy[index % TRACK_REQUEST_COUNT])
                index += 1
                curr_temp = abs(track_request_copy[index % TRACK_REQUEST_COUNT] - current)
                traversed_queue.append(curr_temp)
                current = track_request_copy[index % TRACK_REQUEST_COUNT]
            i += 1

    tb = PrettyTable()
    tb._validate_field_names = lambda *a, **k: None
    field_names = ["track request"]

    for n in range(len(queue_CLOOK)):
        field_names.append(str(queue_CLOOK[n]))

    tb.field_names = field_names

    col = ["tracking number"]
    for i in range(len(traversed_queue)):
        col.append(traversed_queue[i])
    tb.add_row(col)

    print("current point position is: %d" % TRACK_START)
    print("CSACN tracks traversed table: ")
    print(tb)
    caculate(traversed_queue)


def caculate(queue):
    sum_gap = sum([(abs(queue[i] - queue[i - 1])) for i in range(1, len(queue))])
    print('The average number of tracks moved is: %.2f' % (sum_gap/TRACK_REQUEST_COUNT))
    print("")
 
def initQueue(num):
    track_request = [None] * num
    for i in range(num):
        temp_num = random.randint(0, TRACK_MAX_COUNT)
        track_request[i] = temp_num
    return track_request

if __name__ == '__main__':

    TRACK_REQUEST_COUNT = input("Please input tracks number: ")       
    TRACK_MAX_COUNT = input("Please input tracks range: ")
    TRACK_START = input("Please input tracks start postion: ")

    TRACK_REQUEST_COUNT = int(TRACK_REQUEST_COUNT) if TRACK_REQUEST_COUNT.isdigit() else 12
    TRACK_MAX_COUNT = int(TRACK_MAX_COUNT) if TRACK_MAX_COUNT.isdigit() else 100
    TRACK_START = int(TRACK_START) if TRACK_START.isdigit() else 50

    if TRACK_REQUEST_COUNT < 12:
        print("The minimum number of track is 12.")
        sys.exit()

    TRACK_REQUEST_COUNT = TRACK_REQUEST_COUNT - 1

    track_request = initQueue(TRACK_REQUEST_COUNT)
 
    print('The sequence of tracks generated each time is random.\n')
    print("TRACK SEQUECE:    ", track_request, "\n")
    print("Please select algorithms: \n 1. FCFS: \n 2. SSTF:\n 3. SCAN: \n 4. CSCAN: \n 5. LOOK: \n 6. CLOOK: ")

    switch = {
        1: FCFS,
        2: SSTF,
        3: SCAN,
        4: CSCAN,
        5: LOOK,
        6: CLOOK,
    }
    m = 1
    while (m == 1):
        option = input("Please select algorithms (tips: input int 1-6 to select，other key exit.): ")
        option = int(option) if option.isdigit() else 0
        if(option >=1 and option <=6):
            switch.get(option, default_case)(track_request)
        else:
            print("exit.")
            m = 0