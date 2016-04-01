
def simple_if_condition(n):
    i = n
    if i == 0:
        i += 1
    print(i)

def if_else_condition(n):
    i = n
    if i == 0:
        i += 1
    elif i == 1:
        i += 2
    print(i)

def if_else_condition2(n):
    i = n
    if i > 0:
        for j in range(1, n):
            print(j)
    elif i < 0:
        i += 2
    print(i)

def test_function(n):
    for j in range(1, n):
        print(j)

def if_else_condition3(n):
    i = n
    if test_function(n) > 0:
        for j in range(1, n):
            print(j)
    elif i < 0:
        i += 2
    print(i)





# simple_if_condition(0)
# if_else_condition(1)
# if_else_condition2(5)
if_else_condition(5)
