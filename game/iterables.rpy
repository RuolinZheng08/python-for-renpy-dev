# We are going to cover a little bit of screen language here
screen fruit_screen(fruit_list, fruit_set, fruit_colors):
    frame:
        xsize 640
        xalign .5
        ysize 485
        ypos 30

        add Solid('#000') # black

        hbox spacing 20:
            vbox:
                text 'Fruit List'
                for fruit in fruit_list:
                    text fruit

            vbox:
                text 'Fruit Set'
                for fruit in fruit_set:
                    text fruit color '#f00' # red

            vbox:
                text 'Fruit-Color Dictionary'
                for fruit in fruit_colors: # iterate over the keys
                    # look up the key
                    $ fruit_color = fruit_colors[fruit]
                    text fruit color '#f00' # red
                    text fruit_color

label iterables:
    hide screen tutorial

    python:
        fruit_list = ['apple', 'banana', 'pear', 'orange']
        fruit_set = set(['apple', 'banana', 'pear', 'orange'])
        fruit_colors = {'apple': 'red', 
                        'banana': 'yellow', 
                        'pear': 'green', 
                        'orange': 'orange'
                        }
    show screen fruit_screen(fruit_list, fruit_set, fruit_colors)

    e "We have a screen of fruits!"

    jump start