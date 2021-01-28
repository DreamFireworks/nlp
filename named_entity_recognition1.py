import nltk

text="""A biography of Yue Fei, the Eguo Jintuo Zubian (鄂國金佗稡编), was written 60 years after his death by his grandson, the poet and historian Yue Ke (岳柯) (1183–post 1240).[3][4][5] In 1346 it was incorporated into the History of Song, a 496-chapter record of historical events and biographies of noted Song dynasty individuals, compiled by Yuan dynasty prime minister Toqto'a and others.[6] Yue Fei's biography is found in the 365th chapter of the book and is numbered biography 124.[7] Some later historians including Deng Guangming (1907–1998) now doubt the veracity of many of Yue Ke's claims about his grandfather.[8]
According to the History of Song, Yue Fei was named "Fei", meaning to fly, because at the time he was born, "a large bird like a swan landed on the roof of his house"."""

tokenized = nltk.word_tokenize(text)

tagged = nltk.pos_tag(tokenized)

named_entity = nltk.ne_chunk(tagged)

named_entity.draw()
