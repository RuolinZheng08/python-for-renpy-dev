# We are going to cover a little bit of screen language here

#begin iterables
screen fruit_screen(fruit_list, fruit_set, fruit_colors):
    frame:
        xsize 640
        xalign .5
        ysize 300
        ypos 30

        add Solid('#000') # black

        hbox spacing 20:
            vbox:
                text 'Fruit List'
                for fruit in fruit_list:
                    text fruit

            vbox:
                text 'Fruit Set' color '#f00' # red text
                for fruit in fruit_set:
                    text fruit color '#f00' # red text

            vbox:
                text 'Fruit Inventory'
                for fruit in fruit_inventory: # iterate over the keys
                    # look up the key
                    $ fruit_quantity = fruit_inventory[fruit]
                    hbox:
                        text fruit
                        null width 10
                        # fruit_quantity is an integer so we convert it to string
                        text str(fruit_quantity) color '#f00' # red text

label iterables:
    hide screen tutorial
    show screen example('iterables')

    python:
        fruit_list = ['apple', 'banana', 'pear', 'orange']
        fruit_set = set(['apple', 'banana', 'pear', 'orange'])
        fruit_inventory = {'apple': 2, 
                        'banana': 0, 
                        'pear': 3, 
                        'orange': 1
                        }
    show screen fruit_screen(fruit_list, fruit_set, fruit_inventory)

    e "We have a screen of fruits!"

    hide screen fruit_screen
    jump start
#end iterables