# A movie recommendation pragram using NLP
A program that will tell you what to watch next based on the word
vector similarity of the description of movies.

The program utilises the python spaCy NLP library to find similarities
of the context of the descriptions of the movies watched and match a new
unwatched movie to the viewer based on these. 


## How the program works
The movie titles and descriptions are stored in the text file called movies.txt.
watch_next.py opens and reads this file, storing the movies in a list. The program
will select a movie and recommend one to the user based on previous movies watched. 

In this program the only movie watxhed so far is Planet Hulk. The program will find
a similar movie to Planet Hulk based on the description similarities. 


## How to run
You will need to install the spaCy library in your environment/computer before 
attempting to run the program. spaCy uses the "en_core_web_md" language model
in this program. 

The movies.txt text file has to be in the same folder as the watch+next.py file, 
as this location is he path the program will read from. 

When you run the program from the terminal, you will see the recomended program
printed on screen. 
