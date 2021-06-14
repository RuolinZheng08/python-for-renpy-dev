# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

screen tutorial:
    frame:
        xsize 640
        xalign .5
        ysize 485
        ypos 30

        add Solid('#f8f8ff')

        vbox:
            textbutton 'Strings' action Jump('strings')
            textbutton 'Numbers' action Jump('numbers')
            textbutton 'Booleans' action Jump('booleans')
            textbutton 'Lists' action Jump('lists')
            textbutton 'Sets' action Jump('sets')
            textbutton 'Dictionaries' action Jump('dictionaries')
            textbutton 'Conditional' action Jump('conditional')
            textbutton 'Loop' action Jump('loop')
            textbutton 'Iterables' action Jump('iterables')
            textbutton 'Functions' action Jump('functions')
            textbutton 'Classes' action Jump('classes')

label start:

    scene bg room
    show eileen happy
    show screen tutorial

    # These display lines of dialogue.

    # Lines that start with $ is intepreted as a Python statement
    $ print('Hello World!')

    python:
        # Lines that start with # is a comment and won't be evaluated by Ren'Py or Python
        print("Let's learn Python to power up our Ren'Py games")
        print("Are you ready?")

    # anything stored in persistent persists across game relaunches
    $ persistent.player_name = 'Python newbie'

    e "Welcome [persistent.player_name]. You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
