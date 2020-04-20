class Movie:
    def __init__(self, title, genre, watched):
        self.title = title
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return "<Movie {}>".format(self.title)
