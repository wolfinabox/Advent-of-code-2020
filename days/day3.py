#--- Day 3: Toboggan Trajectory ---
import math
def count_tree_encounters(rows:list,slope:tuple)->int:
    curr_pos=[0,0]
    trees_hit=0

    while curr_pos[1]<len(rows):
        if rows[curr_pos[1]][curr_pos[0]]=='#':
            trees_hit+=1
        curr_pos[0]+=slope[0]
        curr_pos[1]+=slope[1]
        if curr_pos[0]>=len(rows[0]):
            curr_pos[0]=curr_pos[0]-len(rows[0])
    return trees_hit

rows=[]
with open('day3_trees.txt','r') as  f:
     rows=[l.strip() for l in f.readlines()]

slopes= ((1,1),(3,1),(5,1),(7,1),(1,2))
total=math.prod(count_tree_encounters(rows,s) for s in slopes)
print(total)