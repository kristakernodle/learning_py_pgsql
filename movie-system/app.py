from user import User
import json


# user = User("Krista")
#
# user.add_movie("Zootopia", "Animation", watched=True)
# user.add_movie("Dolittle", "Adventure/Family")
#
# with open('Krista.txt', 'w') as f:
#     json.dump(user.json(),f)

with open('Krista.txt', 'r') as f:
    json_data = json.load(f)
    user = User.from_json(json_data)

print(user.name)
print(user.movies)





