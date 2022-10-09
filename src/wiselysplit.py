from user import User


class WiseSplit:

    total_expenditure = 0

    def __init__(self) -> None:
        pass

    @staticmethod
    def logic(amount_paid):
        user_name_who_paid = amount_paid.split(':')[0]
        user_amount_paid = int(amount_paid.split(':')[1])

        User.get_user_id_by_name_and_update_amount_spent(user_name_who_paid, user_amount_paid)

        WiseSplit.total_expenditure += user_amount_paid

    @staticmethod
    def who_owes_what_to_whom():
        user_list = User.user_list
        
        for user in user_list:
            print(user.name)


    
