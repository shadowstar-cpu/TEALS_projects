my_num = 1
print(my_num)

def add_2():
    global my_num
    my_num = my_num + 2

def multiply_num(multiply_by):
    global my_num
    my_num = my_num * multiply_by

def add_2_and_multiply(multiply_by_num):
    global my_num
    add_2()
    multiply_num(multiply_by_num)

add_2_and_multiply(3)
print(my_num)