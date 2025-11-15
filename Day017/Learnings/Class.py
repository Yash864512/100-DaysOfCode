class User:  # Syntax to create an empty class
    pass     # The pass statement is used as a placeholder for future code


user1 = User()  # Creating an object of User class
user1.id = "001"  # Assigning values to user1 object attributes
user1.name = "Yaswanth"
user1.followers = 0

print(f"Your id: {user1.id}, your name: {user1.name} and your follower count: {user1.followers}")

user2 = User()
user2.id = "002"
user2.name = "Johnny"
user2.followers = 0

'''The issue in the above section is that after creating each object, we had to manually
initialize every attribute (id, name, followers). To streamline this process, we use the __init__
method, which allows us to pass parameters during object creation and automatically assign them
to the corresponding attributes.'''


class Account:
    def __init__(self, id, username, followers):
        self.user_id = id
        self.user_name = username
        self.followers = 0  # Initializing in the constructor itself
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# Initializing an Account instance(object) with constructor parameters
account_user1 = Account("001", "mehh_yash", 0)
account_user2 = Account("002", "johnnydepp", 0)
print(f"Your id: {account_user1.user_id}, your username: {account_user1.user_name} and your follower: {account_user1.followers}")

account_user1.follow(account_user2)
'''User1 decides to follow user2, then user1 following list increases and user2 followers list 
increases. Here in follow function in Account class, self = account_user1 and user parameter = 
account_user2'''
print(account_user1.followers)
print(account_user1.following)
print(account_user2.followers)
print(account_user2.following)
