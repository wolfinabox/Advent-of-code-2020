#--- Day 6: Custom Customs ---

def yes_per_group(responses):
    groups=responses.split('\n\n')
    group_counts=[]
    for group in groups:
        answers=set(group.replace('\n',''))
        group_counts.append(len(answers))
    return group_counts

def all_yes_per_group(responses):
    groups=responses.split('\n\n')
    group_counts=[]
    for group in groups:
        people=group.split()
        all_yes=people[0]
        for person in people:
            all_yes=list(set(all_yes).intersection(person))
        group_counts.append(len(all_yes))
    return group_counts
# test="""abc

# a
# b
# c

# ab
# ac

# a
# a
# a
# a

# b"""
# group_yesses=yes_per_group(test)
# print(group_yesses)

forms=''
with open('./day6_forms.txt','r') as f:
    forms=f.read()

#Part 1
group_yesses=yes_per_group(forms)
print(sum(group_yesses))

#Part 2
group_all_yesses=all_yes_per_group(forms)
print(sum(group_all_yesses))
