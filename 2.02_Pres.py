age = int(input('how old are you in years?'))
length_of_residency = int(input('how long have you been a resident of the united states?'))
natural_born_citizen = input('are you a natural born citizen?')
can_be_pres = age >= 35 and length_of_residency >= 14 and natural_born_citizen == 'yes'
print (can_be_pres)
height = int(input('how tall are you in inches?'))
quarters = int(input('how many quarters do you have?'))
frequent_rider_pass = input('do you have a frequent rider pass?')
can_ride= (height >= 50 or age>=18) and (quarters>=4 or (frequent_rider_pass == 'yes' and quarters >=2))
print(can_ride)