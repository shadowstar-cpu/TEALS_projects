#Nickelson, Ronald
#2/15/23
#Intro to CS

number = input('enter a number to half')
type = input('would you like a float or a integer format?')
if type == 'float':
    print(float(number) / 2)
if type == 'integer':
    print(int(number) // 2)