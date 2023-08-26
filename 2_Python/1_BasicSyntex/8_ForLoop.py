for i in range(1, 11): 
    print("i times : ", i)

apple = [["iphone 11", "iphone X", "iphone 14"], ["ipad air", "ipad pro", "ipad"], ["macbook air", "macbook pro", "macbook"]]

for devices in apple:
    #print(devices)
    for device in devices:
        print(device, end= ", ")
    print("")               # enter between values

position = [[13, 5],  [32, 2], [22, 8]]             # on x, y axis

position = [[x+3, y+2] for x, y in position]        # Command + D

print(position)

# for x, y in position: 
#       x += 3
#       y += 2
#       position.append([x,y])