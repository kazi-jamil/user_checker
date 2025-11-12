usernames = ['noman','milon','korim']
print('username checker')
print('='*20)
print('you have 3 attempts left to try')
print()
attemts = 0
max_attemts = 3
while attemts < max_attemts:
    user_input = input(f'attempt {attemts+1}/{max_attemts} - enter username:')
    if user_input in usernames:
        print('welcome!')
        break
    else:
        attemts += 1
        if attemts < max_attemts:
            print('sorry, try again!')
            print()
        else:
            print('sorry,out of tries')