class Login:
    def __init__(self):
        self.username = "admin"
        self.password = "admin123"

    def authenticate(self, user, pwd):
        if user == self.username and pwd == self.password:
            print("Login successful")
        else:
            print("Invalid username or password")
