

def begin_day(hour, minute):
    print("Do you even feel like you want to get out of bed?")
    print("Get out of bed or stay in bed")
    while True:
        decision = input("> ")
        if "stay" in decision and minute == 6:
            print("Clearly you don't want to go to work today.\nCall in sick and wake up another day.")
            return "new_day"
        elif "stay" in decision:
            print("The clock says it's: %d:%d0 AM." % (hour, minute))
            print("You lay in bed for another 20 mins.")
            minute += 2
        elif "get" in decision:
            print("You get up and piss.")
            print("Do you want to make coffee or stretch?")
            return "coffee or stretch"
        else:
            print("Make a decision.")

    

    
    


def start():
    hour = 7
    minute = 0
    print("It's another day.")
    print("The alarm goes off, it's %d:%d0 AM." % (hour, minute))
    
    while True:
        decision = begin_day(hour, minute)
        if decision == "new_day":
            continue
        else:
            print("YOU MADE IT! %r" % decision)
        

        


start()