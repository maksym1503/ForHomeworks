class Customer:
    last_id = 0

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.customer_id = Customer.last_id

    def __repr__(self):
        return 'Customer[{0}, {1}, {2}]'.format(self.customer_id, self.first_name, self.last_name)


class Account:
    last_id = 0

    def __init__(self, customer):
        self.customer = customer
        self._balance = 0
        Account.last_id += 1
        self.account_id = Account.last_id
        self.interest_rate = 0.01

    def deposit(self, amount):
        #TODO - add validation to prevent misuse
        self._balance += amount
        if self._balance < 0:
            raise ValueError('Not available for negative values')  ### Worked! Easy check by c = Customer('John', 'Brown', 'john@brown.com') a1 = Account(c) a1.deposit(-100.08)

    def charge(self, amount):
        #TODO - add validation to prevent misuse
        self._balance -= amount
        if self._balance < 0:
            raise ValueError('Not available for negative values')
    def get_balance(self):
        return self._balance

    def calc_interest(self, amount):
        #TODO - add implementation based on self.interest_rate
        self.interest_rate -= amount

    def __repr__(self):
        return 'Account[{0}, {1}, {2}, {3}, {4}]'.format(self.account_id, self.customer.customer_id, self.customer.last_name, self._balance, self.interest_rate)


class Bank:
    def __init__(self):
        self._accounts = []
        self._customers = []

    def create_customer(self, first_name, last_name, email):
        c = Customer(first_name, last_name, email)
        self._customers.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self._accounts.append(a)
        return a


    def transfer(self, acc_from, acc_to, amount):
        #TODO - implement it
        from_account.deposit(amount)
        to_account.deposit(amount)
        # I spent a lot of time working in the direction above, but failed to find a solution.
        # However, I believe I was pretty close to the solution.

    def __str__(self):
        return 'Bank[{0}, {1}]'.format(self._customers, self._accounts)