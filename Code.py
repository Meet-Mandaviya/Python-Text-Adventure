# Done by Meet Mandaviya
positive = ['Yes', 'Y', 'yes', 'y']
negative = ['No', 'N', 'no', 'n']
print()
print('''                               WELCOME! LET'S START THE ADVENTURE
      
You are standing outside of your house and you see a man running towards you and asking for urgent shelter.

Will you provide shelter to him. (Yes / No)''')

a1 = input('-->')
if a1 in positive:
    print('\nAfter 2 minutes, the Police arrived, and ask you that whether the thief is in your house or not. What will you say (Yes / No)\n')
    
    a2 = input('-->')
    if a2 in positive:
        print('\nYou are a good and honest person.')
        print('\nHe was a thief and you helped police to arrest him.')
        print('\nCongratulations! You won the game.')

    elif a2 in negative:
        print('\nYou helped that theif. Now you go to Jail.')
        print('\n************ GAME OVER ************')

    else:
        print('\nYou gave the wrong input.')
        print('\nGOODBYE!')

elif a1 in negative:
    print('\nHe attacked on you and trying to kill you with a knife, Will you knock him down or not. (Yes / No)\n')

    a3 = input('-->')
    
    if a3 in positive:
        print('\nHe was a theif and you knocked him down, then the police arrested him.')
        print('\nSo,Congratulations! You won the game.')

    elif a3 in negative:
        print('\nSorry! You are dead now. He was a theif and he killed you.')
        print('\n************ GAME OVER ************')
    
    else:
        print('\nYou gave the wrong input.')
        print('\nGOODBYE!')
        
else:
    print('\nYou gave the wrong input.')
    print('\nGOODBYE!')
