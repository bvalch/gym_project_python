class Member:
    def __init__(self,first_name,last_name,sex,wallet,premium=False, id=None):
        self.first_name=first_name
        self.last_name=last_name
        self.sex=sex
        self.premium=premium
        self.wallet=wallet
        self.id=id