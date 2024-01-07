
a = [[1,2,3],[4,5,6],[7,8,9]]

player = 1
symbol = 'X'
total_rounds = 0

# prepared separate function for showing matrix
def show_mat():5
    i = 0
    while i<=2:
        j = 0
        while j<=2:
            print(a[i][j], end="  |  ")
            j = j + 1
        print()
        i = i + 1

# main logic starts
while True:
    # showing matrix
    show_mat()

    print("Play your turn, Player-", player)
    print("Symbol :", symbol)
    box = int(input("Select box number : "))

    # filling that box number with player's symbol
    if box==1:
        if a[0][0] == 'X' or a[0][0] == '0':
            print("Box already filled.. Please repeat your turn..!")
            continue
        else:
            a[0][0] = symbol
    elif box==2:
        if a[0][1] == 'X' or a[0][1] == '0':
            print("Box already filled.. Please repeat your turn..!")
            continue
        else:
            a[0][1] = symbol
    elif box==3:
        if a[0][2] == 'X' or a[0][2] == '0':
            print("Box already filled.. Please repeat your turn..!")
            continue
        else:
            a[0][2] = symbol
    elif box==4:
        if a[1][0] == 'X' or a[1][0] == '0':
            print("Box already filled.. Please repeat your turn..!")
            continue
        else:
            a[1][0] = symbol
    elif box==5:
        if a[1][1] == 'X' or a[1][1] == '0':
            print("Box already filled.. Please repeat your turn..!")
            continue
        else:
            a[1][1] = symbol
    elif box==6:
        if a[1][2] == 'X' or a[1][2] == '0':
            print("Box already filled.. Please repeat your turn..!")
            continue
        else:
            a[1][2] = symbol
    elif box==7:
        if a[2][0] == 'X' or a[2][0] == '0':
            print("Box already filled.. Please repeat your turn..!")
            continue
        else:
            a[2][0] = symbol
    elif box==8:
        if a[2][1] == 'X' or a[2][1] == '0':
            print("Box already filled.. Please repeat your turn..!")
            continue
        else:
            a[2][1] = symbol
    elif box==9:
        if a[2][2] == 'X' or a[2][2] == '0':
            print("Box already filled.. Please repeat your turn..!")
            continue
        else:
            a[2][2] = symbol

    # Checking winner, if found, in all 8 locations
    if a[0][0] == a[0][1] and a[0][1] == a[0][2]:
        show_mat()
        print("Player", player, "Wins...!")
        break
    elif a[1][0] == a[1][1] and a[1][1] == a[1][2]:
        show_mat()
        print("Player", player, "Wins...!")
        break
    elif a[2][0] == a[2][1] and a[2][1] == a[2][2]:
        show_mat()
        print("Player", player, "Wins...!")
        break
    elif a[0][0] == a[1][0] and a[1][0] == a[2][0]:
        show_mat()
        print("Player", player, "Wins...!")
        break
    elif a[0][1] == a[1][1] and a[1][1] == a[2][1]:
        show_mat()
        print("Player", player, "Wins...!")
        break
    elif a[0][2] == a[1][2] and a[1][2] == a[2][2]:
        show_mat()
        print("Player", player, "Wins...!")
        break
    elif a[0][0] == a[1][1] and a[1][1] == a[2][2]:
        show_mat()
        print("Player", player, "Wins...!")
        break
    elif a[0][2] == a[1][1] and a[1][1] == a[2][0]:
        show_mat()
        print("Player", player, "Wins...!")
        break

    if player==1:
        player = 2
        symbol = '0'
    elif player==2:
        player = 1
        symbol = 'X'

    total_rounds = total_rounds + 1
    if total_rounds == 9:
        print("Match Draw...!")
        break