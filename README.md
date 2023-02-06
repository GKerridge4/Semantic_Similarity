# Semantic_Similarity
## For HyperionDev Bootcamp

### **This is T38**

This file uses spaCy.
Follow these steps in your terminal:
```
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
```
Or go to the [spaCy website](https://spacy.io/usage) for further instructions.

And you will need to download 'en_core_web_md', like so:
```
python -m spacy download en_core_web_md
```
Find out more about spaCy modules [here.](https://spacy.io/models/en)

#### ***Compulsory Task 1 - semantic.py***

This task shows examples of 'en_core_web_sm' & 'en_core_web_md'
and compares the abilities of both.

#### ***Compulsory Task 2 - watch_next.py***

This file uses spaCy. 
For this file we will only use 'en_core_web_md'.

*Follow the steps above for install information* 👆🏻

This code takes the description of a movie (Planet Hulk in this example) and compares this 
description against a file (movies.txt) that containes a list of movies and their descriptions.
This code be edited to read and movie descriptions and take different user inputs.

To find and compare values, I referenced this code[^1]:
```python
for key, value in similarity_dict.items():
    if value > closest_similarity:
        closest_similarity = value
        similarity_key = key
```

[^1]: *"How to find the largest value in a dictionary by comparing values?"*, zenpoy(2013) - [Link here](https://stackoverflow.com/questions/20453674/how-to-find-the-largest-value-in-a-dictionary-by-comparing-values)
