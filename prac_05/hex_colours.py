def hex_colours():
    COLOURS = {"aliceblue": '#f0f8ff', "antiquewhite": '#faebd7', "aquamarine1": '#7fffd4', "azure1": '#f0ffff',
               "beige": '#f5f5dc', "bisque1": '#ff34c4', "black": '#000000', "blue1": '#0000ff',
               "blueviolet": '#8a2be2', "chartreuse1": "#7fff00"}

    choose_colour = input("What colour are you looking up?")

    if choose_colour != "":
        print("Colour code is {} for {}".format(COLOURS.get(choose_colour), choose_colour))
        hex_colours()

hex_colours()