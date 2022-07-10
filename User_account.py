class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f'''Interest Rate: {self.int_rate} Balance: {self.balance}''')
    def yield_interest(self):
        self.balance *= 1 + (self.int_rate / 100)
        return self
    @classmethod
    def print_all(cls):
        for account in cls.all_accounts:
            account.display_account_info()

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.accounts = [BankAccount(1.2,0)]
    
    def display_info(self):
        print(f'''\nFirst Name : {self.first_name}
Last Name : {self.last_name}
Email : {self.email}
Age: {self.age}''')
        if self.is_rewards_member:
            print(f'''Is a rewards card member with {self.gold_card_points} points\n''')
        else:
            print(f'''Not a rewards card member\n''')
        return self

    def enroll(self):
        if(self.is_rewards_member == True):
            print("User is already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 250
        return self
    
    def spend_points(self, amount):
        if(self.gold_card_points > amount):
            self.gold_card_points -= amount
        else:
            print("Not enough points to spend")
        return self

    def add_account(self):
        self.accounts.append(BankAccount(1.2, 0))
        return self

    def make_deposit(self, amount, account_number):
        self.accounts[account_number].deposit(amount)
        return self

    def make_withdrawl(self, amount, account_number):
        self.accounts[account_number].withdraw(amount)
        return self

    def display_user_balance(self):
        print(f'''{self.first_name} {self.last_name}''')
        for i in range(0, len(self.accounts)):
            print(f'''Account #{i+1}: ${self.accounts[i].balance}''')
        # for account in self.accounts:
        #     account.display_account_info()
        return self

    def transfer_money(self, account_number, to_account, amount):
        self.accounts[account_number].balance -= amount
        to_account.balance += amount

#test data
users = []
users.append(User("Joe", "Smith", "Smith@yahoo.com", 24))
users.append(User("Mary", "Jones", "Jones@gmail.com", 36))
users.append(User("Mike", "Winger", "Winger@outlook.com", 32))

#testing multiple accounts
print("Testing multiple accounts for user 0")
users[0].display_info()
users[0].add_account()
users[0].add_account()
users[0].make_deposit(100, 1)
users[0].make_deposit(300, 0)
users[0].make_deposit(100, 1)
users[0].make_deposit(400, 2)
users[0].make_deposit(50, 1)
users[0].display_user_balance()

#testing transfer money

print("\nTesting Money Transfer")

users[1].add_account()
users[1].add_account()
users[1].make_deposit(100, 2)

users[2].add_account()
users[2].make_deposit(400, 1)

print("*******User 1 Before Transfer ************")
users[1].display_user_balance()
print("*******User 2 Before Transfer ************")
users[2].display_user_balance()

users[2].transfer_money(1, users[1].accounts[2], 50)

print("*******User 1 After Transfer ************")
users[1].display_user_balance()
print("*******User 2 After Transfer ************")
users[2].display_user_balance()
