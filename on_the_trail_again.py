#Nickelson, Ronald
#3/23/23
#Intro to CS
"""Simulation of traveling out west in the 1800's"""

import random

name = input('\nWhat is your name traveler?\n')

welcome_text = """
Welcome to the Oregon Trail! The year is 1850 and Americans are
headed out West to populate the frontier. Your goal is to travel
by wagon train from Independence, Missouri to Oregon (2000 miles). 
You start on March 1st, and your goal is to reach Oregon by December 31st. 
The trail is arduous. Each day costs you food and health. You
can hunt and rest, but you have to get there before winter!"""

help_text = """
Each turn you can take one of 3 actions:

  travel - moves you randomly between 30-60 miles and takes
           3-7 days (random).
  rest   - increases health 1 level (up to 5 maximum) and takes
           2-5 days (random).
  hunt   - adds 100 lbs of food and takes 2-5 days (random).

When prompted for an action, you can also enter one of these
commands without using up your turn:

  status - lists food, health, distance traveled, and day.
  help   - lists all the commands.
  quit   - will end the game.
  
You can also use these shortcuts for commands:

  't', 'r', 'h', 's', '?', 'q'
  
"""

good_luck_text = "Good luck " + name + ", and see you in Oregon!"

win_text = 'Congratulations you made it! ' + name + ' Now you can enjoy the new frontier out west. '

lose_text = 'You died on the trail, RIP ' + name

choice_text = '\nNow choose what to do, ' + name + ' if you need more information enter ? to see the help page.\n'

quit_text = 'Goodbye and good luck ' + name + '! '

sick_text = 'oh no! ' + name + ' got sick.'
# Constants -- parameters that define the rules of the game, which don't change.
MIN_MILES_PER_TRAVEL = 30
MAX_MILES_PER_TRAVEL = 60
MIN_DAYS_PER_TRAVEL = 3
MAX_DAYS_PER_TRAVEL = 7
FOOD_EATEN_PER_DAY_DURING_TRAVEL = 5

MIN_DAYS_PER_REST = 2
MAX_DAYS_PER_REST = 5
HEALTH_CHANGE_PER_REST = 1
MAX_HEALTH = 5
FOOD_EATEN_PER_DAY_DURING_REST = 3

FOOD_PER_HUNT = 100
MIN_DAYS_PER_HUNT = 2
MAX_DAYS_PER_HUNT = 5
FOOD_EATEN_PER_DAY_DURING_HUNT = 8

MAX_SICK_DAYS_PER_MONTH = 2
MILES_BETWEEN_MO_AND_OR = 2000

# Days in each month including January of next year. 0 is not used.
DAYS_IN_MONTH = (None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31)
# Month number to string including January of next year. 0 is not used.
NAME_OF_MONTH = (
    None,
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
    "January",
)

HEALTH_LEVELS = ("dead", "almost dead", "poor", "good", "great", "perfect")

EVENTS = ('River crossing', 'Attacked by hostile parties', 'Snake bite', 'Broken wheel', 'Gored by a boar', 'Mauled by a bear')

def start_in_mo():
    """Initialize all global variables to be start of game."""
    global miles_traveled, food_remaining, health_level, month, event_this_month, hunted
    global day, sicknesses_suffered_this_month, player_quits, name, traveled, rested
    miles_traveled = 0
    food_remaining = 500
    health_level = 5
    month = 3
    day = 1
    sicknesses_suffered_this_month = 0
    event_this_month = False
    player_quits = False
    traveled = False
    hunted = False
    rested = False
    print(welcome_text)
    print(good_luck_text)

def date_as_string():
    """return a string like "December 24"."""
    return NAME_OF_MONTH[month] + " " + str(day)


def maybe_rollover_month():
    """If we are into the next month, change the date. Reset sickness counter."""
    global month, day, sicknesses_suffered_this_month, event_this_month
    if DAYS_IN_MONTH[month] < day:
        day -= DAYS_IN_MONTH[month]
        month += 1
        sicknesses_suffered_this_month = 0
        event_this_month = False
        if month == 12:
            print('You dont have much time left ' + name + '. Hurry before winter comes!')


def no_more_time():
    """Returns true when time has run out."""
    return month > 12  # Is it January of next year?


def sickness_occurs():
    global day, sicknesses_suffered_this_month, month
    """Returns True if you get sick today."""
    # days remaining includes today
    days_remaining_in_month = DAYS_IN_MONTH[month] - day + 1
    sick_days_needed = MAX_SICK_DAYS_PER_MONTH - sicknesses_suffered_this_month
    # gives sick days needed out of days remaining in month as a chance
    # of being sick. When sick days needed is zero there is no chance
    # of getting sick again.
    return random.randint(1, days_remaining_in_month) <= sick_days_needed
