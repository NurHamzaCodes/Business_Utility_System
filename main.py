class ExpenseManager:
    def __init__(self):
        self.dic = {}

    def add_expense(self):
        name = input("\nExpense: ")
        amount = int(input("Amount: "))

        self.dic.update({name:amount})
        print("\nExpense added successfully.",end="")

    def show_expenses(self):
        print("\nExpenses\n"+20*"-")
        for key, value in self.dic.items():
            print(key,end="")
            length = 18-(len(key)+len(str(value)))
            print(length*" ",+value)

    def show_total(self):
        count =0
        print()
        for key, value in self.dic.items():
            print(key,end="")
            length = 18-(len(key)+len(str(value)))
            print(length*" ",+value)
            count += value

        length = 13-len(str(count))
        print(20*"-" + "\nTotal" + length*" ", count)

def opening():
    print(5*"="+" Business Utility System "+5*"=")
    print("\n1. Expense Manager\n2. Exit\n")
    return int(input("Choose: "))

if __name__ == "__main__":
    while True:
        choose1 = opening()

        if choose1 == 1:
            manager = ExpenseManager()

            while True:
                print("\n\n"+5*"="+" Expense Manager "+5*"=")
                print("\n1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Back\n")

                choose2 = int(input("Choose: "))

                match choose2:
                    case 1:
                        manager.add_expense()

                    case 2:
                        manager.show_expenses()

                    case 3:
                        manager.show_total()

                    case 4:
                        print()
                        break

        elif choose1 == 2:
            print("\nThank you!\n")
            break