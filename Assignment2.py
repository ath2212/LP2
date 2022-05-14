class Node:
    def __init__(self, x, y, parent=None, f=0, g=0, h=0, is_blocked=False):
        self.parent  = parent
        self.x = x
        self.y = y
        self.f = f
        self.g = g
        self.h = h
        self.is_blocked = is_blocked

def get_dist(n1, n2):
    return abs(n1.x-n2.x)+abs(n1.y-n2.y)

def f_sort(node):
    return node.f

def get_neighbours(node, maze):
    x, y = node.x, node.y
    res = []
    if x<len(maze[0])-1 and y<len(maze)-1:
        n1 = maze[x+1][y+1]
        if not n1.is_blocked:
            n1.parent = node
            res.append(n1)
    if x>0 and y>0:
        n1 = maze[x-1][y-1]
        if not n1.is_blocked:
            n1.parent = node
            res.append(n1)
    if x>0:
        n1 = maze[x-1][y]
        if not n1.is_blocked:
            n1.parent = node
            res.append(n1)
    if y>0:
        n1 = maze[x][y-1]
        if not n1.is_blocked:
            n1.parent = node
            res.append(n1)
    if x<len(maze[0])-1 :
        n1 = maze[x+1][y]
        if not n1.is_blocked:
            n1.parent = node
            res.append(n1)
    if y<len(maze)-1:
        n1 = maze[x][y+1]
        if not n1.is_blocked:
            n1.parent = node
            res.append(n1)
    if x>0 and y<len(maze)-1:
        n1 = maze[x-1][y+1]
        if not n1.is_blocked:
            n1.parent = node
            res.append(n1)
    if x<len(maze[0])-1 and y>0:
        n1 = maze[x+1][y-1]
        if not n1.is_blocked:
            n1.parent = node
            res.append(n1)
    return res

def search(start_node, end_node, maze):
    open_list = []
    closed_list = []
    open_list.append(start_node)
    while len(open_list) >0:
        if open_list[0]==end_node:
            closed_list.append(open_list[0])
            break
        neighbours = get_neighbours(open_list[0], maze)
        for i in neighbours:
            if i not in open_list and i not in closed_list:
                i.g = i.parent.g+1
                i.h = get_dist(i, end_node)
                i.f = i.h+i.g
                open_list.append(i)
            elif i in open_list and i not in closed_list:
                g = i.parent.g+1
                h = get_dist(i, end_node)
                f = i.h+i.g
                if i.f>f:
                    i.g = i.parent.g+1
                    i.h = get_dist(i, end_node)
                    i.f = i.h+i.g
                    # open_list.append(i)
            elif i not in open_list and i in closed_list:
                g = i.parent.g+1
                h = get_dist(i, end_node)
                f = i.h+i.g
                if i.f>f:
                    i.g = i.parent.g+1 #get_dist(i.parent, i)
                    i.h = get_dist(i, end_node)
                    i.f = i.h+i.g
                    open_list.append(i)
                    closed_list.remove(i)
            print(i.x, i.y, i.f)
        closed_list.append(open_list[0])
        open_list.pop(0)
        open_list.sort(key=f_sort)
    for i in closed_list:
        print(i.x, i.y)

maze = []
for i in range(5):
    maze.append([])
    for j in range(5):
        maze[i].append(Node(x=i, y=j))
maze[0][0].h = get_dist(maze[0][0], maze[0][4])
maze[2][2].is_blocked = True
# maze[3][4].is_blocked = True
# maze[3][3].is_blocked = True
search(maze[0][0], maze[4][4], maze)
