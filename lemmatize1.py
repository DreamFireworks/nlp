# Import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter

article = """
History of british penny
The kingdoms of England and Scotland were merged by the 1707 Act of Union to form the Kingdom of Great Britain. The exchange rate between the pound scots and the English pound sterling had been fixed at 12:1 since the Union of the Crowns in 1603, and in 1707 the pound Scots ceased to be legal tender, with the pound sterling to be used throughout Great Britain. The penny replaced the shilling of the pound Scots.[2]
The design and specifications of the English penny were unchanged by the Union, and it continued to be minted in silver after 1707. Queen Anne's reign saw pennies minted in 1708, 1709, 1710, and 1713. These issues, however, were not for general circulation, instead being minted as Maundy money. The prohibitive cost of minting silver coins had meant the size of pennies had been reduced over the years, with the minting of silver pennies for general circulation being halted in 1660.[3]
The practice of minting pennies only for Maundy money continued through the reigns of George I and George II, and into that of George III. However, by George III's reign there was a shortage of pennies such that a great many merchants and mining companies issued their own copper tokens e.g. the Parys Mining Company on Anglesey issued huge numbers of tokens (although their acceptability was strictly limited).[4]
In 1797, the government authorised Matthew Boulton to strike copper pennies and twopences at his Soho Mint in Birmingham. At the time it was believed that the face value of a coin should correspond to the value of the material it was made from, so they had respectively to contain one or two pence worth of copper (for a penny this worked out to be one ounce of copper). This requirement meant that the coins would be significantly larger than the silver pennies minted previously. The large size of the coins, combined with the thick rim where the inscription was incuse i.e. punched into the metal rather than standing proud of it, led to the coins being nicknamed "cartwheels". These pennies were minted over the course of several years, but all are marked with the date 1797.[5]

19th century
By 1802, the production of privately issued provincial tokens had ceased.[6][7] However, in the next ten years the intrinsic value of copper rose. The return of privately minted token coinage was evident by 1811 and endemic by 1812, as more and more of the Government-issued copper coinage was melted down.[7] The Royal Mint undertook a massive recoinage programme in 1816, with large quantities of gold and silver coin being minted. To thwart the further issuance of private token coinage, in 1817 an Act of Parliament was passed which forbade the manufacture of private token coinage under very severe penalties.[7] Copper coins continued to be minted after 1797, through the reigns of George III, George IV and William IV, and the early reign of Queen Victoria. These later coins were smaller than the cartwheel pennies of 1797, and contained a smaller amount of copper.[5]
In 1857 a survey by the Royal Mint found that around one third of all copper coinage was worn or mutilated, often by advertisements. Two years later Thomas Graham, the Master of the Mint, convinced William Ewart Gladstone, then Chancellor of the Exchequer, that so large a part of the copper coinage must be taken out of circulation that it was worth introducing a whole new coinage which would be "much more convenient and agreeable in use".[8] These new coins were minted in bronze, and their specifications were no longer constrained by the onerous requirement that their face value should match the value of the base metal used to make the coin. These new coins were introduced in 1860 and a year later the withdrawal of the old copper coinage began.[8]

20th century
The specifications of the bronze version of the penny were a mass of 9.45 g (0.333 oz) and a diameter of 30.86 mm (1.215 in),[citation needed] and remained as such for over a hundred years. Pennies were minted every year of Queen Victoria's reign, and every year of Edward VII's reign. George V pennies were produced every year to the same standard until 1922, but after a three-year gap in production the alloy composition was changed to 95.5% copper, 3% tin, and 1.5% zinc, although the weight and size remained unchanged (which was necessary because of the existence by then of large numbers of coin-operated amusement machines and public telephones). Thereafter, pennies were minted every year for the remainder of George V's reign, although only six or seven 1933 coins were minted, specifically for the king to lay under the foundation stones of new buildings; one of these coins was stolen when a church in Leeds was demolished in the 1960s, and its whereabouts is unknown.[9]
A few pennies of Edward VIII exist, dated 1937, but technically they are pattern coins i.e. coins produced for official approval, which it would probably have been due to receive about the time that the King abdicated.[10]
A 1937 George VI penny. Note the change in design of the reverse, with the addition of the lighthouse and shield square which is not angled.
Pennies were not minted every year of George VI's reign: None were minted in 1941, 1942 and 1943. Pennies minted in 1950 and 1951 were for overseas use only. One 1952 penny, believed to be unique, was struck by the Royal Mint.
The worldwide shortage of tin during the Second World War caused a change in the alloy in 1944 to 97% copper, 0.5% tin, 2.5% zinc, but this bronze tarnishes unattractively, and the original 95.5% copper, 3% tin, 1.5% zinc alloy was restored in 1945.
Because of the large number of pennies in circulation there was no need to produce any more in the 1950s, however a large number of specimen sets were issued in 1953 for Elizabeth II's Coronation. At least one 1954 penny was struck, apparently for private internal purposes at the Royal Mint, but it was not until 1961 that there was a need for more pennies to be minted, and production continued each year until 1967, and afterwards (as pennies continued to be minted with the date 1967 until 1970). The 97% copper, 0.5% tin, 2.5% zinc alloy was used again for the 1960s pennies. Finally, there was an issue of proof quality coins dated 1970 produced to bid farewell to the denomination.
"""
tokens = word_tokenize(article)

lower_cased = [word.lower() for word in tokens]

alpha_only = [t for t in lower_cased if t.isalpha()]

no_stops = [t for t in alpha_only if t not in stopwords.words("english")]

wordnet_lemmatizer = WordNetLemmatizer()

lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

bow = Counter(lemmatized)

print(bow.most_common(10))


