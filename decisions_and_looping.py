def x_is_int(x):
    if type(x) == int:
        print('true')
    elif type(x) != int:
        print('false')

x_is_int(1)
x_is_int(1.0)
x_is_int('1')

def if_elif_else_statement(condition_bool):
    if condition_bool:
        print('True')
    elif condition_bool:
        print('False')
    else:
        print('neither true nor false')

if_elif_else_statement(5 > 3)
if_elif_else_statement(5 < 3)
if_elif_else_statement('5')


#the simplest way to start writing loops in python
#is the while loop as demostrated below.

#while contdition:
    #indented_statments

def while_loop(n):
    x = 1
    while x <= n:
        print(x, end=' ')
        x += 1

while_loop(20)