def travel():
    global day, month, miles_traveled, health_level, food_remaining, health_level, sicknesses_suffered_this_month
    traveling = random.randint(MIN_MILES_PER_TRAVEL, MAX_MILES_PER_TRAVEL)
    days_traveled = random.randint(MIN_DAYS_PER_TRAVEL, MAX_DAYS_PER_TRAVEL)
    miles_traveled += traveling
    day += days_traveled
    food_eaten = 0
    maybe_rollover_month()
    i = 0
    traveled = True
    if sickness_occurs() and health_level > 0:
        health_level -= 1
        sicknesses_suffered_this_month += 1
        print(sick_text)
    while i < days_traveled:
        if food_remaining > 0:
            food_remaining -= FOOD_EATEN_PER_DAY_DURING_TRAVEL
            food_eaten += FOOD_EATEN_PER_DAY_DURING_TRAVEL
        elif health_level > 0:
                health_level -= 1
        i += 1
    print('You traveled ' + str(traveling) + ' miles along the trail in ' + str(days_traveled) + ' days and ate ' + str(food_eaten) + ' pounds of food.')
    maybe_warnings()
    	
def rest():
    global day, month, health_level, food_remaining, sicknesses_suffered_this_month, rested
    days_rested = random.randint(MIN_DAYS_PER_REST, MAX_DAYS_PER_REST)
    day += days_rested
    food_eaten = 0
    maybe_rollover_month()
    #<3
    rested = True
    if health_level < 5:
        health_level += HEALTH_CHANGE_PER_REST
    i = 0        
    if sickness_occurs() and health_level > 0:
        health_level -= 1
        sicknesses_suffered_this_month += 1
        print(sick_text)
    while i < days_rested:
        if food_remaining > 0:
            food_remaining -= FOOD_EATEN_PER_DAY_DURING_REST
            food_eaten += FOOD_EATEN_PER_DAY_DURING_REST
        elif health_level > 0:
            health_level =-1
        i += 1
    print('You rested for ' + str(days_rested) + ' days and ate ' + str(food_eaten) + ' pounds of food.')
    maybe_warnings()

def hunt():
    global day, food_remaining, health_level, sicknesses_suffered_this_month
    days_hunted = random.randint(MIN_DAYS_PER_HUNT, MAX_DAYS_PER_HUNT)
    day += days_hunted
    food_remaining += FOOD_PER_HUNT
    i = 0
    food_eaten = 0
    maybe_rollover_month()
    hunted = True
    if sickness_occurs() and health_level > 0:
        health_level -= 1
        sicknesses_suffered_this_month += 1
        print(sick_text)
    while i < days_hunted:
        if food_remaining > 0:
            food_remaining -= FOOD_EATEN_PER_DAY_DURING_HUNT
            food_eaten += FOOD_EATEN_PER_DAY_DURING_HUNT
        elif health_level > 0:
            health_level -= 1
        i += 1
    print('You hunted for ' + str(days_hunted) + ' days and got 100 pounds of food, but you ate ' + str(food_eaten) + ' leaving you with ' + str(100 - food_eaten) + ' more pounds of food.')
    maybe_warnings()



def miles_remaining():
    """Return the number of miles left to go."""
    return max(0, MILES_BETWEEN_MO_AND_OR - miles_traveled)



def print_status():
    print(
        "Today is "
        + date_as_string()
        + ". You have "
        + str(food_remaining)
        + " pounds of food. Your health is "
        + HEALTH_LEVELS[health_level]
        + ".\nYou must travel "
        + str(miles_remaining())
        + " more miles."
    )

def print_help():
    print(help_text)

def maybe_win():
    global win_text, miles_remaining
    '''
    check for win
    if true
    print win text
    ask for restart
    '''
    if miles_remaining() == 0:
        print(win_text)
        quit()

