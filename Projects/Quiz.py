import os
import time

music_points = 0
movie_points = 0

# middle: ask questions
os.system('clear')
answer = input ("On a weekend would you rather, A) Stay in and relax, B) Go out with friends")
if answer == "A" or "a":
    music_points += 1
elif answer == "B" or "b":
    movie_points += 1

os.system('clear')
answer = input ("When you're eating would you rather, A) Listen to music, B) Watch a show")
if answer == "A" or "a":
    music_points += 1
elif answer == "B" or "b":
    movie_points += 1

os.system('clear')
answer = input("Do you know more about, A) Favorite band, B) Favorite show")
if answer == "A" or "a":
    music_points += 1
elif answer == "B" or "b":
    movie_points += 1

os.system('clear')
answer = input("Would you rather, A) Live without music, B) Live without movies")
if answer == "A" or "a":
    movie_points += 1
elif answer == "B" or "b":
    music_points += 1

os.system('clear')
answer = input("Would you rather, A) Listen to the same album on repeat, B) Watch the same season of a show on repeat")
if answer == "A" or "a":
    movie_points += 1
elif answer == "B" or "b":
    music_points += 1

os.system('clear')
answer = input("Would you rather, A) Have a lifetime spotify wrapped, B) Have a lifetime highlight reel")
if answer == "A" or "a":
    music_points += 1
elif answer == "B" or "b":
    movie_points += 1

# end: display results
if music_points > movie_points:
    os.system('clear')
    print ("Drumroll please!")
    time.sleep(2)
    os.system('clear')
    print("You like music more!")
elif music_points < movie_points:
    os.system('clear')
    print ("Drumroll please!")
    time.sleep(2)
    os.system('clear')
    print("You like movies more!")
else:
    os.system('clear')
    print ("Drumroll please!")
    time.sleep(2)
    os.system('clear')
    print("You like both equally!")