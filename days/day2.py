#--- Day 2: Password Philosophy ---

lines=[]
with open('day2_passwords.txt','r') as  f:
    lines=f.readlines()

#part 1
# valid_passwords=[]
# for line in lines:
#     policy,password=(s.strip() for s in line.split(':'))
#     policy_amts,policy_letter=policy.split()
#     policy_min,policy_max=policy_amts.split('-')
#     if password.count(policy_letter) in range(int(policy_min),int(policy_max)+1):
#         valid_passwords.append(password)

# print(len(valid_passwords))

#part 2
valid_passwords=[]
for line in lines:
    policy,password=(s.strip() for s in line.split(':'))
    policy_amts,policy_letter=policy.split()
    
    counts=[password[int(n)-1]==policy_letter for n in policy_amts.split('-')]
    if counts[0]!=counts[1]:
        valid_passwords.append(password)

print(len(valid_passwords))
    