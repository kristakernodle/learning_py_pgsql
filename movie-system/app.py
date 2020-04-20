from user import User

# user = User("Krista")
#
# user.add_movie("Zootopia", "Animation")
# user.add_movie("Dolittle", "Adventure/Family")
#
# user.save_to_file()

user = User.load_from_file("Krista.txt")

print(user.name)
print(user.movies)





