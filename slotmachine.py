"""

Casino-style slotmachine with 1 row. Includes probabilities and different returns on a user's bet depending
on the rarity and "consequence" of the symbols matched.

slotmachine.py
Jeremy Liu
4/12/2025

"""

import random
import time

def main():

    # starting values
    initial_wallet = 500
    wallet = initial_wallet

    number_previouswin = 0
    number_gains = 0
    number_of_spins = 0

    # symbols that appear in the slot machine. Note: probability does not add to 100.
    sym1 = {"symbol": "💀", "probability": 2 / 100, "consequence": -50}
    sym2 = {"symbol": "🍍", "probability": 10 / 100, "consequence": 7}
    sym3 = {"symbol": "🍉", "probability": 10 / 100, "consequence": 7}
    sym4 = {"symbol": "🥑", "probability": 10 / 100, "consequence": 7}
    sym5 = {"symbol": "🍇", "probability": 15 / 100, "consequence": 9}
    sym6 = {"symbol": "🍏", "probability": 10 / 100, "consequence": 9}
    sym7 = {"symbol": "🍊", "probability": 15 / 100, "consequence": 12.5}
    sym8 = {"symbol": "🍎", "probability": 10 / 100, "consequence": 12.5}
    sym9 = {"symbol": "🍒", "probability": 15 / 100, "consequence": 12.5}
    sym10 = {"symbol": "🍈", "probability": 15 / 100, "consequence": 15}
    sym11 = {"symbol": "🍌", "probability": 10 / 100, "consequence": 25}
    sym12 = {"symbol": "👅", "probability": 25 / 100, "consequence": 50}
    sym13 = {"symbol": "🐵", "probability": 8 / 100, "consequence": -10}
    
    emojis = ["💀", "🍍", "🍉", "🥑", "🍇", "🍏", "🍊", "🍎", "🍒", "🍈", "🍌", "👅", "🐵"]

    symbols = [sym1, sym2, sym3, sym4, sym5, sym6, sym7, sym8, sym9, sym10, sym11, sym12, sym13]

    # expanded list comprehension

    probabilities = []
    for symbol in symbols:
        probabilities.append(symbol["probability"])

    while wallet > 0:
        try:
            bet = float(input(f"You have ${wallet:.2f} in your wallet.\nEnter your bet amount: "))
            if bet > wallet:
                print("🚫 Bet too big! Please enter a bet within your wallet's range.")
                continue # goes back to the while loop
            elif bet <= 0:
                print("🚫 Bet cannot be equal to or less than zero! Please try again.")
                continue # goes back to the while loop
        except EOFError:
            print("Aww... 😞. Are you sure? Come again!")
            exit()
        except ValueError:
            print("🚫 Please enter a valid number.")
            continue
        
        # the three random symbols chosen are chosen by random.choices
        # where (the symbols list, the weight of each is the probabiity, and there are three elements chosen total)
        # built in python function
        spin = random.choices(symbols, weights=probabilities, k=3)
        
        # appends the chosen symbols from the list to a new list which is to displayed later in the slotmachine
        symbols_displayed = []
        for chosen_symbol in spin:
            symbols_displayed.append(chosen_symbol["symbol"])
        
        # (spin) =              [{'symbol': '🍏', 'probability': 0.055, 'consequence': 20}, {'symbol': '👅', 'probability': 1.0, 'consequence': 5000}, {'symbol': '🍍', 'probability': 0.1, 'consequence': 10}]
        # (symbols_displayed) = ['🍏', '👅', '🍍']

        # first prints the slotmachine and then the results, gain/loss of wallet
        printer(symbols_displayed[0], symbols_displayed[1], symbols_displayed[2])

        # wallet gain/loss calculations

        if (symbols_displayed[0] == symbols_displayed[1] == symbols_displayed[2]) and (symbols_displayed[0] in emojis[8:12]): # 10th emoji to 14th (inclusive of first only)
            # symbols_displayed[0]["consequence"] looks at the first element of the list's value in the dictionary
            # emojis[10:15] is "🥭", "🍋", "🍌", "👅", "🐵"

            gain = spin[0]["consequence"] * 3 * (bet/10)

            if spin[0]["symbol"] == "🐵":
                print("A monkey (🐵) has griefed you! HAHA!")

            elif spin[0]["symbol"] in ["🍌", "👅"]:
                time.sleep(1)
                for _ in range(100): # prints 100 times
                    celebrator("🎉🎉🎉🎆🎆🎆 ELITE JACKPOT! 🎆🎆🎆🎉🎉🎉")
                    time.sleep(0.1)
                time.sleep(0.9)
                print("🎉🎉🎉🎆🎆🎆 THREE IN A ROW! 🎆🎆🎆🎉🎉🎉")
                time.sleep(1)

            else:
                time.sleep(1)
                for _ in range(5):
                    celebrator("🎉🎉🎉 GIANT JACKPOT! 🎉🎉🎉")
                    time.sleep(0.1)
                time.sleep(0.9)
                print("🎉🎉🎉 THREE IN A ROW! 🎉🎉🎉")
                time.sleep(1)

        elif symbols_displayed[0] == symbols_displayed[1] == symbols_displayed[2]:
            gain = spin[0]["consequence"] * 3 * (bet/10)

            if spin[0]["symbol"] == "🐵":
                print("A monkey (🐵) has griefed you! HAHA!")
            else:
                celebrator("🎉 minor jackpot! 3 in a row!")

        elif symbols_displayed[0] == symbols_displayed[1] or symbols_displayed[0] == symbols_displayed[2] or symbols_displayed[1] == symbols_displayed[2]:
            # need to determine which symbols matched
            for symbol in spin:
                if symbols_displayed.count(symbol["symbol"]) >= 2:

                    if symbol["symbol"] == "🐵":
                        print("A monkey (🐵) has griefed you! HAHA!")

                    elif symbol["symbol"] in emojis[8:12]:

                        if symbol["symbol"] in ["🍌", "👅"]:
                            time.sleep(1)
                            for _ in range(5):
                                celebrator("☀️☀️🌞🌞 !!!!!!!!!!! 🌞🌞☀️☀️")
                                time.sleep(0.1)
                            time.sleep(0.9)
                            print("☀️☀️🌞🌞 TWO RARE MATCHING SYMBOLS! 🌞🌞☀️☀️")

                        else:
                            time.sleep(1)
                            for _ in range(3):
                                celebrator("👍👍👍 SWEET!")
                                time.sleep(0.1)
                            time.sleep(0.9)
                            print("💛 Two great matching symbols! 🪙")

                    else:
                        celebrator("👍 nice! two matching symbols!")

                    gain = symbol["consequence"] * 1.5 * (bet/10)
                    break

        else:
            # gain is the lost bet, so wallet += gain is really wallet - bet
            gain = -bet # not gain -= bet because the gain variable hasn't been created yet
            print("Awww... no match 😞. Try again!")
        
        # wallet's gain
        wallet += gain
        number_of_spins += 1

        if gain <= 0:
            number_previouswin += 1
        else:
            number_previouswin = 0
            number_gains += 1

        print()
        try:
            print(f"Spin #: {number_of_spins} | Avg spins per win: {number_of_spins/number_gains:.2f}")
        except ZeroDivisionError:
            print(f"Spin #: {number_of_spins:.2f} | Avg spins per win: ZeroDivisionError")
        
        print(f"# of spins since last win: {number_previouswin}")
        print()
        print(f"Change: {gain:+.2f} | Wallet: ${wallet:.2f}")
        
        if wallet <= 0:
            
            print("💀 You're temporarily out of money. Try again!")
            time.sleep(1.5)
            print("Restarting! Slot machine ready!")
            time.sleep(1.5)
            wallet += initial_wallet