def maybe_lose():
    global health_level, lose_text
    '''
    check for lose
    if true
    print lose text
    ask for restart
    '''
    if no_more_time():
        print(lose_text + '. You froze to death during the winter.')
        restart = input('would you like to try the trail again?').lower()
        if restart == 'no':
            print('Goodbye ' + name + ', good luck on your travels.')
    elif health_level <= 0 and food_remaining <= 0:
        print(lose_text + '. You ran out of food and died of starvation.')
        restart = input('would you like to try the trail again?').lower()
        if restart == 'no':
            print('Goodbye ' + name + ', good luck on your travels.')
    elif health_level <= 0 and event_today == True:
        print(lose_text + '. You died from the event.')
        restart = input('would you like to try the trail again?').lower()
        if restart == 'no':
            print('Goodbye ' + name + ', good luck on your travels.')
    elif health_level <= 0:
        print(lose_text + '. You died of disease.')
        restart = input('would you like to try the trail again?').lower()
        if restart == 'no':
            print('Goodbye ' + name + ', good luck on your travels.')
        elif restart == 'yes':
            print()

def maybe_warnings():
    if food_remaining <= 50 and food_remaining > 0 and health_level > 0:
        print('Youre running low on food ' + name + '. You might want to go hunting.')
    if health_level <= 2 and health_level > 0:
        print('Youre health is low ' + name + '. You might want to rest.')
    if food_remaining == 0 and health_level > 0:
        print('You are out of food, hunt quick!')


def event_occurs():
    global event_this_month, month, day, event_today
    true_false = (True, False)
    if event_this_month == False:
        event_today = true_false[random.randint(0,1)]
        if event_today == True:
            event()

def event():
    global event_this_month, day, month, health_level, food_remaining, health_level
    event = EVENTS[random.randint(0, 3)]
    if event == 'River crossing' and traveled == True:
        event_this_month = True
        health_lost = random.randint(0,1)
        days_taken = random.randint(3, 10)
        i = 0
        food_eaten_per_day_during_this_event = random.randint(7, 10)
        food_eaten = 0
        day += days_taken
        health_level -= health_lost
        while i < days_taken:
            if food_remaining > 0:
                food_remaining -= food_eaten_per_day_during_this_event
                food_eaten += food_eaten_per_day_during_this_event
            elif health_level > 0:
                health_level -= 1
            i += 1
        if health_lost == 0:
            print('You ran into a small river that you had to cross to continue the trail. You made it across safely. It took ' + str(days_taken) + ' days and you ate ' + str(food_eaten) + ' pounds of food.')
        else:
            print('You ran into a small river that you had to cross to continue the trail. You got injured while crossing. It took ' + str(days_taken) + ' days and you ate ' + str(food_eaten) + ' pounds of food.')
    if event == 'Attacked by hostile parties':
        event_this_month = True
        health_lost = random.randint(1, 3)
        if health_lost == 1:
            days_taken = random.randint(1, 3)
        elif health_lost == 2:
            days_taken = random.randint(4, 7)
        else:
            days_taken = random.randint(8, 10)
        i = 0
        if health_lost == 1:
            food_eaten_per_day_during_this_event = random.randint(7, 8)
        elif health_lost == 2:
            food_eaten_per_day_during_this_event = random.randint(9, 10)
        else:
            food_eaten_per_day_during_this_event = random.randint(11, 12)
        food_eaten = 0
        day += days_taken
        health_level -= health_lost
        while i < days_taken:
            if food_remaining > 0:
                food_remaining -= food_eaten_per_day_during_this_event
                food_eaten += food_eaten_per_day_during_this_event
            elif health_level > 0:
                health_level -= 1
            i += 1
        print('You were ambushed by hostile parties. You lost ' + str(health_lost) + ' health in the attack. It took ' + str(days_taken) + ' days to recover and you ate ' + str(food_eaten) + ' pounds of food.')
    if event == 'Snake bite':
        event_this_month = True
        health_lost = random.randint(1, 2)
        if health_lost == 1:
            days_taken = random.randint(1, 5)
        else:
            days_taken = random.randint(6, 10)
        i = 0
        if health_lost == 1:
            food_eaten_per_day_during_this_event = random.randint(7, 8)
        else:
            food_eaten_per_day_during_this_event = random.randint(9, 10)
        food_eaten = 0
        day += days_taken
        health_level -= health_lost
        while i < days_taken:
            if food_remaining > 0:
                food_remaining -= food_eaten_per_day_during_this_event
                food_eaten += food_eaten_per_day_during_this_event
            elif health_level > 0:
                health_level -= 1
            i += 1
        print('You were bitten by a snake on the trail. You lost ' + str(health_lost) + ' health. It took ' + str(days_taken) + ' days to recover and you ate ' + str(food_eaten) + ' pounds of food.')
    if event == 'Broken wheel' and traveled == True:
        event_this_month = True
        health_lost = random.randint(0, 1)
        if health_lost == 0:
            days_taken = random.randint(2, 4)
        else:
            days_taken = random.randint(5, 8)
        i = 0
        if health_lost == 0:
            food_eaten_per_day_during_this_event = random.randint(6, 8)
        else:
            food_eaten_per_day_during_this_event = random.randint(8, 10)
        food_eaten = 0
        day += days_taken
        health_level -= health_lost
        while i < days_taken:
            if food_remaining > 0:
                food_remaining -= food_eaten_per_day_during_this_event
                food_eaten += food_eaten_per_day_during_this_event
            elif health_level > 0:
                health_level -= 1
            i += 1
            if health_lost == 0:
                print('Your wheel broke while on the the trail. You fixed it without a problem. It took ' + str(days_taken) + ' days to fix it and you ate ' + str(food_eaten) + ' pounds of food.')
            else:
                print('Your wheel broke while on the the trail. You fixed it but you got hurt while you did. You lost 1 health. It took ' + str(days_taken) + ' days to fix it and you ate ' + str(food_eaten) + ' pounds of food.')
    if event == 'Mauled by a bear' and hunting == True:
        event_this_month = True
        health_lost = random.randint(1, 3)
        if health_lost == 1:
            days_taken = random.randint(1, 4)
        elif health_lost == 2:
            days_taken = random.randint(4, 7)
        else:
            days_taken = random.randint(7, 10)
        i = 0
        if health_lost == 1:
            food_eaten_per_day_during_this_event = random.randint(7, 8)
        elif health_lost == 2:
            food_eaten_per_day_during_this_event = random.randint(8, 9)
        else:
            food_eaten_per_day_during_this_event = random.randint(9, 10)
        food_eaten = 0
        day += days_taken
        health_level -= health_lost
        while i < days_taken:
            if food_remaining > 0:
                food_remaining -= food_eaten_per_day_during_this_event
                food_eaten += food_eaten_per_day_during_this_event
            elif health_level > 0:
                health_level -= 1
            i += 1
        print('You were mauled by a bear while hunting. You lost ' + str(health_lost) + ' health. It took ' + str(days_taken) + ' days to recover and you ate ' + str(food_eaten) + ' pounds of food.')
    if event == 'Gored by a boar' and hunting == True:
        event_this_month = True
        health_lost = random.randint(1, 2)
        if health_lost == 1:
            days_taken = random.randint(4, 7)
        else:
            days_taken = random.randint(7, 10)
        i = 0
        if health_lost == 1:
            food_eaten_per_day_during_this_event = random.randint(7, 8)
        else:
            food_eaten_per_day_during_this_event = random.randint(8, 9)
        food_eaten = 0
        day += days_taken
        health_level -= health_lost
        while i < days_taken:
            if food_remaining > 0:
                food_remaining -= food_eaten_per_day_during_this_event
                food_eaten += food_eaten_per_day_during_this_event
            elif health_level > 0:
                health_level -= 1
            i += 1
        print('You were gored by a boar while hunting. You lost ' + str(health_lost) + ' health. It took ' + str(days_taken) + ' days to recover and you ate ' + str(food_eaten) + ' pounds of food.')

