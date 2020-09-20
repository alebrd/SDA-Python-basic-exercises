class User:
    def __init__(self, name):
        self.name = name
        self.__password = ''

    @property
    def password(self):
        if len(self.__password) == 0:
            return ''
        secret = self.__password[0]
        for i in range(len(self.__password) - 2):
            secret += '*'
        secret += self.__password[-1]
        return secret

    @password.setter
    def password(self, new_password):
        if len(new_password) < 6:
            while len(new_password) <= 6:
                new_password += '#'
        self.__password = new_password

    @password.deleter
    def password(self):
        del self.__password


u = User("Roccetta")
u.password = "s"
print(u.password)
u.password = "L0nger passwords ArE M0r3 Secure 0r s0 th3y s@y!"
print(u.password)
