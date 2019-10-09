a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,5,6,10,34,58,2938,129]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,129,34,10,2938,999,129]
c = []

for num in a:
    if num in b:
        if num in c:
            pass # "pass" le dice a Python que no haga nada
        else:
            c.append(num)
print(c)
