label dictionaries:
    hide screen tutorial
    show screen example('dictionaries')

    #begin dictionaries
    python:
        grades = {'A': [90, 100], 
                  'B': [80, 89], 
                  'C': [70, 79], 
                  'D': [60, 69],
                  'F': [0, 59]}

    menu:
        "What letter grade did you get on the midterm?"

        "A":
            $ score_range = grades['A']
        "B":
            $ score_range = grades['B']
        "C":
            $ score_range = grades['C']
        "D":
            $ score_range = grades['D']
        "F":
            $ score_range = grades['F']

    $ score_lower = score_range[0]
    $ score_upper = score_range[1]
    e "So you got a score between [score_lower] and [score_upper]."
    #end dictionaries

    jump start