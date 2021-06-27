import numpy as np

file=open('./input.txt')
lines=file.readlines();
passes=[(line.split()) for line in lines]



# part 1
number_of_valid_passwords=0

for passw in passes:
    policy=   np.array(passw[0].split('-')).astype('int') 
    char_to_check= passw[1][0]
    password= passw[2]

    count=0 
    for char in password:
        if char_to_check == char:
            count+=1
    
    if count >= policy[0] and count<=policy[1]:
        number_of_valid_passwords+=1

print(number_of_valid_passwords)



# part 2
number_of_valid_passwords=0

for passw in passes:
    policy=   np.array(passw[0].split('-')).astype('int') 
    char_to_check= passw[1][0]
    password= passw[2]
    count=0
    for i in range(2):
        count+=int(password[policy[i]-1]==char_to_check)      # if this is 2, both are same chars. if this is 0, both are differsnt. if this is exactly one, exactly one of them is same as char we need.
    

    if count==1:
         number_of_valid_passwords+=1


print(number_of_valid_passwords)