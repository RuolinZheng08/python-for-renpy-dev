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
            null height 20
            textbutton 'Strings' action Jump('strings') left_padding 20
            textbutton 'Numbers' action Jump('numbers') left_padding 20
            textbutton 'Booleans' action Jump('booleans') left_padding 20
            textbutton 'Lists' action Jump('lists') left_padding 20
            textbutton 'Sets' action Jump('sets') left_padding 20
            textbutton 'Dictionaries' action Jump('dictionaries') left_padding 20
            textbutton 'Conditional' action Jump('conditional') left_padding 20
            textbutton 'Loop' action Jump('loop') left_padding 20
            textbutton 'Iterables' action Jump('iterables') left_padding 20
            textbutton 'Functions' action Jump('functions') left_padding 20
            textbutton 'Classes' action Jump('classes') left_padding 20

label start:

    scene bg room
    show eileen happy
    hide screen example # code snippet example
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
