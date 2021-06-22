# Your Hallway


def run():
    import main
    import variables

    options = {"look": 1, "check": 1, "leave": 2, "walk out": 2}
    option = -1

    while option != 0:
        if option == -1:
            print("You enter the hallway.")
        elif option == 1:
            print("You see pictures on the wall. Will you inspect further?")
            pictures()
        elif option == 2:
            print("You leave.")
            return 3
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


def pictures():
    picture_choice = "temp"
    while picture_choice != "yes" or "no":
        picture_choice = input()
        if picture_choice == "yes":
            print("You see a picture that you don't recognize. Where did this come from?")
            print("You return your attention to the rest of the hallway.")
            return
        elif picture_choice == "no":
            print("You look away")
            print("You return your attention to the rest of the hallway.")
            return
        else:
            print("You need to make a choice, yes or no.")
