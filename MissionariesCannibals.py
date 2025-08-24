from collections import deque
def is_valid(state):
    ml,cl,b=state
    mr=3-ml
    cr=3-cl
    # if b not in(0,1):
    #     return False
    if ml<0 or cl<0 or mr<0 or cr<0:
        return False
    if (ml>0 and cl>ml) or (mr>0 and cr>mr):
        return False
    return True
def get_neighbours(state):
    m,c,b=state
    moves=[]
    d=-1 if b=="left" else "right"
    for m_move,c_move in [(1,0),(2,0),(0,1),(0,2),(1,1)]:
        new_m=m+(d*m_move)
        new_c=c+(d*c_move)
        new_b="right"
        if new_b==" left":
            t="left"
        else:
            t="right"
        new_state=(new_m,new_c,t)
        if(is_valid(new_state)):
            moves.append(new_state)
    return moves
def slove():
    start=(3,3,"left")
    goal=(0,0,"right")
    queue=deque()
    queue.append((start,[start]))
    visited=set()
    visited.add(start)
    while queue:
        curstate,path=queue.popleft()
        if curstate==goal:
            return path
        for next_state in get_neighbours(curstate):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state,path+[next_state]))
    return None
solution=slove()
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found!!!!!!")



        
       