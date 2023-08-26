# Tuple
#fruits = ('banana', 'strawberry', 'apple')
#fruits[2] = 'watermelon'
#print(fruits[2])

# List
fruits_list = ['banana', 'strawberry', 'apple']
fruits_list[2] = 'watermelon'
print(fruits_list)

# List Function 
fruits_list.append('orange')            # append : means to add
print(f'appended : {fruits_list}')

fruits_list.remove('banana')            # remove : delete
print(f'removed : {fruits_list}')

print(f'pop : {fruits_list.pop()}')     # pop : taking last element and remove 
print(f'poped : {fruits_list}')

apple = [["iphone 11", "iphone X", "iphone 14"], ["ipad air", "ipad pro", "ipad"], ["macbook air", "macbook pro", "macbook"]]

print(apple[1][1])      #Command + Option
print(apple[2][0])
print(apple[0][2])
print(apple[2][2])
print(apple[1][0])

# Dictionary    {}  dict_name =  { key1 : value1, key2 : value2, ... }

price = {"HP": 949.99, 
         "ASUS" : 499.97,
         "MACBOOK" : 599
         }

print(price["HP"])

# zip - separates

x_axis = [(35, 43), (12, 35), (89, 22), (90, 54)]
left, right = zip(*(x_axis))
print(left)
print(right)