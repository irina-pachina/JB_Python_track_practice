# 1
# print("""Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!""")

# 2
# print("Write how many cups of coffee you will need:")
# number = int(input())
# water_dose = 200
# milk_dose = 50
# beans_dose = 15
# print(f"""For 25 cups of coffee you will need:
# {water_dose * number} ml of water
# {milk_dose * number} ml of milk
# {beans_dose * number} g of coffee beans""")

# 3
# print("Write how many ml of water the coffee machine has:")
# water_left = int(input())
# print("Write how many ml of milk the coffee machine has:")
# milk_left = int(input())
# print("Write how many grams of coffee beans the coffee machine has:")
# beans_left = int(input())
# print("Write how many cups of coffee you will need:")
# number = int(input())
#
# water_dose = 200
# milk_dose = 50
# beans_dose = 15
#
# # water_need = water_dose * number
# # milk_need = milk_dose * number
# # beans_need = beans_dose * number
#
# water_can = water_left // water_dose
# milk_can = milk_left // milk_dose
# beans_can = beans_left // beans_dose
#
# N = min(water_can, milk_can, beans_can)
#
# if N == number:
#     print("Yes, I can make that amount of coffee")
# elif N > number:
#     print(f"Yes, I can make that amount of coffee (and even {N - number} more than that)")
# elif N < number:
#     print(f"No, I can make only {N} cups of coffee")

# 4
# water_left = 400
# milk_left = 540
# beans_left = 120
# cups_left = 9
# money_left = 550
#
#
# def leftovers(action, water, milk, beans, cups, money):
#     global water_left, milk_left, beans_left, cups_left, money_left
#     if action == "buy":
#         water_left -= water
#         milk_left -= milk
#         beans_left -= beans
#         cups_left -= cups
#         money_left += money
#     elif action == "fill":
#         water_left += water
#         milk_left += milk
#         beans_left += beans
#         cups_left += cups
#     elif action == "take":
#         money_left = 0
#     print(f"""The coffee machine has:
#     {water_left} of water
#     {milk_left} of milk
#     {beans_left} of coffee beans
#     {cups_left} of disposable cups
#     {money_left} of money""")
#
#
# def buy(action):
#     print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
#     coffee_style = int(input())
#     if coffee_style == 1:
#         leftovers(action, 250, 0, 16, 1, 4)
#     elif coffee_style == 2:
#         leftovers(action, 350, 75, 20, 1, 7)
#     elif coffee_style == 3:
#         leftovers(action, 200, 100, 12, 1, 6)
#
#
# def fill(action):
#     print("Write how many ml of water do you want to add:")
#     water_add = int(input())
#     print("Write how many ml of milk do you want to add:")
#     milk_add = int(input())
#     print("Write how many grams of coffee beans do you want to add:")
#     beans_add = int(input())
#     print("Write how many disposable cups of coffee do you want to add:")
#     cups_add = int(input())
#     leftovers(action, water_add, milk_add, beans_add, cups_add, 0)
#
#
# def take(action):
#     print(f"I gave you {money_left}")
#     leftovers(action, 0, 0, 0, 0, 0)
#
#
# leftovers("buy", 0, 0, 0, 0, 0)
#
# print("Write action (buy, fill, take):")
# action = input()
#
# if action == "buy":
#     buy(action)
# elif action == "fill":
#     fill(action)
# elif action == "take":
#     take(action)

# 5
# water_left = 400
# milk_left = 540
# beans_left = 120
# cups_left = 9
# money_left = 550
#
#
# def leftovers(action, water, milk, beans, cups, money):
#     global water_left, milk_left, beans_left, cups_left, money_left
#     if action == "buy":
#         water_left -= water
#         milk_left -= milk
#         beans_left -= beans
#         cups_left -= cups
#         money_left += money
#     elif action == "fill":
#         water_left += water
#         milk_left += milk
#         beans_left += beans
#         cups_left += cups
#     elif action == "take":
#         money_left = 0
#     elif action == "remaining":
#         print(f"""The coffee machine has:
#         {water_left} of water
#         {milk_left} of milk
#         {beans_left} of coffee beans
#         {cups_left} of disposable cups
#         {money_left} of money""")
#
#
# def buy(action):
#     print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
#     coffee_style = input()
#     if coffee_style == "back":
#         return
#     elif int(coffee_style) == 1:
#         if water_left < 250:
#             print("Sorry, not enough water!")
#         elif beans_left < 16:
#             print("Sorry, not enough beans!")
#         elif cups_left < 1:
#             print("Sorry, not enough cups!")
#         else:
#             print("I have enough resources, making you a coffee!")
#             leftovers(action, 250, 0, 16, 1, 4)
#     elif int(coffee_style) == 2:
#         if water_left < 350:
#             print("Sorry, not enough water!")
#         elif milk_left < 75:
#             print("Sorry, not enough milk!")
#         elif beans_left < 20:
#             print("Sorry, not enough beans!")
#         elif cups_left < 1:
#             print("Sorry, not enough cups!")
#         else:
#             print("I have enough resources, making you a coffee!")
#             leftovers(action, 350, 75, 20, 1, 7)
#     elif int(coffee_style) == 3:
#         if water_left < 200:
#             print("Sorry, not enough water!")
#         elif milk_left < 100:
#             print("Sorry, not enough milk!")
#         elif beans_left < 12:
#             print("Sorry, not enough beans!")
#         elif cups_left < 1:
#             print("Sorry, not enough cups!")
#         else:
#             print("I have enough resources, making you a coffee!")
#             leftovers(action, 200, 100, 12, 1, 6)
#
#
# def fill(action):
#     print("Write how many ml of water do you want to add:")
#     water_add = int(input())
#     print("Write how many ml of milk do you want to add:")
#     milk_add = int(input())
#     print("Write how many grams of coffee beans do you want to add:")
#     beans_add = int(input())
#     print("Write how many disposable cups of coffee do you want to add:")
#     cups_add = int(input())
#     leftovers(action, water_add, milk_add, beans_add, cups_add, 0)
#
#
# def take(action):
#     print(f"I gave you {money_left}")
#     leftovers(action, 0, 0, 0, 0, 0)
#
#
# while 1:
#     print("Write action (buy, fill, take, remaining, exit):")
#     action = input()
#
#     if action == "buy":
#         buy(action)
#     elif action == "fill":
#         fill(action)
#     elif action == "take":
#         take(action)
#     elif action == "remaining":
#         leftovers(action, 0, 0, 0, 0, 0)
#     elif action == "exit":
#         break

# 6
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
            self.buy(action)
        elif action == "fill":
            self.fill(action)
        elif action == "take":
            self.take(action)
        elif action == "remaining":
            self.leftovers(action, 0, 0, 0, 0, 0)
        # elif action == "exit":
        #     exit

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
                    self.leftovers(action, 250, 0, 16, 1, 4)
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
                    self.leftovers(action, 350, 75, 20, 1, 7)
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
                    self.leftovers(action, 200, 100, 12, 1, 6)

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
        print("Write action (buy, fill, take, remaining, exit):")

