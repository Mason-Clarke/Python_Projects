# TEMPLATE FOR NEW PLACES


def run():
    import main
    import variables

    options = {"look": 1, "check": 1, "leave": 2, "walk out": 2}
    option = -1

    while option != 0:
        if option == -1:
            print("Insert place description here.")
        elif option == 1:
            print("You look.")
        elif option == 2:
            print("You leave.")
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
