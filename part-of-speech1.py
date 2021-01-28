import nltk

text = """The Lego Group began in the workshop of Ole Kirk Christiansen (1891–1958), a carpenter from Billund, Denmark, who began making wooden toys in 1932.[8][9] In 1934, his company came to be called "Lego", derived from the Danish phrase leg godt [lɑjˀ ˈkʌt], which means "play well".[10] In 1947, Lego expanded to begin producing plastic toys.[11] In 1949 Lego began producing, among other new products, an early version of the now familiar interlocking bricks, calling them "Automatic Binding Bricks". These bricks were based on the Kiddicraft Self-Locking Bricks, which had been patented in the United Kingdom in 1939[12] and released in 1947. Lego had received a sample of the Kiddicraft bricks from the supplier of an injection-molding machine that it purchased.[13] The bricks, originally manufactured from cellulose acetate, were a development of the traditional stackable wooden blocks of the time.The Lego Group's motto, "only the best is good enough"[15] (Danish: det bedste er ikke for godt, literally "the best isn't excessively good") was created in 1936.[9] This motto, which is still used today, was created by Christiansen to encourage his employees never to skimp on quality, a value he believed in strongly.[9] By 1951 plastic toys accounted for half of the Lego company's output, even though the Danish trade magazine Legetøjs-Tidende ("Toy Times"), visiting the Lego factory in Billund in the early 1950s, felt that plastic would never be able to replace traditional wooden toys.[16] Although a common sentiment, Lego toys seem to have become a significant exception to the dislike of plastic in children's toys, due in part to the high standards set by Ole Kirk."""

tokenized = nltk.word_tokenize(text)

pos = [nltk.pos_tag(word) for word in tokenized]
print(pos)

"""
CC     coordinating conjunction
CD     cardinal digit
DT     determiner
EX     existential there (like: "there is" ... think of it like "there exists")
FW     foreign word
IN     preposition/subordinating conjunction
JJ     adjective 'big'
JJR    adjective, comparative 'bigger'
JJS    adjective, superlative 'biggest'
LS     list marker 1)
MD     modal could, will
NN     noun, singular 'desk'
NNS    noun plural 'desks'
NNP    proper noun, singular 'Harrison'
NNPS   proper noun, plural 'Americans'
PDT    predeterminer 'all the kids'
POS    possessive ending parent's
PRP    personal pronoun I, he, she
PRP$   possessive pronoun my, his, hers
RB     adverb very, silently,
RBR    adverb, comparative better
RBS    adverb, superlative best
RP     particle give up
TO     to go 'to' the store.
UH     interjection errrrrrrrm
VB     verb, base form take
VBD    verb, past tense took
VBG    verb, gerund/present participle taking
VBN    verb, past participle taken
VBP    verb, sing. present, non-3d take
VBZ    verb, 3rd person sing. present takes
WDT    wh-determiner which
WP     wh-pronoun who, what
WP$    possessive wh-pronoun whose
WRB    wh-abverb where, when
"""