def snow_slow():
    '''
    900
    650 miles
    450
    slowed after nov 1 if in the rockies (middle 650 miles)

	this will be checked at the start of every turn check for if in range, if in range set constant variable miles per travel to decreased value, otherwise set to starting value
    '''
    if month > 10 and (miles_traveled > 900 and miles_traveled < 1550):
        MIN_MILES_PER_TRAVEL = 20
        MAX_MILES_PER_TRAVEL = 50
        print('Your travel is slowed due to snow in the mountians.')
    else:
        MIN_MILES_PER_TRAVEL = 30
        MAX_MILES_PER_TRAVEL = 60

def choice():
    maybe_win()
    maybe_lose()
    print_status()
    choice = input(choice_text)
    if choice == 'travel' or choice == 'Travel' or choice == 't' or choice == 'T':
        travel()
    elif choice == 'hunt' or choice == 'Hunt' or choice == 'h' or choice == 'H':
        hunt()
    elif choice == 'rest' or choice == 'Rest' or choice == 'r' or choice == 'R':
        rest()
    elif choice == 'status' or choice == 'Status' or choice == 's' or choice == 'S':
        print_status()
    elif choice == 'help' or choice == 'Help'  or choice =='?':
        print_help()
    elif choice == 'quit' or choice == 'Quit' or choice == 'q' or choice == 'Q':
        print(quit_text)
        quit()
    else:
        print('please retry, enter "?" for help')
    event_occurs()

start_in_mo() 
while player_quits == False:
    choice()