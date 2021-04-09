# 1
import random
import sqlite3


# class Bank:
#     cards_store = {}
#
#     def options(self, action):
#         if action == 1:
#             self.create_account()
#         elif action == 2:
#             self.login()
#
#     def create_account(self):
#         iin = 400000
#         customer_acc_number = random.randrange(100000000, 999999999)
#         checksum = 8
#         card_number = str(iin) + str(customer_acc_number) + str(checksum)
#         pin = str(random.randrange(1000, 9999))
#         n = len(self.cards_store) + 1
#         # print(len(self.cards_store))
#         self.cards_store[f"{n}"] = {"card_number": card_number, "pin": pin}
#         # print(self.cards_store)
#         print(f"""Your card has been created
# Your card number:
# {card_number}
# Your card PIN:
# {pin}""")
#
#     def login(self):
#         print("Enter your card number:")
#         card_number = input()
#         print("Enter your PIN:")
#         pin = input()
#         find = 0
#         for i in self.cards_store:
#             if card_number == self.cards_store[f"{i}"]["card_number"] and pin == self.cards_store[f"{i}"]["pin"]:
#                 # print(self.cards_store[f"{i}"])
#                 find = 1
#         if find == 1:
#             print("You have successfully logged in!")
#         else:
#             print("Wrong card number or PIN!!")
#
#
# bank_inst = Bank()
# while 1:
#     print("""1. Create an account
# 2. Log into account
# 0. Exit""")
#     action = int(input())
#     if action == 0:
#         break
#     else:
#         bank_inst.options(action)

# 2
# class Bank:
#     cards_store = {}
#
#     def __init__(self):
#         self.state = "logout"
#         self.balance = 0
#
#     def options(self, action):
#         if action == 1 and self.state == "logout":
#             self.create_account()
#         elif action == 2 and self.state == "logout":
#             self.login()
#         elif action == 1 and self.state == "login":
#             self.balance_check()
#         elif action == 2 and self.state == "login":
#             self.logout()
#
#     def create_account(self):
#         iin = 400000
#         customer_acc_number = random.randrange(100000000, 999999999)
#         pre_card_number = str(iin) + str(customer_acc_number)
#         pre_card_number = [int(x) * 2 if i % 2 == 0 else int(x) for i,x in enumerate(pre_card_number)]
#         pre_card_number = [int(x) - 9 if int(x) > 9 else int(x) for x in pre_card_number]
#         checksum = 10 - (sum(pre_card_number) % 10)
#         card_number = str(iin) + str(customer_acc_number) + str(checksum)
#         pin = str(random.randrange(1000, 9999))
#         n = len(self.cards_store) + 1
#         self.cards_store[f"{n}"] = {"card_number": card_number, "pin": pin}
#         # print(self.cards_store)
#         print(f"""Your card has been created
# Your card number:
# {card_number}
# Your card PIN:
# {pin}""")
#
#     def login(self):
#         print("Enter your card number:")
#         card_number = input()
#         print("Enter your PIN:")
#         pin = input()
#         find = 0
#         for i in self.cards_store:
#             if card_number == self.cards_store[f"{i}"]["card_number"] and pin == self.cards_store[f"{i}"]["pin"]:
#                 # print(self.cards_store[f"{i}"])
#                 find = 1
#         if find == 1:
#             print("You have successfully logged in!")
#             self.state = "login"
#         else:
#             print("Wrong card number or PIN!!")
#
#     def balance_check(self):
#         print(f"Balance: {self.balance}")
#
#     def logout(self):
#         print("You have successfully logged out!")
#
#
# bank_inst = Bank()
# while 1:
#     if bank_inst.state == "logout":
#         print("""1. Create an account
# 2. Log into account
# 0. Exit""")
#     else:
#         print("""1. Balance
# 2. Log out
# 0. Exit""")
#     action = int(input())
#     if action == 0:
#         break
#     else:
#         bank_inst.options(action)

# 3
# conn = sqlite3.connect('card.s3db')
#
# cur = conn.cursor()
#
# cur.execute('DROP TABLE IF EXISTS card;')
# cur.execute('CREATE TABLE card ( id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0 );')
# conn.commit()
#
#
# class Bank:
#
#     def __init__(self):
#         self.state = "logout"
#         self.current_card = []
#
#     def options(self, action):
#         if action == 1 and self.state == "logout":
#             self.create_account()
#         elif action == 2 and self.state == "logout":
#             self.login()
#         elif action == 1 and self.state == "login":
#             self.balance_check()
#         elif action == 2 and self.state == "login":
#             self.logout()
#
#     def create_account(self):
#         iin = 400000
#         customer_acc_number = random.randrange(100000000, 999999999)
#         pre_card_number = str(iin) + str(customer_acc_number)
#         pre_card_number = [int(x) * 2 if i % 2 == 0 else int(x) for i,x in enumerate(pre_card_number)]
#         pre_card_number = [int(x) - 9 if int(x) > 9 else int(x) for x in pre_card_number]
#         checksum = 10 - (sum(pre_card_number) % 10)
#         card_number = str(iin) + str(customer_acc_number) + str(checksum)
#         pin = str(random.randrange(1000, 9999))
#
#         cur.execute("INSERT INTO card(number, pin) VALUES(?, ?)", (card_number, pin))
#         conn.commit()
#
#         print(f"""Your card has been created
# Your card number:
# {card_number}
# Your card PIN:
# {pin}""")
#
#     def login(self):
#         print("Enter your card number:")
#         card_number = input()
#         print("Enter your PIN:")
#         pin = input()
#
#         cur.execute("select * from card where number=? and pin=?;", (card_number, pin))
#         conn.commit()
#         self.current_card = cur.fetchone()
#
#         if self.current_card:
#             print("You have successfully logged in!")
#             self.state = "login"
#         else:
#             print("Wrong card number or PIN!!")
#
#     def balance_check(self):
#         print(f"Balance: {self.current_card[3]}")
#
#     def logout(self):
#         self.current_card = []
#         print("You have successfully logged out!")
#
#
# bank_inst = Bank()
# while 1:
#     if bank_inst.state == "logout":
#         print("""1. Create an account
# 2. Log into account
# 0. Exit""")
#     else:
#         print("""1. Balance
# 2. Log out
# 0. Exit""")
#     action = int(input())
#     if action == 0:
#         break
#     else:
#         bank_inst.options(action)

