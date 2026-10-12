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
            if amount >= 0:

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


    def delete(self):
        print("\nExpenses\n"+20*"-")
        count = 1

        if self.dic != {}:
            
            for key, value in self.dic.items():
                name = str(count)+". "+key.split(". ", 1)[1]
                print(name,end="")
                length = 18-(len(name)+len(str(value)))
                print(length*" ", value)
                count += 1

        else:
            print("No expense added!") 


        try:
            n = int(input("\nChoose Expense you want to delete: "))

        except:
            print("\nNumber only!\nExpense Delete Failed!")

        else:
            try:
                del self.dic[list(self.dic.keys())[n-1]]

            except:
                print(f"\nExpense No: {n} Never Exist!\nExpense Delete Failed!")

            else:
                print("\nExpense Delete Successfully!")


    def edit(self):
        print("\nExpenses\n"+20*"-")
        count = 1
        
        if self.dic != {}:
                    
            for key, value in self.dic.items():
                name = str(count)+". "+key.split(". ", 1)[1]
                print(name,end="")
                length = 18-(len(name)+len(str(value)))
                print(length*" ", value)
                count += 1

            try:
                    n = int(input("\nChoose Expense you want to edit: "))
                    
            except:
                    print("\nNumber only!\nExpense Edit Failed!")
                    
            else:
                if n > len(self.dic.keys()):
                    print(f"\nExpense No: {n} Never Exist!\nExpense Edit Failed!")
            
                else:
                    try:
                        choose3 = int(input("\nWhat is need to change:\n\t1. Expense name\n\t2. Amount\nChoose: "))

                    except:
                        print("\nNumber only!\nExpense Edit Failed!")

                    else:
                        if choose3 == 1:
                            new_dic = {}
                            name = input("\nGive new name: ")

                            for k,v in self.dic.items():
                                if k == list(self.dic.keys())[n-1]:
                                    k = str(k.split(". ", 1)[0])+". "+name

                                new_dic.update({k:v})

                            self.dic = new_dic

                        elif choose3 == 2:
                            try:
                                amount = int(input("\nGive new amount: "))

                            except:
                                print("\nNumber only!\nExpense Edit Failed!")

                            else:
                                if amount < 0:
                                    print("\nAmount are only positive\nExpense edit failed!")

                                else:
                                    self.dic[list(self.dic.keys())[n-1]] = amount

                        else:
                            print("\nInvaild Choice!\nExpense Edit Failed!")
        
        else:
            print("\nNo expense added!") 
        
        
def opening():
    print(5*"="+" Business Utility System "+5*"=")
    print("\n1. Expense Manager\n2. Exit\n")
    
    try:
        choose1 = int(input("Choose: "))

    except:
        print("\nonly number!\n")
        return opening()

    else:
        if choose1 in [1,2]:
            return choose1

        else:
            print("\nInvaild Choice!")
            return opening()

if __name__ == "__main__":
    manager = ExpenseManager()

    while True:
        choose1 = opening()

        if choose1 == 1:

            while True:
                print("\n\n"+5*"="+" Expense Manager "+5*"=")
                print("\n1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Edit Expense\n5. Delete Expense\n6. Back\n")

                try:
                    choose2 = int(input("Choose: "))

                except:
                    print("\nNumber only!")

                else:
                    if choose2 in [1,2,3,4,5,6]:
                        match choose2:
                            case 1:
                                manager.add_expense()

                            case 2:
                                manager.show_expenses()

                            case 3:
                                manager.show_total()

                            case 4:
                                manager.edit()

                            case 5:
                                manager.delete()

                            case 6:
                                print()
                                break

                    else:
                        print("\nInvaild Chioce!")

        elif choose1 == 2:
            print("\nThank you!\n")
            break
