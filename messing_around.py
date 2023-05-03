import random
def double(number):
    print(number + number)
double(3)
def half(number):
    print(number * 0.5)
half(4)
def add(number, number2):
    print(number + number2)
add (5, 6)
def subtract(number, number2):
    print(number - number2)
subtract(18, 5)
#x+1=5
def Equation(number, equals):
    if number == equals:
        print("x=0")
    else:
        print('x=' + str(equals - number))
Equation(1,5)
random_list = []
def pick_random(number_of_digits):
    i = 0
    while i < number_of_digits:
        random_list.append(random.randint(0, 9))
        i = i+1
    print(random_list)
pick_random(4)
def Name_Date(name, date):
    print("made by, " + name + ", on, 1/31/23, it was last edited on " + date)
Name_Date("Ronald Nickelson", "3/11/23")
