label booleans:
    hide screen tutorial

    python:
        has_visited_park = False
        has_visited_shop = False
        has_visited_beach = False

label boolean_choices:
    menu:
        "Where to hang out for the day?"

        # We will cover conditionals `if-else` in later sections
        "Park" if not has_visited_park:
            e "Let's go to the park!"
            $ has_visited_park = True
            jump boolean_choices

        "Beach" if not has_visited_beach:
            if not has_visited_shop:
                e "I'd love to visit the beach, but maybe we can stop by the store to get some ice cream first?"
            else:
                e "Great! We have everything we need. Let's go to the beach!"
                $ has_visited_beach = True
            jump boolean_choices

        "Shop" if not has_visited_shop:
            e "Let's get some ice cream!"
            $ has_visited_shop = True
            jump boolean_choices

    jump start