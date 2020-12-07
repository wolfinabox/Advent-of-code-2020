#--- Day 5: Binary Boarding ---

def binary_partition(parts:str,top:int):
    bottom=0
    for part in parts:
        half=(top-bottom)//2
        #top half
        if int(part):
            bottom+=half
        #bottom half
        else:
            top-=half
            
    return bottom

# 128 rows (0-127)
# 8 columns (0-7)
def find_seat_num(bin_partition:str)->int:
    row_bin,col_bin=bin_partition[:7],bin_partition[7:]
    row_bin_exp=''.join([('1' if n=='B' else '0') for n in row_bin])
    col_bin_exp=''.join([('1' if n=='R' else '0') for n in col_bin])
    row,col=binary_partition(row_bin_exp,128),binary_partition(col_bin_exp,8)
    return row,col

# seats=['FBFBBFFRLR','BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']
# for s in seats:
#     row,col=find_seat_num(s)
#     print(f'row: {row}, col: {col}, id: {row*8+col}')

passes=[]
with open('./day5_boardingpasses.txt','r') as f:
    passes=[l.strip() for l in f.readlines()]

seats=[find_seat_num(p) for p in passes]
seat_ids=[i[0]*8+i[1] for i in seats]

#Part 1
max_seat_id=max(seat_ids)
print(max_seat_id)


#Part 2
seats_not_taken=list(set(range(0,max_seat_id+1)).difference(set(seat_ids)))
my_seat=[s for s in seats_not_taken if s-1 not in seats_not_taken and s+1 not in seats_not_taken][0]
print(my_seat)