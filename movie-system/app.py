from user import User
import json
import os
print(os.getcwd())

user = User("Krista")

user.add_movie("Zootopia", "Animation", watched=True)
user.add_movie("Dolittle", "Adventure/Family")

with open('Krista.txt', 'w') as f:
    json.dump(user.json(),f)





