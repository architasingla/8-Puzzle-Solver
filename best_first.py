
from copy import deepcopy as deepc

q = []
visited = []

def compare(s0, g):
    if (s0 == g):
        return 1
    else:
        return 0

def findPos(s):
    for i in range (len(s)):
        for j in range (len(s[0])):
            if (s[i][j] == 0):
                return [i,j]

def up(s, pos):
    row = pos[0]
    col = pos[1]
    s1 = deepc(s)
    if row == 0:
        return s1
    else:
        s1[row][col], s1[row-1][col] = s1[row-1][col], s1[row][col]
        print("---------------------------------------------------------")
        print(s1)
        return s1

def down(s, pos):
    row = pos[0]
    col = pos[1]
    s1 = deepc(s)
    if row == (len(s1) - 1):
        return s1
    else:
        s1[row][col], s1[row+1][col] = s1[row+1][col], s1[row][col]
        print("---------------------------------------------------------")
        print(s1)
        return s1

def left(s, pos):
    row = pos[0]
    col = pos[1]
    s1 = deepc(s)
    if col == 0:
        return s1
    else:
        s1[row][col], s1[row][col-1] = s1[row][col-1], s1[row][col]
        print("---------------------------------------------------------")
        print(s1)
        return s1

def right(s, pos):
    row = pos[0]
    col = pos[1]
    s1 = deepc(s)
    if col == (len(s1[row]) - 1):
        return s1
    else:
        s1[row][col], s1[row][col+1] = s1[row][col+1], s1[row][col]
        print("---------------------------------------------------------")
        print(s1)
        return s1

def dist(cs, gs):
    d = 0
    for i in range (len(cs)):
        for j in range (len(cs[i])):
            if (cs[i][j] != gs[i][j]):
                d += 1
    return d

def enqueue(ds):
    flag = 0
    for i in visited:
        if compare(i, ds[1]):
            flag = 1
            break
    if flag == 0:
        q.append(ds)

def dequeue():
    if (len(q) == 0):
        print("Goal can't be reached")
        exit()
    else:
        a = q.pop(0)
        return a[1]



def main():
    s0 = [[2,0,3], [1,8,4], [7,6,5]]
    goal = [[1,2,3], [8,0,4], [7,6,5]]

    curr_state = deepc(s0)
    g = deepc(goal)
    
    while (1):
        pos = findPos(curr_state)
        # print (pos)
        
        new_state = up(curr_state, pos)
        dis = dist(curr_state, g)
        if compare(new_state, g) == 1:
            print("Found")
            exit()
        else:
            enqueue([dis, new_state])
        
        new_state = down(curr_state, pos)
        dis = dist(curr_state, g)
        if compare(new_state, g) == 1:
            print("Found")
            exit()
        else:
            enqueue([dis, new_state])
        
        new_state = right(curr_state, pos)
        dis = dist(curr_state, g)
        if compare(new_state, g) == 1:
            print("Found")
            exit()
        else:
            enqueue([dis, new_state])
        
        new_state = left(curr_state, pos)
        dis = dist(curr_state, g)
        if compare(new_state, g) == 1:
            print("Found")
            exit()
        else:
            enqueue([dis, new_state])

        visited.append(curr_state)
        q.sort()
        curr_state = dequeue()
        print("---------------------------------------------------------")
    
    

if __name__ == '__main__':
    main()
