users = {}


class User:
    def __init__(self, user_name, email, password, last_login):
        self.user_name = user_name
        self.email = email
        self.password = self.encrypt(password, 5)
        self.last_login = last_login
        self.message = []

    def send_message(self, username, message):
        recipient = users[username]
        recipient.message.append(message)

    def encrypt(self, text, n):
        cipher = ""
        for char in text:
            if char == " ":
                cipher += char
            else:
                cipher += chr((ord(char) + n - 97) % 26 + 97)
        return cipher


user1 = User('key01', 'joe@gmail.com', 'nuh870p', '2017/09/09')
user2 = User('key02', 'key02@gmail.com', 'crjrf33', '2018/09/09')
users[user1.user_name] = user1
users[user2.user_name] = user2

print(users)

print(user1.message)

user2.send_message('key01', 'go fuck yourself')

print(user1.message)
print(user1.password)


