# Using functions really saves us a lot of repeated code
# We have this pretty complex choice scenario coded up in just 50 lines :)

label functions:
    hide screen tutorial

    python:
        def make_smoothie(fruit):
            procedures = []
            procedures.append('Blending ' + fruit + 'in a blender...')
            procedures.append('Adding milk...')
            procedures.append('Enjoy a delicious ' + fruit + ' smoothie!\n\n')
            return procedures

        def add_to_player_health(player_health, value):
            result = player_health + value
            # but need to make sure result is between 0 and 100
            result = max(0, result) # if smaller than 0, use 0
            result = min(100, result) # if larger than 100, use 100
            return result

    $ wants_some_smoothie = True
    $ player_health = 60
    e "Player health is now [player_health]."

label functions_choices:
    menu:
        "What kind of smoothie shall we make?"

        "Apple":
            $ procedures = make_smoothie('apple')
            $ health_increment = 20

        "Dragonfruit":
            $ procedures = make_smoothie('dragonfruit')
            $ health_increment = 50

        "I've had enough smoothie for the day":
            $ wants_some_smoothie = False

    if wants_some_smoothie:
        python:
            first_procedure = procedures[0]
            second_procedure = procedures[1]
            third_procedure = procedures[2]
            player_health = add_to_player_health(player_health, health_increment)

        e "[first_procedure]"
        e "[second_procedure]"
        e "[third_procedure]"
        e "Player health is now [player_health]."

        jump functions_choices
    else:
        jump start