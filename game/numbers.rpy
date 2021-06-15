label numbers:
    hide screen tutorial
    show screen example('numbers')

    #begin numbers
    $ player_health = 60
    e "Player health is currently: [player_health]"
    menu:
        "What to have for dinner?"

        "Pizza":
            $ player_health += 10
            e "Nice! I love pizza."

        "Veggies":
            $ player_health += 50
            # but we don't want player_health to exceed 100
            $ player_health = min(player_health, 100)
            e "Veggies? That's a super healthy choice!"

    e "Player health after dinner is: [player_health]"
    #end numbers

    jump start