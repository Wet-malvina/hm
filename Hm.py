class User():
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__acces = "user"


    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_acces(self):
        return self.__acces

    def set_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__acces = 'admn'

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f'работник добавлен в список')
        print(user_list)

    def remove_user(self, user_list, user ):
        user_list.remove(user)
        print(f'работник удален из списка')
        print(user_list)


users = []
user1 = User ("11", "Кирилл")
user2 = User('12', 'Марина')
user3 = User('13', 'Карина')
user4 = User('14', 'Виктория')
admin = Admin('123', 'Дима')

print(user1.get_id())
print(user3.get_name())


admin.add_user(users, user1)
admin.add_user(users, user2)
admin.add_user(users, user3)
admin.add_user(users, user4)

admin.remove_user(users, user3)
