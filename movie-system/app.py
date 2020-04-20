from user import User
import json

commands = ["options: List these controls",
            "new: Add a new movie to the user",
            "list: List all movies for user",
            "update: Set a movie as watched for user",
            "delete: Delete a movie from user's movie list",
            "watched: List all watched movies",
            "quit: Save and quit program."]


def menu():
    username = input("Enter the user's name: ")
    try:
        with open(f"{username}.txt".format(username), 'r') as f:
            print(f'Welcome, {username}!')
            user_data = json.load(f)
            user = User.from_json(user_data)
    except FileNotFoundError:
        user = User(username)

    print("To see all possible commands, enter 'options'")
    selection = input("Please enter command: ").lower()

    selection.strip()

    while selection != "quit":
        if selection == "options":
            print(*commands, sep="\n")

        elif selection == "list":
            print(*[f"{movie.name}" for movie in user.movies], sep="\n")

        elif selection == "watched":
            print(*[movie.name for movie in user.watched_movies()], sep="\n")
        else:

            movie_name = input("Enter the movie name: ")

            if selection == "new":
                movie_genre = input("Enter the movie genre: ")
                movie_watched = input("Has this movie been watched? Y/[N]: ")
                if movie_watched == 'y':
                    watched=True
                else:
                    watched = False
                user.add_movie(movie_name, movie_genre, watched=watched)

            for movie in user.movies:
                if movie.name == movie_name:
                    if selection == "delete":
                        user.movies = [movie for movie in user.movies if movie.name != movie_name]
                        break
                    movie.watched = True
                    break

        selection = input("Please enter command: ").lower()
        selection.strip()

    with open(f"{username}.txt", 'w') as f:
        json.dump(user.json(), f)


menu()
