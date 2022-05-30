from copy import deepcopy as deepc

q = []
visited = []

def compare(s0, g): # to compare the received states with the goal state and not have to type the code each time
    if (s0 == g):
        return 1
    else:
        return 0

def findPos(s): # to find the position of the movable tile 
    for i in range (len(s)):
        for j in range (len(s[0])):
            if (s[i][j] == 0):
                return [i,j]

def up(s, pos): # to move the tile up by 1 unit
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

def down(s, pos): # to move the tile down by 1 unit
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

def left(s, pos): # to move the tile left by 1 unit
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

def right(s, pos): # to move the tile right by 1 unit
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

def dist(cs, gs): # to find the distance between each current state's tile and the corresponding tile in the goal state
    d = 0
    for i in range (len(cs)):
        for j in range (len(cs[i])):
            if (cs[i][j] != gs[i][j]):
                d += 1
    return d

def enqueue(ds): # to add states to the queue to be checked later
    flag = 0
    for i in visited: # to make sure a visited state is not used again, the check is added
        if compare(i, ds[1]):
            flag = 1
            break
    if flag == 0:
        q.append(ds)

def dequeue(): # to get the new state to be run through
    q.sort()
    if (len(q) == 0):
        print("Goal can't be reached")
        exit()
    else:
        a = q.pop(0)
        elem = a[1]
        q.clear() # hill climbing algorithm, so that the better state is figured out easily
        return elem

def main(): # the main function to be run
    s0 = [[1,2,3], [8,0,4], [7,6,5]]
    goal = [[2,8,1], [0,4,3], [7,6,5]]

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
        new = dequeue()
        if dist(new, g) >= dist(curr_state, g): # to check the best solution from the hill climbing algo, the comparison
            print("The Best Solution Found is: ", curr_state)           # to check the better lesser distance
            exit()
        print("---------------------------------------------------------")
    
    

if __name__ == '__main__':
    main()
