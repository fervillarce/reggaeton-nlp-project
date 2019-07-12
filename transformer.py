def translate_list(l):
    list_translated = []
    try:
        for line in l:
            blob = TextBlob(line)
            line_translated = blob.translate(to="en")
            list_translated.append(line_translated)
    except:
        # Metí la excepción para que no me cortara la traducción cuando haya un '', pero luego hice una función para eliminar ''.
        pass
    return list_translated


def analyze_sentiment(l):
    sentim = []
    try:
        for line in l:
            blob = TextBlob(line)
            sentim.append(blob.sentiment.polarity)
    except:
        pass
    return sentim


def flatten_list(l):
    """
    Receive a list of lists and return a list with just one element.
    """
    return sum(l, [])


import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

def remove_stopwords(l):
    new_list = []
    stop_words = stopwords.words('spanish')
    more_stopwords = ['si', 'pa', 'sé', 'solo', 'yeah', 'yeh', 'oh', 'i', 'to', 'va', 'the', 'aunque', 'you', 'eh', 'cómo']
    total_stopwords = stop_words + more_stopwords
    for sentence in l:
        sentence = sentence.lower() # Si no lo pongo, no me elimina las palabras que empiezan por mayúscula (ejemplo: Y, Que)
        word_tokens = word_tokenize(sentence) 
        filtered_sentence = [w for w in word_tokens if not w in total_stopwords]
        filtered_sentence = [word.lower() for word in filtered_sentence if word.isalpha()]
        new_list.append(filtered_sentence)
    return flatten_list(new_list)


"""
Hice la siguiente consulta para ver qué palabras son las más frecuentes tras haber quitado stopwords.
relevant_words = pd.Series(df['No_stopwords'].sum())
relevant_words.value_counts()
Por eso, en la función añado "more_stopwords".
"""


