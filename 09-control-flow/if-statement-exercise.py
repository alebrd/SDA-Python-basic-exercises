selected_days = int(input('please select a number between 1 - 7 '))

if selected_days < 1:
    print('there are no negative number days!')
elif selected_days == 1:
    print('you choose monday ')
elif selected_days == 2:
    print('you choose tuesday ')
elif selected_days == 3:
    print('you choose wednesday ')
elif selected_days == 4:
    print('you choose thursday ')
elif selected_days == 5:
    print('you choose friday ')
elif selected_days == 6:
    print('you choose saturday ')
elif selected_days == 7:
    print('you choose sunday ')

elif selected_days > 7:
    print('there are only 7 days in the week! ')

