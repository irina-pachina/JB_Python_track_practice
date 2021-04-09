# Program prints a menu where a user can choose to buy a coffee, fill up the machine, take out a cash,
# check the remaining ingredients or exit.
# Class CoffeeMachine has a method that takes a string as input. Every time the user inputs a string to the console,
# the program invokes this method with one argument. Program stores the current state of the machine
# to handle inputs for different purposes.

class CoffeeMachine:

    def __init__(self):
        self.water_left = 400
        self.milk_left = 540
        self.beans_left = 120
        self.cups_left = 9
        self.money_left = 550
        self.choosing_a_type_of_coffee = False

    def options(self, action):
        if self.choosing_a_type_of_coffee or action == "buy":
            return self.buy(action)
        elif action == "fill":
            self.fill(action)
        elif action == "take":
            self.take(action)
        elif action == "remaining":
            self.leftovers(action, 0, 0, 0, 0, 0)

    def leftovers(self, action, water, milk, beans, cups, money):
        if action == "buy":
            self.water_left -= water
            self.milk_left -= milk
            self.beans_left -= beans
            self.cups_left -= cups
            self.money_left += money
        elif action == "fill":
            self.water_left += water
            self.milk_left += milk
            self.beans_left += beans
            self.cups_left += cups
        elif action == "take":
            self.money_left = 0
        elif action == "remaining":
            print(f"""The coffee machine has:
            {self.water_left} of water
            {self.milk_left} of milk
            {self.beans_left} of coffee beans
            {self.cups_left} of disposable cups
            {self.money_left} of money""")

    def buy(self, action):
        if not self.choosing_a_type_of_coffee:
            self.choosing_a_type_of_coffee = True
            return True
        else:
            self.choosing_a_type_of_coffee = False
            if action == "back":
                return
            elif int(action) == 1:
                if self.water_left < 250:
                    print("Sorry, not enough water!")
                elif self.beans_left < 16:
                    print("Sorry, not enough beans!")
                elif self.cups_left < 1:
                    print("Sorry, not enough cups!")
                else:
                    print("I have enough resources, making you a coffee!")
                    self.leftovers("buy", 250, 0, 16, 1, 4)
            elif int(action) == 2:
                if self.water_left < 350:
                    print("Sorry, not enough water!")
                elif self.milk_left < 75:
                    print("Sorry, not enough milk!")
                elif self.beans_left < 20:
                    print("Sorry, not enough beans!")
                elif self.cups_left < 1:
                    print("Sorry, not enough cups!")
                else:
                    print("I have enough resources, making you a coffee!")
                    self.leftovers("buy", 350, 75, 20, 1, 7)
            elif int(action) == 3:
                if self.water_left < 200:
                    print("Sorry, not enough water!")
                elif self.milk_left < 100:
                    print("Sorry, not enough milk!")
                elif self.beans_left < 12:
                    print("Sorry, not enough beans!")
                elif self.cups_left < 1:
                    print("Sorry, not enough cups!")
                else:
                    print("I have enough resources, making you a coffee!")
                    self.leftovers("buy", 200, 100, 12, 1, 6)

    def fill(self, action):
        print("Write how many ml of water do you want to add:")
        water_add = int(input())
        print("Write how many ml of milk do you want to add:")
        milk_add = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        beans_add = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        cups_add = int(input())
        self.leftovers(action, water_add, milk_add, beans_add, cups_add, 0)

    def take(self, action):
        print(f"I gave you {self.money_left}")
        self.leftovers(action, 0, 0, 0, 0, 0)


coffee_machine = CoffeeMachine()
print("Write action (buy, fill, take, remaining, exit):")
while 1:
    action = input()
    if action == "exit":
        break
    elif coffee_machine.options(action):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    else:
        print("Write action (buy, fill, take, remaining, exit):!")