# 4
conn = sqlite3.connect('card.s3db')

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS card;')
cur.execute('CREATE TABLE card ( id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0 );')
conn.commit()


class Bank:

    def __init__(self):
        self.state = "logout"
        self.current_card = []

    def options(self, action):
        if action == 1 and self.state == "logout":
            self.create_account()
        elif action == 2 and self.state == "logout":
            self.login()
        elif action == 1 and self.state == "login":
            self.balance_check()
        elif action == 2 and self.state == "login":
            self.add_income()
        elif action == 3 and self.state == "login":
            self.do_transfer()
        elif action == 4 and self.state == "login":
            self.close_account()
        elif action == 5 and self.state == "login":
            self.logout()

    def create_account(self):
        iin = 400000
        customer_acc_number = random.randrange(100000000, 999999999)
        pre_card_number = str(iin) + str(customer_acc_number)
        pre_card_number = [int(x) * 2 if i % 2 == 0 else int(x) for i, x in enumerate(pre_card_number)]
        pre_card_number = [int(x) - 9 if int(x) > 9 else int(x) for x in pre_card_number]
        reminder = sum(pre_card_number) % 10
        if reminder == 0:
            checksum = 0
        else:
            checksum = 10 - reminder
        card_number = str(iin) + str(customer_acc_number) + str(checksum)
        pin = str(random.randrange(1000, 9999))

        cur.execute("INSERT INTO card(number, pin) VALUES(?, ?)", (card_number, pin))
        conn.commit()

        print(f"""Your card has been created
Your card number:
{card_number}
Your card PIN:
{pin}""")

    def login(self):
        print("Enter your card number:")
        card_number = input()
        print("Enter your PIN:")
        pin = input()

        cur.execute("select * from card where number=? and pin=?;", (card_number, pin))
        conn.commit()
        self.current_card = cur.fetchone()

        if self.current_card:
            print("You have successfully logged in!")
            self.state = "login"
        else:
            print("Wrong card number or PIN!!")

    def balance_check(self):
        print(f"Balance: {self.current_card[3]}")

    def add_income(self):
        print("Enter income:")
        income = self.current_card[3] + int(input())
        cur.execute("UPDATE card SET balance=? where number=?;", (income, self.current_card[1]))
        conn.commit()
        cur.execute("select * from card where number=?;", (self.current_card[1],))
        conn.commit()
        self.current_card = cur.fetchone()
        print("Income was added!")

    def close_account(self):
        cur.execute("delete from card where id=?;", (self.current_card[0],))
        conn.commit()
        self.current_card = []
        print("The account has been closed!")
        self.state = "logout"

    def luhn_valid(self, card_number):
        checksum_input = int(card_number[-1])

        pre_card_number = card_number[0:15]
        pre_card_number = [int(x) * 2 if i % 2 == 0 else int(x) for i, x in enumerate(pre_card_number)]
        pre_card_number = [int(x) - 9 if int(x) > 9 else int(x) for x in pre_card_number]
        checksum_comp = 10 - (sum(pre_card_number) % 10)
        if checksum_input == checksum_comp:
            return True
        else:
            return False

    def do_transfer(self):
        print("""Transfer
Enter card number:""")
        card_number = input()
        valid = self.luhn_valid(card_number)
        print(valid)
        if not valid:
            print("Probably you made a mistake in the card number. Please try again!")
        else:
            cur.execute("select * from card where number=?;", (card_number,))
            conn.commit()
            exist = cur.fetchone()

            if not exist:
                print("Such a card does not exist.")
            elif card_number == self.current_card[1]:
                print("You can't transfer money to the same account!")
            else:
                print("Enter how much money you want to transfer:")
                money = int(input())
                if money > self.current_card[3]:
                    print("Not enough money!")
                else:
                    reminder = self.current_card[3] - money
                    cur.execute("UPDATE card SET balance=? where number=?;", (reminder, self.current_card[1]))
                    conn.commit()
                    cur.execute("select * from card where number=?;", (self.current_card[1],))
                    conn.commit()
                    self.current_card = cur.fetchone()

                    income = exist[3] + money
                    cur.execute("UPDATE card SET balance=? where number=?;", (income, exist[1]))
                    conn.commit()
                    print("Success!")

    def logout(self):
        self.current_card = []
        self.state = "logout"
        print("You have successfully logged out!")


bank_inst = Bank()
while 1:
    if bank_inst.state == "logout":
        print("""1. Create an account
2. Log into account
0. Exit""")
    else:
        print("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit""")
    action = int(input())
    if action == 0:
        print("Bye!")
        break
    else:
        bank_inst.options(action)
