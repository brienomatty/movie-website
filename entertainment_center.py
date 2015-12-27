import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "Awesomness",
                     "https://sleephotography.files.wordpress.com/2013/05/avatar_poster_21.jpg",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")

Titanic = media.Movie("Titanic",
                      "A love story about a poor man and a rich chick",
                      "http://cdn.traileraddict.com/content/paramount-pictures/titanic.jpg",
                      "https://www.youtube.com/watch?v=kVrqfYjkTdQ")

Boondock_Saints = media.Movie("Boondock Saints",
                              "A pair of twin Irish Catholics murder murderers..for good.",
                              "http://orig11.deviantart.net/09c7/f/2010/073/7/9/boondock_saints_movie_poster_2_by_demonofthesword.jpg",
                              "https://www.youtube.com/watch?v=ydXojYfCF3I")

Weekend_at_Bernies = media.Movie("Weekend at Bernie's",
                                 "The most fun dead guy EVER",
                                 "http://movie-guru.com/wp-content/uploads/2015/03/h3hjMREZEUPtDkZBiYDzLq0THk0.jpg",
                                 "https://www.youtube.com/watch?v=YCTgcZ6ImsQ")

Lords_of_Dogtown = media.Movie("Lords of Dogtown",
                               "The start of professional skateboarding",
                               "http://images.moviepostershop.com/lords-of-dogtown-movie-poster-2005-1020255725.jpg",
                               "https://www.youtube.com/watch?v=BmXeGwbGVCE")

movies = [Lords_of_Dogtown, Weekend_at_Bernies, Boondock_Saints, Titanic, avatar, toy_story]

# Open Page in Browser
fresh_tomatoes.open_movies_page(movies)
