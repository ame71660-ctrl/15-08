import string
texts = ['Python Community','i like python community!','Should,I,subscribe? Yes!']
for text in texts:
    clean_text=text.translate(str.maketrans("","", string.punctuation))
    words=[word.capitalize() for word in clean_text.split() ]
    hasting ="".join(words)
    hasting=hasting[:140]
    print(hasting)