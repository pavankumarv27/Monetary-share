class User:

    count = 0
    user_list = []

    def __init__(self, name) -> None:
        self.name = name
        self.amount_in_bank = 0
        User.count += 1
        self.user_id = User.count
        User.user_list.append(self)
        print(User.user_list)
        self.owes_you = []
        self.you_owe = []

    @staticmethod
    def get_user_id_by_name_and_update_amount_spent(name, amount):
        for u in User.user_list:
            if u.name == name:
                u.credit_amount(amount)
                return u

    def credit_amount(self, amnt):
        self.amount_in_bank += amnt

    def debit_amount(self, dbt_amount, current_payer):
        self.amount_in_bank -= dbt_amount
        other_users = []
        for usr in User.user_list:
            if usr == current_payer:
                continue
            usr.you_owe.append((current_payer, dbt_amount))
            other_users.append(usr)
        for u in other_users:
            current_payer.owes_you((u, dbt_amount))

if __name__ == "__main__":
    pass
