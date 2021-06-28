import numpy as np

file=open('./input.txt')
contents=file.read()


# Part1
passports=[]
set_of_all_keys={'byr','iyr','eyr','hgt','hcl','ecl','pid','cid'}
set_of_reqd_keys={'byr','iyr','eyr','hgt','hcl','ecl','pid'}

number_of_valid_pass=0

for entry in contents.split('\n\n'):

    passport={}
    for item in entry.replace('/n',' ').split():
        key,value=item.split(':')
        passport[key]=value

    passports.append(passport)
    if set(passport.keys()) in [set_of_all_keys,set_of_reqd_keys]:
        number_of_valid_pass+=1

print(number_of_valid_pass)


#Part2
passports=[]
set_of_all_keys={'byr','iyr','eyr','hgt','hcl','ecl','pid','cid'}

number_of_valid_pass=0

for entry in contents.split('\n\n'):

    passport={}
    for item in entry.replace('/n',' ').split():
        key,value=item.split(':')
        passport[key]=value

    passports.append(passport)
    if set(passport.keys()) not in [set_of_all_keys,set_of_reqd_keys]:
        continue

    if not (1920<=int(passport['byr'])<=2002):
        continue
    
    if not (2010<=int(passport['iyr'])<=2020):
        continue
    
    if not (2020<=int(passport['eyr'])<=2030):
        continue
   
    if passport['hgt'][-2:] == 'cm':
        if not (150<=int(passport['hgt'][:-2])<=193): 
            continue
    elif passport['hgt'][-2:] == 'in':
         if not (59<=int(passport['hgt'][:-2])<=76):
            continue
    else:
        continue

    if passport['hcl'][0]=='#':       
        for ch in passport['hcl'][1:]:         
            if ch not in ([str(a) for a in list(range(10))]+list('abcdef')):
                continue
    else:
        continue
        
    if passport['ecl'] not in 'amb blu brn gry grn hzl oth'.split():
        continue
    
    if len(passport['pid'])!=9:
        continue
    
    number_of_valid_pass+=1  # this runs only if all ifs above are false.


print(number_of_valid_pass)
