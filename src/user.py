class User:

    count = 0
    user_list = []

    def __init__(self, name) -> None:
        self.name = name
        self.amount_spent = 0
        User.count += 1
        self.user_id = User.count
        User.user_list.append(self)
        print(User.user_list)

    @staticmethod
    def get_user_id_by_name_and_update_amount_spent(name, amount):
        for u in User.user_list:
            if u.name == name:
                u.amount_spent += amount
                return u.user_id

    def credit_amount():
        pass

    def debit_memo():
        pass


if __name__ == "__main__":
    pass
