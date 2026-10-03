# punch_card_tools.py
# The PunchCard class for The Daily Grind's loyalty program.
# punch_card.py imports it from this file.

PUNCHES_FOR_FREE = 8


class PunchCard:
    def __init__(self, name):
        self.name = name
        self.punches = 0
        self.drinks_bought = 0

    def buy_drink(self):
        self.punches = self.punches + 1
        self.drinks_bought = self.drinks_bought + 1
        print(self.name, "bought a drink and got a punch.")

    def free_drink_ready(self):
        return self.punches >= PUNCHES_FOR_FREE

    def punches_needed(self):
        needed = PUNCHES_FOR_FREE - self.punches
        if needed < 0:
            needed = 0
        return needed

    def redeem(self):
        if self.free_drink_ready():
            self.punches = self.punches - PUNCHES_FOR_FREE
            return True
        return False

    def __str__(self):
        shown = self.punches
        if shown > PUNCHES_FOR_FREE:
            shown = PUNCHES_FOR_FREE
        card = "[" + "X" * shown + "." * (PUNCHES_FOR_FREE - shown) + "]"
        status = ""
        if self.free_drink_ready():
            status = "  FREE DRINK READY"
        return f"{self.name:<10} {card} {self.punches:>2}/{PUNCHES_FOR_FREE}{status}"
