# Template, self - is a reference to the current instance of class 
class User:
    uname = 'admin'

    def __init__(self, name, age):
        self.name = name
        self.age=age

    def showName(self):
        print("Name is Provided")

# create an object
user = User("check", 30)
print(user.uname, user.name, user.age)
user.showName()