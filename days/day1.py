#--- Day 1: Report Repair ---
nums=[]
with open('day1_expensereport.txt','r') as  f:
    for line in f.readlines():
        if line:
            nums.append(int(line))

#part 1
result=None
for a in nums:
    for b in nums:
        if a+b==2020:
            result=a*b
            break
    if result:break

print(result)

#part 2
result=None
for a in nums:
    for b in nums:
        for c in nums:
            if a+b+c==2020:
                result=a*b*c
                break
    if result:break

print(result)