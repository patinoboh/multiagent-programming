import random

class KupujemLacno:

    def __lt__(self, other):
        return self.name() < other.name()

    def __init__(self, num_strategies):
        self.num_strategies = num_strategies
        self.remaining_money = 0
        self.num_auctions = 0
        distrib_a = (100,200)
        distrib_b = (-50,50)
        self.samples = sorted([random.randint(distrib_a[0], distrib_a[1]) + random.randint(distrib_b[0], distrib_b[1]) for _ in range(num_strategies)])
        # self.comp

    # name of the strategy - make sure it is unique
    def name(self):
        return "KupujemLacno"

    # name of the author of the strategy
    def author(self):
        return "Patrik Brocek"

    # number of auctions that will be simulated - called before the first auction
    def set_num_auctions(self, num_auctions):
        self.num_auctions = num_auctions

    # amount of money available for all auctions - called before the first aution
    def set_money(self, money):
        self.remaining_money = money

    # called after winning an aution with the price that was paid for the object
    def won(self, price):
        self.remaining_money -= price

    # value of the object for this agent - called before every auction
    def set_value(self, value): 
        self.value = value

    # shows interest in the object for the current price, called in each iteration of each aution
    def interested(self, price, active_strats):
        if price > self.remaining_money:
            return False
    
        if price <= self.value:
            return True
        if self.remaining_money - self.value < 10: # za to uz by som si aj tak nic nekupil
            return True
        
        return False # mam love ale cena je vysoka

# Poznamky : 
# ak uz mi neostanu peniasky kupit dalsie tak kupim aj drahsie - NIE lebo M+V
# chces mat posledne miesto v sete
# nejak zobrat do uvahy aj active_strats
# to samplovanie neviem ci mi nejak pomoze
# pamatat si kolko som bol ochotny platit a nejak z toho nieco pocitat
# TODO dynamicky thresshold


def strategy_ascending(num_strategies):
    return KupujemLacno(num_strategies)

def strategy_descending(num_strategies):
    return KupujemLacno(num_strategies)