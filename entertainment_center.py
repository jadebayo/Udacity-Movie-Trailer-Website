import media
import fresh_tomatoes

#Creating instances of movies

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar =  media.Movie("Avatar",
                      "A marine on an alien planet",
                      "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                      "http://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie("School of Rock", "Storylie",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille", "Storyline",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Storyline",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

the_hunger_games = media.Movie("Hunger Games", "Storyline",
                               "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                               "https://www.youtube.com/watch?v=PbA63a7H0bo")

#Adding the movies to a list of movies
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, the_hunger_games]

fresh_tomatoes.open_movies_page(movies)
