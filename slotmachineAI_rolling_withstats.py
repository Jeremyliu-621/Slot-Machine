import random
import time

def main():

    # starting vars (changeable)
    initial_wallet = 500
    max_spins = 100
    allow_refills = True
    sleeptime = 1
    wallet_divider = 10
    
    # starting vars (unchangeable)
    wallet = initial_wallet
    total_gain = 0
    total_loss = 0
    number_of_spins = 0
    number_gains = 0
    number_losses = 0
    number_refills = 0

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

    while wallet > 0 and number_of_spins < max_spins:
        
        bet = wallet/wallet_divider

        print(f"The AI's bet is 1/10 of the wallet, so bet == {wallet/10}")
        
        if sleeptime > 0:
            time.sleep(sleeptime)
        
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
                            print("☀️☀️🌞🌞 TWO GIANT MATCHING SYMBOLS! 🌞🌞☀️☀️")
                        else:
                            print("👍👍👍 SWEET! two great matching symbols!")

                    else:
                        time.sleep(1)
                        for _ in range(3):
                            celebrator("👍👍👍 SWEET!")
                            time.sleep(0.1)
                        time.sleep(0.9)
                        print("💛 Two great matching symbols! 🪙")

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
            number_losses += 1
            total_loss += gain
        if gain > 0:
            number_gains += 1
            total_gain += gain
        
        if wallet <= 1:
            
            if allow_refills:
                print("💀 You're temporarily out of money. Try again!")
                time.sleep(1.5)
                print("Restarting! Slot machine ready!")
                time.sleep(1.5)
                wallet += initial_wallet
            
            else:
                exit()

        print()
        print(f"Change: {gain:+.2f}")
        print()
        print(f"Number of spins: {number_of_spins}")
        print(f"Number of gains: {number_gains}")
        print(f"Number of losses: {number_losses}")
        try:
            print(f"Percent chance to win: {((number_gains/number_of_spins)*100)}")
        except ZeroDivisionError:
            print(f"Percent chance to win: ZeroDivisionError")
        print()
        print(f"Wallet: ${wallet:.2f}")
        print(f"Total Gain: {total_gain:+.2f}")
        print(f"Total Loss: ${total_loss:.2f}")
        print()
        print(f"Net revenue for gambler: ${(total_gain+total_loss):.2f}")
        print(f"Net revenue for casino: ${-(total_gain+total_loss):.2f}")
        print()
        print(f"Average change for gambler (taking into account starting wallet): {((total_gain+total_loss) / number_of_spins):+.5f}")
        print(f"Average gain for casino (taking into account starting wallet): {(-((total_gain+total_loss) / number_of_spins)):+.5f}")
        print(f"(Average change for gambler / starting wallet) * 100: {(((total_gain+total_loss) * 100/ number_of_spins)/initial_wallet):+.4f}% of initial wallet")
        print(f"(Average change for casino / starting wallet) * 100: {(-((total_gain+total_loss) * 100/ number_of_spins)/initial_wallet):+.4f}% of initial wallet")
        print()
        try:
            print(f"Average number of spins per gain: {(number_of_spins/number_gains):.2f}")
            print(f"Average number of spins per loss: {(number_of_spins/number_losses):.2f}")
        except ZeroDivisionError:
            print(f"Average number of spins per gain: ZeroDivisionError")
            print(f"Average number of spins per loss: ZeroDivisionError")
        print(f"\nNumber of refills (${initial_wallet}): {number_refills}")


def printer(first_symbol, second_symbol, third_symbol):
    print(f"""
                 ||*|  {first_symbol}   |*|  {second_symbol}   |*|  {third_symbol}   |*||
    """)

def celebrator(prompt):

    for _ in range(random.randint(10, 40)):
        prompt += " "
    prompt += random.choice(["💵", "💸", "💰", "❤️"])

    print(prompt)

main()