select = 0      #Can be any number except 6. Just need to define 'select' as something for the computer.

while (select != 6) :


    menu = '''
    [1] Cola
    [2] Diet Coke
    [3] 7up
    [4] Brisk
    [5] Sprite
    [6] exit
    '''     # ''' : string 있는 그대로 print (like an image)

    print(menu)

    select = float(input("Select Drink : "))

    if select == 1 : 
        drink = "Coke"
    elif select == 2 :
        drink = 'Diet Coke'
    elif select == 3 :
        drink = '7up'
    elif select == 4 :
        drink = 'Brisk'
    elif select == 5 :
        drink = 'Sprite'
    elif select == 6 :
        break
    else :
        drink = "Nothing"

    print(f'Your Choice : {drink}')