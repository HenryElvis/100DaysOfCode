class User:
    
    def __init__(self, name):
        self.name = name
        self.following = 0
        self.follower = 0

    def follow(self, user):
        self.following += 1
        user.follower += 1

user = User("Elvis")
user_1 = User("Idriss")

user.follow(user_1)

print(user.following)
print(user_1.follower)

# class Car:

#     def __init__(self, seat):
#         self.seats = seat

#     def enter_race_mode(self):
#         self.seats = 4