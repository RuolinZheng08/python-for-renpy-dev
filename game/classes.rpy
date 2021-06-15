#begin classes
label classes:
    hide screen tutorial
    show screen example('classes')

    python:
        class Animal():
          def __init__(self, name, speech):
            self.name = name
            self.speech = speech
            self.health = 50

          def greet(self):
            # string concatenation
            greeting = self.name + ' says ' + self.speech
            return greeting
          
          def add_health(self, value):
            self.health += value
            # but need to make sure self.health is between 0 and 100
            self.health = max(0, self.health) # if smaller than 0, use 0
            self.health = min(100, self.health) # if larger than 100, use 100
            # no return value

    e "Let's get a pet and give it a name!"
    python:
        animal_name = renpy.input("What's the pet's name?")
        animal_speech = renpy.input("What does it say?")
        animal = Animal(animal_name, animal_speech)
        greeting = animal.greet()
    e "Here is a message from your pet: [greeting]"
    e "Your pet currently has health [animal.health]"
    $ is_interacting_with_pet = True

label classes_choices:
    menu:
        "What to do with the pet?"

        "Feed the pet":
            $ animal.add_health(20)

        "Play with the pet":
            $ animal.add_health(50)

        "Do nothing":
            $ is_interacting_with_pet = False

    if is_interacting_with_pet:
        e "Your pet currently has health [animal.health]"
        jump classes_choices
    else:
        jump start
#end classes