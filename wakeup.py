def decision_options(option1, option2):
    print("(%r or %r)" % (option1, option2))

def begin_day():
    sleep_in_counter = 0
    print("Do you want to get the day started?")
    decision_options("Out of bed", "Stay in bed")
    while True:
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
    decision_options("Work", "Outside")
    while True:
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
    decision_options("East", "West")

def bike_time_skip():
    print("You decide to go for a long bike ride today.\nDo you want to go East or West")
    decision_options("East", "West")

def afternoon_routine():
    print("It's the afternoon, and you're free to enjoy your hobbies.")

    


def start():
    while True:
        print("It's another day. Rise and shine.")
        print("The alarm goes off, it's 8:00 AM.")
        begin_day()
        
        
start()