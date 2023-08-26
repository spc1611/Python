#Operators

x = 5
y = 8

print(x + y)
print(x - y)
print(x * y)
print(x / y)

# // % divmod() **

print(x // y)
print(x % y)        # % : modulars (remainder) 5 / 8 = 0 ... 5
                    # used in level up (in game)
print(divmod(x,y))  # result type : list (we will learn later)
print(x ** y)       # ** : power

x += 3      # x = x + 3 (add 3 more to the exisitng x=5)

x, y =  10 + x, 18 + x      # only possible in python (having two variables on the left side)
print(x)    # 18
print(y)    # 26