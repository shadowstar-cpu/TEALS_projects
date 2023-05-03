#nickelson, ronald
#2/23/2023
#intro to CS

side_a = int(input('what is the length of the first side of the triangle? '))
side_b = int(input('what is the length of the second side of the triangle? '))
side_c = int(input('what is the length of the third side of the triangle? '))
triangle = False
if (side_a + side_b)< side_c or (side_a + side_c)< side_b or (side_b + side_c)< side_a:
    print('This is not a triangle')
else:
    perimeter = str((side_a + side_b + side_c))
    print('the perimeter of your triangle is ' + perimeter + '. ')
    triangle = True
if triangle and (side_a != side_b and side_b != side_c and side_c != side_a):
    print('this is a scalene triangle')
elif triangle and ((side_a == side_b and side_a != side_c) or (side_b == side_c and side_b != side_a) or (side_a == side_c and side_a != side_b)):
    print('this is an isoscles triangle')
elif triangle and (side_a == side_b and side_b == side_c and side_c == side_a):
    print ('this is a equilateral triangle')