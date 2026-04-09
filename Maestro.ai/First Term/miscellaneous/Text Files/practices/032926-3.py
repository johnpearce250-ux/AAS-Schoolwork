
actions=[]
number=0

while True:
    action=input('Enter a task or undo to undo a task (up to 3)')
    if action.lower() != 'undo':
        actions.append(action)
    else:
        try:
            number=int(input('How many times to undo?'))
        except ValueError:
            print('Value must be an integer')
            continue
        if number > 3:
            print('Can only updo up to 3 actions')
        else: 
            for _ in range(number):
                if actions:
                    actions.pop()
                else:
                    break
            print(actions)
            break

    print(actions)