#--- Day 4: Passport Processing ---
needed_fields=('byr','iyr','eyr','hgt','hcl','ecl','pid')
valid_hex_digits='0123456789abcdef'
valid_eye_colors=('amb','blu','brn','gry','grn','hzl','oth')
passports=[]
tmp_passport=[]
def validate_field(field_type:str,field_value:str)->bool:
    validators={
        'byr':lambda v:len(v)==4 and int(v) in range(1920,2003),
        'iyr':lambda v:len(v)==4 and int(v) in range(2010,2021),
        'eyr':lambda v:len(v)==4 and int(v) in range(2020,2031),
        'hgt':lambda v:('cm' in v and int(v[:-2]) in range(150,194)) or ('in' in v and int(v[:-2]) in range(59,77)),
        'hcl':lambda v:v[0]=='#' and len(v[1:])==6 and all(c in valid_hex_digits for c in v[1:]),
        'ecl':lambda v:v in valid_eye_colors,
        'pid':lambda v:len(v)==9,
        'cid':lambda v:True
    }
    return validators[field_type](field_value)

with open('day4_passports.txt','r') as  f:
    for line in f.readlines():
        if not line.strip():
            passports.append(' '.join(tmp_passport))
            tmp_passport=[]
        else: tmp_passport.append(line.strip())
if tmp_passport:passports.append(' '.join(tmp_passport))

#part 1
valid_passports=[]
for passport in passports:
    field_names=[f.split(':')[0] for f in passport.split()]
    if all(f in field_names for f in needed_fields):
        valid_passports.append(passport)

print(len(valid_passports))

#part 2
valid_passports=[]
for passport in passports:
    fields=passport.split()
    field_names=[f.split(':')[0] for f in passport.split()]
    if all(f in field_names for f in needed_fields) and all(validate_field(t,v) for t,v in (field.split(':') for field in fields)):
        valid_passports.append(passport)
  
print(len(valid_passports))