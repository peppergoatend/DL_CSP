# DL, Condtional Notes

military_time = 900

if military_time > 600:
    print("It's too early why are you awake!!")
elif military_time < 900:
    print("Good Morning!")
elif military_time < 1200:
    print("Good Morning! You should be at school!")
elif military_time < 1700:
    print("Good Afternoon.")
else:
    print("Good Evening!")

# nesting conditionals
day = "Saturday"
time = 800

if time > 900 and time < 1600:
    if day != "Saturday" or day != "Sunday":
        print("You should be a school!")
    else:
        if time > 1200:
            print("Good Afternoon!")
        else:
            print("Good Morning!")
else:
    print("You are not required to be in school")