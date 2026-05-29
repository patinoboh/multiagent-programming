import random

class Base:

    def __lt__(self, other):
        return self.name() < other.name()
    
    def __init__(self, num_strategies):
        self.num_strategies = num_strategies
        self.remaining_money = 0
        self.num_auctions = 0
        self.auctions_left = 0

    def name(self):
        return "Base class"

    def author(self):
        return "Patrik Broček"

    def set_num_auctions(self, num_auctions):
        self.num_auctions = num_auctions
        self.auctions_left = num_auctions

    def set_money(self, money):
        self.remaining_money = money

    def won(self, price):
        self.remaining_money -= price

    def set_value(self, value):
        self.value = value
        self.auctions_left -= 1

    def target_spend_per_auction(self):
        if self.auctions_left <= 0:
            return 0
        return self.remaining_money / self.auctions_left

    def phase(self):
        if self.num_auctions == 0:
            return 0
        return self.auctions_left / self.num_auctions

    def competition_factor(self):
        return 1 + 0.15 * (self.num_strategies - 1)


# ENGLISH AUCTION

class EnglishStrategy(Base):
    def name(self):
        return "Patino English best"

    def compute_threshold(self, price, active_strats):
        t = self.target_spend_per_auction()
        phase = self.phase()

        # base threshold
        threshold = 0.7 * t * phase

        # competition makes us more conservative
        threshold *= self.competition_factor()

        # fewer players left → closer to final → relax
        if active_strats > 0:
            threshold *= (active_strats / self.num_strategies)

        # panic mode: too much money left
        if self.remaining_money > self.auctions_left * 150:
            threshold *= 0.6

        # broke mode: very little money
        if self.remaining_money < 100:
            threshold *= 1.5

        # endgame: spend it
        if self.auctions_left < 50:
            threshold *= 0.3

        return threshold

    def interested(self, price, active_strats):
        if price > self.remaining_money:
            return False

        margin = self.value - price
        threshold = self.compute_threshold(price, active_strats)

        return margin >= threshold


# DUTCH AUCTION

class DutchStrategy(Base):

    def name(self):
        return "Patino Dutch best"

    def compute_threshold(self):
        t = self.target_spend_per_auction()
        phase = self.phase()

        # base threshold
        threshold = 0.6 * t * phase

        threshold /= self.competition_factor()

        # threshold += random.uniform(0, 10)

        # panic mode - too much money left
        if self.remaining_money > self.auctions_left * 150:
            threshold *= 0.7

        # broke mode
        if self.remaining_money < 100:
            threshold *= 1.5

        # endgame - buy aggressively
        if self.auctions_left < 50:
            threshold *= 0.3

        return threshold

    def interested(self, price, active_strats):
        if price > self.remaining_money:
            return False

        threshold = self.compute_threshold()
        target_price = self.value - threshold

        return price <= target_price


def strategy_ascending(num_strategies):
    return EnglishStrategy(num_strategies)


def strategy_descending(num_strategies):
    return DutchStrategy(num_strategies)