# ***===== WHAT TO WATCH NEXT?! =====***

import spacy

# We load 'en_core_web_md' so we can accurately 
# compare blocks of text to find their similarities.
nlp = spacy.load('en_core_web_md')


# A variable for the description of our current movie. This could 
# also be a user input or data imported from somewhere else.
planetHulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

def watch_next(filmDescription):

    # Change our film description into an nlp for spaCy to read.
    nlpFilmDescription = nlp(filmDescription)

    # Create an empty list & dict to append 
    # our movies and descriptions to.
    movies_list = []
    movies_dict = {}

    # Read information from 'movies.txt' 
    # and append it to our empty list.
    with open('movies.txt', 'r') as movies:
        for lines in movies.readlines():
            movies_list.append(lines.split("\n'"))

    # Strip & split the data from our 
    # list and create a dictionary.
    for movies in movies_list:
        for movie in movies:
            movie = movie.strip().split(' :')
            movies_dict[movie[0]] = movie[1]


    # Now we want to use '.similarity' to compare the current 
    # film description against every other movie description.
    # We will do this with a list and dictionary again.
    similarity_list = []
    for movie in movies_dict:
        nlp_movie = nlp(movies_dict[movie])
        similarity_list.append([movie, nlp_movie.similarity(nlpFilmDescription)])

    similarity_dict = {}
    for movie in similarity_list:
        similarity_dict[movie[0]] = movie[1]


    # Now we have our similarities in our new dictionary, we can 
    # loop through every comparison to find the most similar 
    # movie while keeping track of the 'key' & 'value'.
    closest_similarity = 0

    for key, value in similarity_dict.items():
        if value > closest_similarity:
            closest_similarity = value
            similarity_key = key

    # Finally, with our most similar 
    # 'key' & 'value'('movie' & 'description') 
    # we can display the information clearly.
    print(f'''
With a similarity of {closest_similarity},
{similarity_key} would be the best movie 
to watch next! 
Here is the description:
"{movies_dict.get(similarity_key)}"
''')

# Initiate the function:
watch_next(planetHulk)