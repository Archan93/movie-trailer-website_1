import movie_class
import fresh_tomatoes

# Create instances of movies by passing movie name, storyline, poster image url,
# and Youtube trailer url as arguments.  
Iron_man_1 = movie_class.Movies(
                    "Iron Man 1",
                    "After being held captive in an Afghan cave, an industrialist "
                    "creates a unique weaponized suit of armor to fight evil.",
                    "http://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                    "https://www.youtube.com/watch?v=8hYlB38asDY")
                                
Thor = movie_class.Movies(
                "Thor",
                "The powerful but arrogant god Thor is cast out of Asgard to live "
                "amongst humans in Midgard (Earth), where he soon becomes one "
                "of their finest defenders.",
                "http://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
                "https://www.youtube.com/watch?v=JOddp-nlNvQ")
                    
The_Avengers = movie_class.Movies(
                        "The Avengers",
                        "Earth's mightiest heroes must come together and learn to fight "
                        "as a team if they are to stop the mischievous Loki and his "
                        "alien army from enslaving humanity.",
                        "http://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                        "https://www.youtube.com/watch?v=eOrNdBpGMv8")
                                
Man_of_Steel = movie_class.Movies(
                        "Man of Steel",
                        "Clark Kent, one of the last of an extinguished race disguised "
                        "as an unremarkable human, is forced to reveal his identity "
                        "when Earth is invaded by an army of survivors who threaten to "
                        "bring the planet to the brink of destruction.",
                        "http://upload.wikimedia.org/wikipedia/en/8/85/ManofSteelFinalPoster.jpg",
                        "https://www.youtube.com/watch?v=T6DJcgm3wNY")
                            
Batman_Begins = movie_class.Movies(
                        "Batman_Begins",
                        "After training with his mentor, Batman begins his war on crime "
                        "to free the crime-ridden Gotham City from corruption that the "
                        "Scarecrow and the League of Shadows have cast upon it.",
                        "http://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
                        "https://www.youtube.com/watch?v=vak9ZLfhGnQ")
                                
Green_Lantern = movie_class.Movies(
                        "Green Lantern",
                        "Reckless test pilot Hal Jordan is granted an alien ring that "
                        "bestows him with otherworldly powers that inducts him into an "
                        "intergalactic police force, the Green Lantern Corps.",
                        "http://upload.wikimedia.org/wikipedia/en/6/6b/Green_Lantern_poster.jpg",
                        "https://www.youtube.com/watch?v=8NWGl_A3b60")

#Store movie instances in to an array.                                
movies = [Iron_man_1, Thor, The_Avengers, Man_of_Steel, Batman_Begins, Green_Lantern]

#pass array in to open_movies_page function to create a web page for the movies.
fresh_tomatoes.open_movies_page(movies)