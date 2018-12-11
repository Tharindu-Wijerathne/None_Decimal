
banner = '''


_____   __ __________ ____   ___ ________    _________ _________ ________ __________ ____       ____    ____    ___
|   \  |  ||  _____  ||   \  |  ||  _____|   |   __  \ |   _____||  _____||___   ___||   \     /   |   /    \   |  |
|    \ |  ||  |   |  ||    \ |  || |_____    |  |  |  ||  |_____ | |          | |    |    \   /    |  /  __  \  |  |
|  |\ \|  ||  |___|  ||  |\ \|  || |_____    |  |__|  ||  |_____ | |_____ ____| |___ |  |\ \_/ /|  | /  |__|  \ |  |___
|__| \____||_________||__| \____||_______|   |_______/ |________||_______||_________||__| \___/ |__|/__/    \__\|______|

                                                                                 [Coded By AGENT-X.Tharindu_Wijerathne]


Enter 'B' to Convert Decimal in to Binary
Enter 'O' to Convert Decimal in to Octadecimal
Enter 'H' to Convert Decimal in to Hexadecimal
'''
print(banner)


def binary(F):
    if F > 1:
        binary(F//2)
    print(F % 2, end="")


def octa(U):
    if U > 1:
        octa(U//8)
        print(U % 8, end="")


def hexa(K):
    ten = 'A'
    eleven = 'B'
    twele = 'C'
    thirteen = 'D'
    fourteen = 'E'
    fifteen = 'F'
    if K > 1:
        hexa(K//16)
        bal = K % 16
        if bal == 10:
            print(ten, end="")
        elif bal == 11:
            print(eleven, end="")
        elif bal == 12:
            print(twele, end="")
        elif bal == 13:
            print(thirteen, end="")
        elif bal == 14:
            print(fourteen, end="")
        elif bal == 15:
            print(fifteen, end="")
        else:
            print(bal, end="")


try:
    selection = input("NONE DECIMAL - ").upper()
    if selection == 'B':
        binary(int(input("Enter Your Number - ")))
    elif selection == 'O':
        octa(int(input("Enter Your Number - ")))
    elif selection == 'H':
        hexa(int(input("Enter Your Number - ")))
    else:
        print("Invalid Selection")
except(KeyboardInterrupt):
    print("Programe Interrupted")
