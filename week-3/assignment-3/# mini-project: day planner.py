# mini-project: day planner
day = input("What day of the week is it? ").strip().lower()
time = input("Is it morning, afternoon, or evening? ").strip().lower() 

if (day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday") and time == "morning":
    print("Happy weekday morning! Lets get to work and do some coding.")
elif (day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday") and time == "afternoon":
    print("Good afternoon! Tired yet from studying or coding all morning? Maybe take a short break and come back later.")
elif (day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday") and time == "evening":
    print("Good evening! You made it through the work day. Don't lose your mind in the computer and maybe get some well-needed rest and hit it hard again the next morning.")
elif (day == "saturday" or day == "sunday") and time == "morning":
    print("Why are you even awake? Its the weekend! Sleep in and enjoy your morning.")
elif (day == "saturday" or day == "sunday") and time == "afternoon":
    print("Good weekend afternoon! Enjoy your day and maybe get some coding in if you feel like it.")
elif (day == "saturday" or day == "sunday") and time == "evening":
    print("Good weekend evening! Enjoy your night and maybe get some coding in if you feel like it.")
else:
    print("Sorry, I didn't understand that. Please make sure to enter a valid day of the week and time of day.")