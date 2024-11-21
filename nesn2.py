


class Test():
    def publick_func(self):
        print('Публичный метод')

    def _protected_func(self):
        print('защищенный метод')

    def __private_func(self):
        print('Приватный метод')

    def test_private(self):
        self.__private_func()

test = Test()

test.publick_func()

test._protected_func()

test.test_private()