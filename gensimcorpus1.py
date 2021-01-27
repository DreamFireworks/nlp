from nltk.tokenize import word_tokenize
from collections import Counter
from gensim.corpora.dictionary import Dictionary

article = """
Dîvânu Lugâti't-Türk (Türkçe: Türk Dilleri Sözlüğü), Orta Türkçe döneminde Kâşgarlı Mahmud tarafından Bağdat'ta 1072-1074 yılları arasında yazılan Türkçe-Arapça bir sözlüktür. Türkçenin bilinen en eski sözlüğü olup Batı Asya yazı Türkçesiyle ilgili var olan en kapsamlı ve önemli dil yapıtıdır.
Bir kültür hazinesi olan Dîvânu Lugâti't-Türk (DLT), bir yandan XI. asırda söz varlığının genişliğini ve çeşitliliğini gözler önüne sermekte, bir yandan da o dönemde insan ve toplum yaşamıyla, maddi ve manevi kültürle ilgili, ilgi çekici kayıtlar ortaya koymaktadır. Bu bakımdan zamanımızdan yaklaşık bin yıl önce yazılan DLT, Türkçenin ilk sözlüğü olmaktan öte pek çok araştırmacının teslim ettiği üzere tarihî ve kültürel başvuru kaynaklarımızın da ilklerindendir. Toplumların yaşam biçimleri, dünyayı algılayışları o toplumun dilinde de kendini gösterir. DLT, yaklaşık bir asırdır Türklük biliminin başlıca araştırma konularından biri olmuştur. Bu eser, edebiyat bakımından önemli olduğu kadar kültür özelliklerini yansıtması bakımından da değerlidir.
Kökleşik Arap sözlük bilgisi ilkelerine göre hazırlanmış olan sözlük, Kâşgarlı Mahmud'un Türk boylarıyla ilgili ayrıntılı bilgisinin yanı sıra, Arap dil bilimi konusunda da esaslı bir eğitim görmüş olduğunu gösterir.
"""

tokens = word_tokenize(article)
lower_cased = [word.lower() for word in tokens]
bag_of_words = Counter(lower_cased)
print(tokens)

tokenized_docs = [word_tokenize(doc.lower()) for doc in tokens]

dictionary = Dictionary(tokenized_docs)

turk_id = dictionary.token2id.get("türk")

print(dictionary.get(turk_id))

corpus = [dictionary.doc2bow(word) for word in tokenized_docs]

print(corpus)