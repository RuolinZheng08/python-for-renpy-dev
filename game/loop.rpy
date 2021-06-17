label loop:
    hide screen tutorial
    show screen example('loop')

    #begin loop
    $ countdown = 5
    e "Let's start the countdown from [countdown]."

    while countdown > 0:
        e "Countdown value: [countdown]"
        $ countdown -= 1

    e "The end value of countdown is [countdown]"
    #end loop

    jump start