class Bill:
    """
    object that contains data of a bill
    Total amount and period of a bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    '''
    create a flatmate person who lives in the house and play the share
    of the bill
    '''

    def __init__(self, name, days_in_the_house):
        self.days_in_the_house = days_in_the_house
        self.name = name

    def pays(self, bill, flatmate2):
        total_days = self.days_in_the_house + flatmate2.days_in_the_house
        fraction = self.days_in_the_house / total_days
        return bill.amount * fraction