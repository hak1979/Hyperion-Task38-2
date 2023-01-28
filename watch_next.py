'''
A program that will tell you what to watch next based on the word
vector similarity of the description of movies.
'''

# import libraries
import os
import sys
import spacy

# load the language model
nlp = spacy.load("en_core_web_md")

# read movies.txt file if exist, toehrwise error message and exit program
# a list of movies is stored in movies_list
if os.path.isfile("movies.txt"):
    with open("movies.txt", "r+", encoding="utf-8") as file:
        movies_list = file.readlines()
else:
    print("movies.txt file does not exist.")
    print("The program will terminate now.")
    sys.exit()


def watch_next(movie_list):
    ''' A function to return which movies a user would watch next if they have
        watched Planet Hulk. The function takee in the movies list as a parameter
        and returns the title of the most similar movie.'''

    planet_hulk_description = nlp("Will he save their world or destroy it? When the"\
                            " Hulk becomes too dangerous for the Earth, the"\
                            " Illuminati trick Hulk into a shuttle and launch him"\
                            " into space to a planet where the Hulk can live in peace."\
                            " Unfortunately, Hulk land on the planet Sakaar where he is"\
                            " sold into slavery and trained as a gladiator.")

    # set the highest similarity initially to 0, the first movie will be compared to this
    highest_similarity = 0

    # itirate through the list of movies
    for movie in movie_list:
        movie = movie.strip().split(" :")

        # use spacy to calculate the similarities between the movie (movie[1])
        # and planet hulk desciptions
        similarity = nlp(movie[1]).similarity(planet_hulk_description)

        # if the similarity is greater than the highest so far, set this as highest
        # similarity and set the movie title as selected movie; movie[0]
        if similarity > highest_similarity:
            highest_similarity = similarity
            selected_movie = movie[0]

    # returns the title of the selected movie
    return selected_movie


# call wacth_next function and print out the recommendation on screen.
print("The recommended movie to watch next based on your recent views is"\
      f" {watch_next(movies_list)}")
