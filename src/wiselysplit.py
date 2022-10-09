from user import User


class WiseSplit:

    total_expenditure = 0
    user_list = User.user_list

    def __init__(self) -> None:
        pass

    @staticmethod
    def logic(amount_paid):
        user_name_who_paid = amount_paid.split(':')[0]
        user_amount_paid = round(int(amount_paid.split(':')[1]))

        WiseSplit.who_owes_what_to_whom(user_name_who_paid, user_amount_paid)

        # User.get_user_id_by_name_and_update_amount_spent(user_name_who_paid, user_amount_paid)

        WiseSplit.total_expenditure += user_amount_paid

    @staticmethod
    def who_owes_what_to_whom(usr, amount_paid):

        current_payer = User.get_user_id_by_name_and_update_amount_spent(usr, amount_paid)

        debit_money = round(amount_paid/len(WiseSplit.user_list))

        for u in WiseSplit.user_list:
            if u.name == current_payer.name:
                continue
            u.debit_amount(debit_money, current_payer)
            


        
        

    
    
