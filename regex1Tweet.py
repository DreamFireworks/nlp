from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer

pattern1=r"\#\w+"

tweets =['The Witcher 3: Wild Hunt yeni nesil konsollar için duyuruldu. #witcher #Witcher3 #CDProjektRed #PS5 #XboxSeriesX #Xbox #oyun #games',
 'Uma Aslında Kim? | Witcher 3 : Wild Hunt Hikayeleri via @YouTube #witcher #netflix #uma #fantastik',
 '#Cyberbug2077 hashtagleri yayılmaya başladı. #witcher 3 ün çıkışından daha kötü oldu bug açısından. Bakalım düzeltebilecekler mi @CDPROJEKTRED']
 
 
hashtags = regexp_tokenize(tweets[0],pattern1)
print(hashtags)