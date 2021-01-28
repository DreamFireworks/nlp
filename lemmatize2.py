from nltk.stem import WordNetLemmatizer

lem = WordNetLemmatizer()

words = ["drive","driving","driver","drives","drove","cats","children","making","made","doing","done"]

for w in words:
    print(lem.lemmatize(w))

print(lem.lemmatize("driving","v")) #v is for verb
print(lem.lemmatize("drove","v")) #v is for verb