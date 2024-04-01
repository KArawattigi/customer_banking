""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance: float, interest: float):
        self.__balance = balance
        self.__interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance:float):
        """Sets the balance for the for the account"""
        self.__balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest:float):
        """Sets the interest gained for the the account"""
        self.__interest = interest

    #defining getters instead of direct access to class attributes 
    def get_balance(self):
        return self.__balance
    
    def get_interest(self):
        return self.__interest
