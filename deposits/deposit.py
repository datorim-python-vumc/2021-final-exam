class Deposit:

    def __init__(self, deposit, term, rate):
        self.deposit = deposit
        self.term = term
        self.rate = rate

    # for loop if don't know the formula
    def interest(self):
        amount_end_of_term = self.deposit * (1 + self.rate) ** self.term
        interest = amount_end_of_term - self.deposit

        return interest
