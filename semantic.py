# ===== LET'S GET PEDANTIC WITH SEMANTICS =====

import spacy
nlp = spacy.load('en_core_web_md')


# === A Cat and a Monkey walk in to a Whole Foods for an apple & a banana ===
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
'''
'cat':'banana'?
I'm not too sure what cats and bananas have in common
anymore than an apple. All I can think of is that
cats are often scared of bananas but not apples.
'''

# My example:
tokens = nlp('diet food pizza Italy ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
'''
I really would've for Italy had more in common with food and 
pizza, but I can say that dieting doesn't happen it Italy!
'''

# === Running the example file with 'sm' not 'md'! O_O ===

'''
The difference when running the code with 'sm' instead of 'md'
was that my terminal printed the following:
_________________________________________________________________
The model you're using has no word vectors loaded, so the result 
of the Doc.similarity method will be based on the tagger, parser 
and NER, which may not give useful similarity judgements. This 
may happen if you're using one of the small models, e.g. `en_core_web_sm`, 
which don't ship with word vectors and only use context-sensitive tensors. 
You can always add your own word vectors, or use one of the 
larger models instead if available.
_________________________________________________________________
This displays clearly the difference between the 'sm' from the
last task and the 'md' (and other models) that can be imported.
'''