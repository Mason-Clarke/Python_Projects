# Your Bedroom


def run():
    import main
    import variables

    options = {"look around": 1, "look": 1, "check": 1, "leave": 2, "shop": 2}
    option = -1

    print("What is your name?")
    variables.player.name = input()
    print("How old are you?")
    variables.player.age = input()

    while option != 0:
        if option == -1:
            print(variables.player.name + ", you wake up in a soft bed")
        elif option == 1:
            print("You look around the room and see WALLS")
        elif option == 2:
            print("You leave the bedroom and continue on your way.")
            return 2
        elif option == 99:
            print("You can't do that. Try something else.")

        print("What do you do?")
        option = input()

        for key in options:
            if option in options:
                option = options[option]
                break
            else:
                option = 99
