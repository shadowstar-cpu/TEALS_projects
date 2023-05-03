print('Hello! were going to do a basic personality test on you! ')

repeat = 'y'

while (repeat != 'n'):

  name = input('What is your name? ')

  birth_month = int(input('What month were you born in? Please use the number of the month. '))

  birth_day = int(input('What day were you born? '))

  fav_color = input('What is your favorite color? ')

  zodiac_list = ['capricorn', 'aquarius', 'pisces', 'aries', 'taures', 'gemini',
   'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagitarrius']

  zodiac = 'None'

  if birth_month == 1 and (birth_day >= 1 and birth_day <= 19):
    zodiac = zodiac_list[0]
  elif birth_month == 1 and (birth_day >= 20 and birth_day <= 31):
    zodiac = zodiac_list[1]
  elif birth_month == 2 and (birth_day >= 1 and birth_day <= 18):
    zodiac = zodiac_list[1]
  elif birth_month == 2 and (birth_day >= 19 and birth_day <= 29):
    zodiac = zodiac_list[2]
  elif birth_month == 3 and (birth_day >= 1 and birth_day <= 20):
    zodiac = zodiac_list[2]
  elif birth_month == 3 and (birth_day >= 21 and birth_day <= 30):
    zodiac = zodiac_list[3]
  elif birth_month == 4 and (birth_day >= 1 and birth_day <= 19):
    zodiac = zodiac_list[3]
  elif birth_month == 4 and (birth_day >= 20 and birth_day <= 31):
    zodiac = zodiac_list[4] 
  elif birth_month == 5 and (birth_day >= 1 and birth_day <= 20):
    zodiac = zodiac_list[4]
  elif birth_month == 5 and (birth_day >= 21 and birth_day <= 31):
    zodiac = zodiac_list[5]
  elif birth_month == 6 and (birth_day >= 1 and birth_day <= 21):
    zodiac = zodiac_list[5]
  elif birth_month == 6 and (birth_day >= 22 and birth_day <= 30):
    zodiac = zodiac_list[6]
  elif birth_month == 7 and (birth_day >= 1 and birth_day <= 22):
    zodiac = zodiac_list[6]
  elif birth_month == 7 and (birth_day >= 23 and birth_day <= 31):
    zodiac = zodiac_list[7]
  elif birth_month == 8 and (birth_day >= 1 and birth_day <= 22):
    zodiac = zodiac_list[7]
  elif birth_month == 8 and (birth_day >= 23 and birth_day <= 31):
    zodiac = zodiac_list[8]
  elif birth_month == 9 and (birth_day >= 1 and birth_day <= 22):
    zodiac = zodiac_list[8]
  elif birth_month == 9 and (birth_day >= 23 and birth_day <= 31):
    zodiac = zodiac_list[9]
  elif birth_month == 10 and (birth_day >= 1 and birth_day <= 23):
    zodiac = zodiac_list[9]
  elif birth_month == 10 and (birth_day >= 24 and birth_day <= 31):
    zodiac = zodiac_list[10]
  elif birth_month == 11 and (birth_day >= 1 and birth_day <= 21):
    zodiac = zodiac_list[10]
  elif birth_month == 11 and (birth_day >= 22 and birth_day <= 30):
    zodiac = zodiac_list[11]
  elif birth_month == 12 and (birth_day >= 1 and birth_day <= 21):
    zodiac = zodiac_list[11]
  elif birth_month == 12 and (birth_day >= 22 and birth_day <= 31):
    zodiac = zodiac_list[0]

  personalityz = ['none', 'none', 'none', 'none', 'none']

  if zodiac == 'capricorn':
    personalityz = ['sensitive', 'persistent', 'ambitious', 'hard-working', 'impatient']
  elif zodiac == 'aquarius':
    personalityz = ['unique', 'intelligent' ,'impulsive', 'loyal', 'optimistic']
  elif zodiac == 'pisces':
    personalityz = ['compassionate', 'artistic', 'emotional', 'empathetic', 'creative']
  elif zodiac == 'aries':
    personalityz = ['fiery', 'passionate', 'domineering', 'confident', 'courageous']
  elif zodiac == 'taures':
    personalityz = ['hard-headed', 'tenacious', 'reliable', 'loyal', 'sensual']
  elif zodiac == 'gemini':
    personalityz = ['flexible', 'clever', 'impulsive', 'unreliable', 'playful']
  elif zodiac == 'cancer':
    personalityz = ['nuturing','loyal','protective', 'moody', 'clingy']
  elif zodiac == 'leo':
    personalityz = ['confident', 'comfortable', 'drama-adoring', 'generous', 'loving']
  elif zodiac == 'virgo':
    personalityz = ['hard-working', 'creative', 'patient', 'critical', 'stubborn']
  elif zodiac == 'libra':
    personalityz = ['charming', 'attractive', 'well-balanced', 'self-indulgent', 'peaceful']
  elif zodiac == 'scorpio':
    personalityz = ['brave', 'honest', 'jealous', 'loyal', 'resentful']
  elif zodiac == 'sagittarius':
    personalityz = ['optimistic', 'hilarious', 'fair-minded', 'intellectual', 'spontaneous']

  personalityc = ['none', 'none', 'none', 'none', 'none']

  if fav_color == 'black' or fav_color == 'Black':
    personalityc = ['strong-willed', 'determined', 'demanding']
  elif fav_color == 'blue' or fav_color == 'Blue':
    personalityc = ['sensitive', 'reliable', 'serene']
  elif fav_color == 'green' or fav_color == 'Green':
    personalityc = ['analytical', 'conceptual', 'inventive']
  elif fav_color == 'yellow' or fav_color == 'Yellow':
    personalityc = ['joyful', 'optimistic', 'fun']
  elif fav_color == 'purple' or fav_color == 'Purple':
    personalityc = ['intuitive', 'spiritual', 'charismatic']
  elif fav_color == 'red' or fav_color == 'Red':
    personalityc = ['bold', 'boisterous', 'passionate']
  elif fav_color == 'brown' or fav_color == 'Brown':
    personalityc = ['strength', 'reliable', 'resilient']
  elif fav_color == 'grey' or fav_color == 'Grey':
    personalityc = ['detached', 'reliable', 'composed']
  elif fav_color == 'pink' or fav_color == 'Pink':
    personalityc = ['loving', 'sensual', 'senstive']
  elif fav_color == 'orange' or fav_color == 'Orange':
    personalityc = ['warm', 'enthusiastic', 'tolerant']

  if personalityz[0] == personalityc[0]:
    personalityc.remove(personalityz[0])
  elif personalityz[0] == personalityc[1]:
    personalityc.remove(personalityz[0])
  elif personalityz[0] == personalityc[2]:
    personalityc.remove(personalityz[0])
  elif personalityz[1] == personalityc[0]:
    personalityc.remove(personalityz[1])
  elif personalityz[1] == personalityc[1]:
    personalityc.remove(personalityz[1])
  elif personalityz[1] == personalityc[2]:
    personalityc.remove(personalityz[1])
  elif personalityz[2] == personalityc[0]:
    personalityc.remove(personalityz[2])
  elif personalityz[2] == personalityc[1]:
    personalityc.remove(personalityz[2])
  elif personalityz[2] == personalityc[2]:
    personalityc.remove(personalityz[2])
  elif personalityz[3] == personalityc[0]:
    personalityc.remove(personalityz[3])
  elif personalityz[3] == personalityc[1]:
    personalityc.remove(personalityz[3])
  elif personalityz[3] == personalityc[2]:
    personalityc.remove(personalityz[3])
  elif personalityz[4] == personalityc[0]:
    personalityc.remove(personalityz[4])
  elif personalityz[4] == personalityc[1]:
    personalityc.remove(personalityz[4])
  elif personalityz[4] == personalityc[2]:
    personalityc.remove(personalityz[4])

  if len(personalityz) == 5 and len(personalityc) == 3:
    print('Youre zodiac sign is: ' + zodiac +
    '. \nAccording to this your personality is ' + personalityz[0] + ', ' 
    + personalityz[1] + ', ' + personalityz[2] + ', ' + personalityz[3] +
    ', ' + personalityz[4] + '. \nAccording to your favorite color ' +
    'your personality is ' + personalityc[0] + ', ' + personalityc[1] + ', ' + personalityc[2] + '. ')

  elif len(personalityz) == 5 and len(personalityc) == 2:
    print('Youre zodiac sign is: ' + zodiac +
    '. \nAccording to this your personality is ' + personalityz[0] + ', ' 
    + personalityz[1] + ', ' + personalityz[2] + ', ' + personalityz[3] +
    ', ' + personalityz[4] + '. \nAccording to your favorite color ' +
    'your personality is ' + personalityc[0] + ', ' + personalityc[1] + '. ')

  elif len(personalityz) == 5 and len(personalityc) == 1:
    print('Youre zodiac sign is: ' + zodiac +
    '. \nAccording to this your personality is ' + personalityz[0] + ', ' 
    + personalityz[1] + ', ' + personalityz[2] + ', ' + personalityz[3] +
    ', ' + personalityz[4] + '. \nAccording to your favorite color ' +
    'your personality is ' + personalityc[0] + '. ')

  elif len(personalityz) == 5 and len(personalityc) == 0:
    print('Youre zodiac sign is: ' + zodiac +
    '. \nAccording to this your personality is ' + personalityz[0] + ', ' 
    + personalityz[1] + ', ' + personalityz[2] + ', ' + personalityz[3] +
    ', ' + personalityz[4] + '. \nAll the traits of your favorite color are in your zodiac traits')

  def Name_Date(name, date):
    print("This program was made by, " + name + ", on, 1/31/23, it was last edited on " + date)
  Name_Date("Ronald Nickelson", "3/5/23")

  repeat = input('would you like to repeat this program? ')