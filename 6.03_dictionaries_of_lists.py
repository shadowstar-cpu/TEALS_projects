days_of_week = {'monday' : [],
                'tuesday' : [],
                'wednesday' : [],
                'thursday' : [],
                'friday' : [],
                'saturday' : [],
                'sunday' : []
                }
player_quit = False
while player_quit == False:
    action = input('what action would you like to take?\n').lower()
    if action == 'add':
        day = input('what day would you like to add a task to?\n').lower()
        if day in days_of_week:
            task = input('what task would you like to add\n').lower()
            if task not in days_of_week[day]:
                days_of_week[day].append(task)
            else:
                print('that task is already in your list.')
        else:
            print('That is not a day please try again.')
    elif action == 'get':
        day = input('what day would you like to get the list for?\n').lower()
        if day in days_of_week:
            print(days_of_week[day])
        else:
            print('That is not a day please try again.')
    elif action == 'quit':
        quit()
    else:
        print('that is not a valid action, try again.')
#ily