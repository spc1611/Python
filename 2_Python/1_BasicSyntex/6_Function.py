def CubeVolumn(width, height, length):
    volumn = width * height * length
    return volumn

w, h, l = float(input("Input width : ")), float(input("Input height : ")), float(input("Input length : "))

result = CubeVolumn(w, h, l)
print(result)