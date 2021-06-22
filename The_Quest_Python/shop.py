# Bob's Item Emporium


def run():
    import main
    import variables
    from items import Wallet

    shop = {'Sword': 50, "Shield": 60, "Potion": 20}
    shopOptions = {"Buy": 0, "Sell": 1, "Exit": 2}
    masonWallet = Wallet()
    masonWallet.currBalance += 100
    print("Welcome to Bob's Item Emporium! How can I help you today fine traveller!")

    print("Here are your options:")

    state = ''

    # Pick which shop function you want: Buy, Sell or Exit
    while state != 2:

        while state not in shopOptions and state != 2:
            for option in shopOptions:
                print(option)
            print("What would you like to do?")
            state = input()
            if state not in shopOptions:
                print("Oh dear, I'm afraid we don't do that here..\nWhat would you like to do?")
            if state == "Exit":
                state = 2
        choice = ''

        while state in shopOptions and choice != "Back":
            operation = shopOptions[state]

            # Buy Loop
            if operation == 0:
                print("Here are your options!")
                for item, price in shop.items():
                    print(item, ":", price)
                print('Back')
                print("What would you like?")
                choice = input()

                while choice in shop:
                    price = shop[choice]

                    # If you have adequate balance
                    if masonWallet.currBalance >= price:
                        masonWallet.currBalance -= price
                        print("You have purchased", choice)
                        print("You have", masonWallet.currBalance, "dollars remaining.")
                        print("Would you like anything else?")
                        for item, price in shop.items():
                            print(item + ":", price)
                        print("Back")
                        choice = input()

                    # If balance too low
                    else:
                        print("Im sorry, you don't have enough for that item.\nWas there anything else?")
                        for item, price in shop.items():
                            print(item, ":", price)
                        print('Back')
                        choice = input()

                # Item not in shop
                if choice not in shop and choice != "Back":
                    print("We don't seem to have any", choice)

            # Sell Block (not initialized)
            elif operation == 1:
                print("I'm afraid were not accepting items right now.")
                state = ''

            if choice == "Back":
                state = ''
    print("Thank you, have a spectacular day!")
    return 0
