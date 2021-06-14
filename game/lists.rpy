label lists:
    hide screen tutorial

    python:
        fruits = ['apple', 'banana', 'pear', 'apple']
        veggies = ['carrot', 'cabbage']
        ingredients = [fruits, veggies]

        num_fruits = len(fruits)
        num_veggies = len(veggies)
        num_ingredient = num_fruits + num_veggies
        num_ingredient_types = len(ingredients)

    e "We have [num_ingredient_types] types of ingredients."
    e "[num_fruits] fruits and [num_veggies] veggies, so a total of [num_ingredient] ingredients."

    e "Let's get some more veggies. How about celeries?"
    # ingredients[1] is the veggies list
    python:
        ingredients[1].append('celery')
        first_veggie_item = veggies[0] # equivalently ingredients[1][0]
        second_veggie_item = ingredients[1][1] # just to show you their equivalence
        last_veggie_item = veggies[-1]
    e "Our veggies are: [first_veggie_item], [second_veggie_item], [last_veggie_item]"

    jump start
