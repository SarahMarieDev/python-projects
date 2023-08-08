class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "sarah")
user_2 = User("002", "dustin")

user_1.follow(user_2)
user_2.follow(user_1)
print(f"{user_1.username} has {user_1.followers} followers and is following {user_1.following}.")
print(f"{user_2.username} has {user_2.followers} followers and is following {user_2.following}.")

