import random

def decision_options(option1, option2):
    print("(%r or %r)" % (option1, option2))

def begin_day():
    sleep_in_counter = 0
    print("Do you want to get the day started?")
    while True:
        decision_options("Out of bed", "Stay in bed")
        decision = input("> ")
        if "stay" in decision and sleep_in_counter == 2:
            print("Clearly you don't want to go to work today.\nCall in sick and wake up another day.")
            start()
        elif "stay" in decision:
            print("You lay in bed for another 20 mins.")
            sleep_in_counter += 1
        elif "out" in decision:
            print("You get up and piss.")
            print("You're out of bed.\nWork starts at 9:00 AM.")
            morning_routine()
        else:
            print("Make a decision.")

    
def morning_routine():
    coffee_counter = 0
    print("It's alwayts nice to start the day with a coffee,\nbut you might want to stretch instead to wake up?")
    decision_options("Coffee", "Stretch")
    while True:
        decision = input("> ")
        if "coffee" in decision and coffee_counter == 2:
            print("You've overloaded on coffee, and have an anxiety attack.")
            print("Due to this you decide to take the day off work, and calm down.")
            start()
        if "coffee" in decision:
            print("You enjoy a cup of coffee and feel refreshed.")
            coffee_counter += 1
        elif "stretch" in decision:
            print("You salute the sun by doing 5 progressive sun salutations.")
            print("Followed up by 10 minutes of meditation.")
            print("You feel refreshed and ready for anything.")
            daily_activity()
        else:
            print("Make a decision.")


def daily_activity():
    print("Now that you're ready, how would you like to spend your day?")
    while True:
        decision_options("Work", "Outside")
        decision = input("> ")
        if "work" in decision:
            work_time_skip()
        elif "outside" in decision:
            print("You don't feel like working today.\n How would you like to spend your time outside?")
            decision_options("Walk", "Bike")
            decision = input("> ")
            if "walk" in decision:
                walk_time_skip()
            elif "bike" in decision:
                bike_time_skip()
            else:
                print("Make a decision.")
        else:
            print("Make a decision.")



def work_time_skip():
    print("You log in to your work station remotely.")
    print("The next 8 hours of your life pass by as you stare into the screen.")
    print("Some days, it feels longer. Some days, the time flies by.")
    afternoon_routine()

def walk_time_skip():
    print("You decide to go for a long walk today.\nDo you want to go East or West")
    outdoor_direction_decision()

def bike_time_skip():
    print("You decide to go for a long bike ride today.\nDo you want to go East or West")
    outdoor_direction_decision()


def outdoor_direction_decision():
    random_occurences = [
    'You see a homeless man, and search your pocket for change. You give him what little you can and he smiles.',
    'A dog is running wildly without supervision, you wonder where it\'s owner is.',
    'There\'s a family enjoying a picnic in a park, they look content and happy in life.',
    'There\'s a protest occuring, you wonder what it is for in this desolate time. It could be anything.',
    'A busker is playing your favorite song. You sit and listen for a bit before giving them some pocket change.'
    ]
    while True:
        decision_options("East", "West")
        decision = input("> ")
        if "east" in decision or "west" in decision:
            print("You head off to the %r, Along the way you see:" % decision)
            for i in range(3):
                print(random.choice(random_occurences))
            afternoon_routine()
        else:
            print("Make a decision.")


def afternoon_routine():
    print("It's the afternoon, and you're free to enjoy your hobbies.")
    while True:
        decision_options("Art", "Video Games")
        decision = input("> ")
        if "art" in decision:
            print("You decide to paint and draw. \nThe Warhammer figures that have been left unpainted for months now are beckoning.")
            nighttime_routine()
        elif "games" in decision:
            print("Video Games and adventure are calling, you settle in for the long haul with snacks and beverages.")
            nighttime_routine()
        else:
            print("Make a decision.")

def nighttime_routine():
    print("After a long day, it's time for bed.")
    print("Taking the time to brush your teeth, and wash your face,\nyou make your way to bed and read until you pass out.")
    print("During lockdown everyday has been the same routine, with subtle variety thrown in. \nMost days have been good, but some are long and unbearable.")
    print("Oh well! there's always tomorrow. Time to start another day.\n\n")
    start()

def start():
    while True:
        print("It's another day. Rise and shine.")
        print("The alarm goes off, it's 8:00 AM.")
        begin_day()
        
        
start()