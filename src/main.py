from ops import convert_string_to_dict
from user import User
from wiselysplit import WiseSplit


def main():
    no_of_people = input('Enter number of people: ')

    for i in range(int(no_of_people)):
        User(input(f'Enter name of person {i}: '))

    wise_split_mode = True
    while wise_split_mode:
        user_option = int(input(
            "Enter option:\n1. someone paid\n2. Check total amount spent in the trip\n3. Who owes what to whom\n4. Exit\n\nYour choice: "))
        if user_option == 1:
            statement = input('Who paid how much? format - <name>:<amount>: ')
            WiseSplit.logic(statement)
        elif user_option == 2:
            print("Total amount spent in this trip: ", WiseSplit.total_expenditure, "\n")
        elif user_option == 3:
            pass
        else:
            break


if __name__ == "__main__":
    main()
