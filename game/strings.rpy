label strings:
    hide screen tutorial
    show screen example('strings')

    # show code example as in the Ren'Py official tutorial
    #begin strings
    $ string = "Learning Python for Ren'Py is fun!"
    e "I said: [string]"

    $ len_string = len(string)
    e "The string has a length of [len_string]"

    $ last_character = string[-1]
    e "The last character of the string is: [last_character]"

    $ string_uppercase = string.upper()
    e "I said: [string_uppercase]!!!!!"
    #end strings

    jump start