import fresh_tomatoes
import media

# Creating each of the movie objects with their associated information
tucker = media.Movie("Tucker", "The story of a man and his dreams",
                     "http://upload.wikimedia.org/wikipedia/en/2/28",
                     "/Tuckerposter.jpg",
                     "https://www.youtube.com/watch?v=ty93RYkzYQQ",
                     "August 12, 1988")

avengers = media.Movie("The Avengers", "Earth's mightiest heroes defend",
                       "earth",
                       "http://upload.wikimedia.org/wikipedia/en/f/f9/",
                       "TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8",
                       "May 4, 2012 (USA)")

imitation = media.Movie("The Imitation Game",
                        "Alan Turing works to crack the code of the",
                        " Enigma Machine",
                        "http://upload.wikimedia.org/wikipedia/en/5/5e",
                        "/The_Imitation_Game_poster.jpg",
                        "https://www.youtube.com/watch?v=S5CjKEFb-sM",
                        "January 7, 2015 (Egypt)")

transcendence = media.Movie("Transendence",
                            "An AI researcher achieves transcendence",
                            "by going digital",
                            "http://upload.wikimedia.org/wikipedia/en/e/ef",
                            "/Transcendence2014Poster.jpg",
                            "https://www.youtube.com/watch?v=VCTen3-B8GU",
                            "April 10, 2014 (USA)")

holy_grail = media.Movie("Monty Python and the Quest for the Holy Grail",
                         "A group of knights seek out the Holy Grail, ",
                         "hilarity ensues",
                         "http://upload.wikimedia.org/wikipedia/en/4/49/",
                         "Monty_python_and_the_holy_grail_2001_release_",
                         "movie_poster.jpg",
                         "https://www.youtube.com/watch?v=urRkGvhXc8w",
                         "January 1, 1975 (USA)")

to_the_greek = media.Movie("Get Him to the Greek",
                           "An understudy of Jay-Z has to get a washed ",
                           "up rock star to play a show",
                           "http://upload.wikimedia.org/wikipedia/en/c/c2",
                           "/Get_Him_to_the_Greek.jpg",
                           "https://www.youtube.com/watch?v=N6ixkr0-qvo",
                           "June 4, 2010 (USA)")

# The array of movies to be loaded
movies = [tucker, avengers, imitation, transcendence,
          holy_grail, to_the_greek]

# Takes the array of movies and displays them on a webpage
fresh_tomatoes.open_movies_page(movies)
