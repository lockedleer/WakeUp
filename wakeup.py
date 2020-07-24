def decision_options(option1, option2):
    print("(%r or %r)" % (option1, option2))

def begin_day():
    sleep_in_counter = 0
    print("Do you want to get the day started?")
    cldecision_options("Out of bed", "Stay in bed")
    while True:
        decision = input("> ")
        if "stay" in decision and sleep_in_counter == 2:
            print("Clearly you don't want to go to work today.\nCall in sick and wake up another day.")
            return "new_day"
        elif "stay" in decision:
            print("You lay in bed for another 20 mins.")
            sleep_in_counter += 1
        elif "out" in decision:
            print("You get up and piss.")
            return "out"
        else:
            print("Make a decision.")

    
def morning_routine():
    coffee_counter = 0

def work_time_skip():
    print("You log in to your work station remotely.")
    print("The next 8 hours of your life pass by as you stare into the screen.")
    print("Some days, it feels longer. Some days, the time flies by.")
    


def start():
    while True:
        print("It's another day. Rise and shine.")
        print("The alarm goes off, it's 8:00 AM.")
        decision = begin_day()
        if decision == "new_day":
            continue
        elif decision == "out":
            print("You're out of bed.\nWork starts at 9:00 AM.")
            decision = morning_routine()
        else:
            print("YOU MADE IT! %r" % decision)
        

        


start()