class Coffee:
    def __init__(self, water, milk, beans, cash):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cash = cash


class CoffeeMachine:
    espresso = Coffee(250, 0, 16, 4)
    latte = Coffee(350, 75, 20, 7)
    cappuccino = Coffee(200, 100, 12, 6)

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.cash = 550

    def take(self):
        print(f'\nI gave you ${self.cash}\n')
        self.cash = 0

    def fill(self):
        print(f'\nWrite how many ml of water do you want to add:')
        self.water += int(input())
        print(f'Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print(f'Write how many grams of coffee beans do you want to add:')
        self.beans += int(input())
        print(f'Write how many disposable cups of coffee do you want to add:\n')
        self.cups += int(input())

    def remaining(self):
        print(f'\nThe coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.beans} of coffee beans\n{self.cups} of disposable cups\n{self.cash} of money\n')

    def buy(self):
        i = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino,  back - to main menu:')
        if i == 'back':
            return True
        elif i == '1':
            self.change(self.espresso)
        elif i == '2':
            self.change(self.latte)
        elif i == '3':
            self.change(self.cappuccino)

    def change(self, name):
        if self.water > name.water:
            if self.milk > name.milk:
                if self.beans > name.beans:
                    if self.cups > 0:
                        print('I have enough resources, making you a coffee!\n')
                        self.water -= name.water
                        self.milk -= name.milk
                        self.beans -= name.beans
                        self.cups -= 1
                        self.cash += name.cash
                    else:
                        print(f'Sorry, not enough cups!\n')
                else:
                    print(f'Sorry, not enough beans!\n')
            else:
                print(f'Sorry, not enough milk!\n')
        else:
            print(f'Sorry, not enough water!\n')

    def actions(self, l):
        if l == 'buy':
            self.buy()
        elif l == 'fill':
            self.fill()
        elif l == 'take':
            self.take()
        elif l == 'remaining':
            self.remaining()
    def menu(self):
        print('Write action (buy, fill, take, remaining, exit):')
        action = input()
        while action != 'exit':
            self.actions(action)
            print('Write action (buy, fill, take, remaining, exit):')
            action = input()


coffee = CoffeeMachine()
coffee.menu()
