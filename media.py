import webbrowser


class Movie():
    """Creates a movie with the necessary pieces of information
       about that movie

    Attributes:
        title: A string for the title of the movie
        storyline: A string for the summary of the movie
        poster_image_url: A url for the poster image
        trailer_youtube_url: A url to watch the trailer
        release_date: The release date of the movie
        """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date

    # Used to display the trailer of the movie
    # object passed to it in a web browser
    def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
