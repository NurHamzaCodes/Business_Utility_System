class ExpenseManager:
    def __init__(self):
        self.dic = {}
        self.count = 1

    def add_expense(self):
        name = input("\nExpense: ")
        try:
            amount = int(input("Amount: "))

        except:
            print("\nAmount are only number\nExpense added failed!")

        else:
            if amount > 0:
                self.dic.update({f"{self.count}. {name}":amount})
                self.count += 1
                print("\nExpense added successfully.",end="")

            else:
                print("\nAmount are only positive\nExpense added failed!")


    def show_expenses(self):
        print("\nExpenses\n"+20*"-")
        if self.dic != {}:
            for key, value in self.dic.items():
                name = key.split(". ", 1)[1]
                print(name,end="")
                length = 18-(len(name)+len(str(value)))
                print(length*" ", value)

        else:
            print("No expense added!")

    def show_total(self):
        count =0
        print()
        if self.dic != {}:
            for key, value in self.dic.items():
                name = key.split(". ", 1)[1]
                print(name,end="")
                length = 18-(len(name)+len(str(value)))
                print(length*" ", value)
                count += value

            length = 13-len(str(count))
            print(20*"-" + "\nTotal" + length*" ", count)

        else:
            print("No expense added!")

def opening():
    print(5*"="+" Business Utility System "+5*"=")
    print("\n1. Expense Manager\n2. Exit\n")
    return int(input("Choose: "))

if __name__ == "__main__":
    manager = ExpenseManager()

    while True:
        choose1 = opening()

        if choose1 == 1:

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

        else:
            print("\nInvaild Choise!!\n")