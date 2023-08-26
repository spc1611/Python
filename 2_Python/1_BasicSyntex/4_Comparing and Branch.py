# x = int(input("first num: "))    # String --> int
# y = int(input("second num: "))   # String --> int

# print(x + y)

#########################

# Comparison: result (True/False)
# == != > < >= <=
# and or not

a = 3
b = 5
a == b
print(a == b and a > b or a >= 3)

# False and False or True         # 'and' has higher priority than 'or'
# False or True 
# True

###################

age = 20

age = float(input("Your age : "))   #Can input decimal for float, can input only integer for int.
result = ""

if age > 20: 
    result = "beer"
elif 20 >= age and age > 1 :
    result = "juice"
else:
    result = 'milk'     # both " and ' works.

print(result)           #Should not be on the TAB.