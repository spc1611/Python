#I : Input // O : Output

apple = [["iphone 11", "iphone X", "iphone 14"], ["ipad air", "ipad pro", "ipad"], ["macbook air", "macbook pro", "macbook"]]

file = open("save.txt", 'w')

for devices in apple:
#print(devices)
    for device in devices:
        file.write(f"{device} \n")

file.close()

file = open("save.txt", 'r')

lines = file.readlines()
print("Lines : ", lines)

for line in lines: 
    print(line)

file.close