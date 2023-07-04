def a():
    print('You ordered sinigang')
    while True:
        confirmation = input('Confirm your order (Enter Yes/No): ')
        if confirmation.lower() == 'yes':
            print('Order confirmed.')
            break
        elif confirmation.lower() == 'no':
            print('Order canceled.')
            return "cancel"
        else:
            print('Invalid input. Please enter Yes or No.')

def b():
    print('You ordered sinigang')
    while True:
        confirmation = input('Confirm your order (Enter Yes/No): ')
        if confirmation.lower() == 'yes':
            print('Order confirmed.')
            break
        elif confirmation.lower() == 'no':
            print('Order canceled.')
            return "cancel"
        else:
            print('Invalid input. Please enter Yes or No.')

def c():
    print('You ordered sinigang')
    while True:
        confirmation = input('Confirm your order (Enter Yes/No): ')
        if confirmation.lower() == 'yes':
            print('Order confirmed.')
            break
        elif confirmation.lower() == 'no':
            print('Order canceled.')
            return "cancel"
        else:
            print('Invalid input. Please enter Yes or No.')

choice = ""
while choice != "a" and choice != "b" and choice != "c":
    choice = input('Select a menu (Only Letter): A. Sinigang B. Adobo C.Tocino\n').lower()
    if choice != "a" and choice != "b" and choice != "c":
        print("Invalid choice.")

if choice == "a":
    result = a()
elif choice == "b":
    result = b()
elif choice == "c":
    result = c()
else:
    result = "cancel"

if result == "cancel":
    
    choice = ""
while choice != "a" and choice != "b" and choice != "c":
    choice = input('Select a menu (Only Letter): A. Sinigang B. Adobo C.Tocino\n').lower()
    if choice != "a" and choice != "b" and choice != "c":
        print("Invalid choice.")

    if choice == "a":
     result = a()
    elif choice == "b":
     result = b()
    elif choice == "c":
     result = c()
    else:
     result = "cancel"
    
else:
    print("Thank you for ordering")
