label sets:
    hide screen tutorial

    python:
        fruit_list = ['apple', 'banana', 'pear', 'apple']
        fruit_set = set(fruit_list)

        num_fruits = len(fruit_list)
        num_fruit_types = len(fruit_set)

    e "We have [num_fruits] fruits and [num_fruit_types] types of fruits."

label sets_choices:
    menu:
        "Let's get some different types of fruits. What shall we get?"

        "Mangoes":
            if 'mango' in fruit_set:
                e "We already have mangoes."
            else:
                $ fruit_set.add('mango')
                e "We got mangoes!"
            jump sets_choices

        "Apples":
            if 'apple' in fruit_set:
                e "We already have apples."
            jump sets_choices

        "We have everything we need!":
            pass

    e "We now have [num_fruit_types] types of fruits."

    jump start
