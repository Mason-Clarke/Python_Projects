# USE THE SAME FORMAT AS I HAVE HERE AND THEN WHEN YOU WANT TO EXIT TO A NEW PLACE
# SIMPLY USE exit() CODE IN THE OTHER PAGE WITH A NUMBER INSIDE THE PARENTHESIS

import your_home.your_bedroom
import your_home.your_hallway
import shop
import variables

adventure = 1
global_options = {"pick nose": "don't pick your nose"}

while adventure != 0:
    # your bedroom
    if adventure == 1:
        adventure = your_home.your_bedroom.run()

    # your hallway
    elif adventure == 2:
        adventure = your_home.your_hallway.run()

    # bob's item shop
    elif adventure == 3:
        adventure = shop.run()

    # insert new area
    elif adventure == 4:
        print("THIS IS A PLACEHOLDER")

    # insert new area
    elif adventure == 5:
        print("THIS IS A PLACEHOLDER")

print("GAMEOVER")
exit()
