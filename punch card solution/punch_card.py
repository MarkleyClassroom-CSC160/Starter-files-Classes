# punch_card.py
# The Daily Grind's punch card program. The PunchCard class is in punch_card_tools.py.

from punch_card_tools import PunchCard

cards = [PunchCard("Ava"), PunchCard("Marco"), PunchCard("Jin")]

print("Welcome to The Daily Grind!")
choice = ""
while choice != "quit":
    print()
    choice = input("What would you like to do? (buy / redeem / cards / quit): ").strip().lower()

    if choice == "buy" or choice == "redeem":
        name = input("Whose card? ").strip().lower()
        matched = False
        for card in cards:
            if card.name.lower() == name:
                matched = True
                if choice == "buy":
                    card.buy_drink()
                    if card.free_drink_ready():
                        print("Good news:", card.name, "has a free drink ready!")
                elif card.redeem():
                    print(card.name, "redeemed a FREE drink. Enjoy!")
                else:
                    print(card.name, "needs", card.punches_needed(), "more punches for a free drink.")
        if not matched:
            print("There's no card for that name.")
    elif choice == "cards":
        for card in cards:
            print(card)
    elif choice != "quit":
        print("Please type buy, redeem, cards, or quit.")

# end of the day report
total = 0
for card in cards:
    total = total + card.drinks_bought
print()
print("End of day: The Daily Grind sold", total, "drinks.")
