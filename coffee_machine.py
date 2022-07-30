class CoffeeMachine:
    def __init__(self):
        self.have = {'money': 550, 'water': 400, 'milk': 540, 'beans': 120, 'cups': 9}
        self.drink = {'espresso': {'money': -4, 'water': 250, 'beans': 16, 'cups': 1},
                      'latte': {'money': -7, 'water': 350, 'milk': 75, 'beans': 20, 'cups': 1},
                      'cappuccino': {'money': -6, 'water': 200, 'milk': 100, 'beans': 12, 'cups': 1}}
        self.action = None

    def buy(self):
        self.action = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
        if self.action == 'back':
            self.option()
        else:
            for k, v in self.drink[list(self.drink.keys())[int(self.action)-1]].items():
                if v > self.have[k]:
                    print(f'Sorry, not enough {k}!\n')
                    self.option()
        for k, v in self.drink[list(self.drink.keys())[int(self.action)-1]].items():
            self.have[k] -= v
        print('I have enough resources, making you a coffee!\n'), self.option()

    def fill(self):
        self.have['water'] += int(input('\nWrite how many ml of water you want to add:\n'))
        self.have['milk'] += int(input('Write how many ml of milk you want to add:\n'))
        self.have['beans'] += int(input('Write how many grams of coffee beans you want to add:\n'))
        self.have['cups'] += int(input('Write how many disposable cups you want to add:\n'))
        print(), self.option()

    def option(self):
        self.action = input('Write action (buy, fill, take, remaining, exit):\n')
        exit() if self.action == 'exit' else getattr(self, self.action)()

    def remaining(self):
        print('\nThe coffee machine has:', f"{self.have['water']} ml of water",
              f"{self.have['milk']} ml of milk", f"{self.have['beans']} g of coffee beans",
              f"{self.have['cups']} disposable cups", f"${self.have['money']} of money\n", sep='\n')
        self.option()

    def take(self):
        print(f"I gave you ${self.have['money']}\n")
        self.have['money'] = 0
        self.option()


machine = CoffeeMachine()
machine.option()
