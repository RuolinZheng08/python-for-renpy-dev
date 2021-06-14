label conditional:
    hide screen tutorial

    e "How did you do on the midterm?"

    $ score = 95

    if 90 <= score <= 100:
        e "You got an A! Congrats!"
    elif 80 <= score <= 89:
        e "You got an B. Try harder next time!"
    else:
        e "You got some other grades. Don't worry."

    $ has_study_buddy = False
    menu:
        "Would you like to get a study buddy for the final?"

        "Nah I'm fine on my own" if 90 <= score <= 100:
            $ has_study_buddy = False

        "Of course!":
            $ has_study_buddy = True

    if has_study_buddy:
        e "Let's study together for the final!"
    else:
        e "Looks like you are studying alone for the final."

    jump start