def printer(first_symbol, second_symbol, third_symbol):
    print(f"""
                              .-------.
                              | SLOTS |
                  ____________|=======|____________
                 |  __    __    ___  _____   __    |
                 | / _\  / /   /___\/__   \ / _\   |
                 | \ \  / /   //  //  / /\ \\ \    |
                 | _\ \/ /___/ \_//  / /  \/_\ \ []|
                 | \__/\____/\___/   \/     \__/ []|
                 |===_______===_______===_______===|
                 ||*|       |*|       |*|       |*||
                 ||*|       |*|       |*|       |*||
                 ||*|  {first_symbol}   |*|  {second_symbol}   |*|  {third_symbol}   |*||
                 ||*|       |*|       |*|       |*|| __
                 ||*|_______|*|_______|*|_______|*||(__)
                 |===_______===_______===_______===| ||
                 ||*|       |*|       |*|       |*|| ||
                 ||*|_______|*|_______|*|_______|*||_//
                 |lc=___________________________===|_/
                 |  /___________________________\  |
                 |   |  note: gambling is not  |   |
                _|    \__condoned by: Jeremy__/    |_
               (_____________________________________)
    """)

def celebrator(prompt):

    for _ in range(3):

        for _ in range(random.randint(10, 25)):
            prompt += " "
        prompt += random.choice(["💵", "💸", "💰", "❤️", "🧧",])

    print(prompt)

main()
