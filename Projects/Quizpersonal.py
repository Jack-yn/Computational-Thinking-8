# beginning: format and establish variables
import time
import os

def print_question(question, option_a, option_b):
    print(f"{question}")
    print(f"A) {option_a}")
    print(f"B) {option_b}")
    print()

def get_answer():
    while True:
        answer = input("Please choose A or B: ").strip().upper()
        if answer in ['A', 'B']:
            return answer
        else:
            print(" ")
            print("Invalid input! Please choose A or B.")

os.system('clear')

music_points = 0
movie_points = 0

# middle: ask questions
os.system('clear')
print_question("On a weekend would you rather", "Stay in and relax", "Go out with friends")
answer = get_answer()
if answer == "A" or "a":
    music_points += 1
elif answer == "B" or "b":
    movie_points += 1

os.system('clear')
print_question("When you're eating would you rather", "Listen to music", "Watch a show")
answer = get_answer()
if answer == "A" or "a":
    music_points += 1
elif answer == "B" or "b":
    movie_points += 1

os.system('clear')
print_question("Do you know more about your favorite show or your favorite band", "Favorite band", "Favorite show")
answer = get_answer()
if answer == "A" or "a":
    music_points += 1
elif answer == "B" or "b":
    movie_points += 1
    os.system('clear')

os.system('clear')
print_question("Would you rather", "Live without music", "Live without movies")
answer = get_answer()
if answer == "A" or "a":
    movie_points += 1
elif answer == "B" or "b":
    music_points += 1
    os.system('clear')

os.system('clear')
print_question("Would you rather", "Listen to the same album on repeat", "Watch the same season of a show on repeat")
answer = get_answer()
if answer == "A" or "a":
    movie_points += 1
elif answer == "B" or "b":
    music_points += 1
    os.system('clear')

os.system('clear')
print_question("Would you rather", "Have a lifetime spotify wrapped", "Have a lifetime highlight reel")
answer = get_answer()
if answer == "A" or "a":
    music_points += 1
elif answer == "B" or "b":
    movie_points += 1
    os.system('clear')

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