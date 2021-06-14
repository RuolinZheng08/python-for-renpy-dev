label loop:
    hide screen tutorial

    $ countdown = 5
    e "Let's start the countdown from [countdown]."

    while countdown > 0:
        $ countdown -= 1
        e "Countdown value: [countdown]"

    e "The end value of countdown is [countdown]"

    jump start