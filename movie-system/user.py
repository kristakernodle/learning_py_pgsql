from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre, watched=False):
        movie = Movie(name, genre, watched)
        self.movies.append(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.title != name, self.movies))

    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))

    def save_to_file(self):
        with open("{}.txt".format(self.name), 'w') as f:
            for movie in self.movies:
                f.write("{},{},{}\n".format(movie.title, movie.genre, str(movie.watched)))

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            content = f.readlines()
            username = filename.strip('.txt')
            movies = []
            for item in content:
                movie = item.split(',')
                movies.append(Movie(movie[0], movie[1], watched=bool(movie[2])))
        user = User(username)
        user.movies = movies
        return user
