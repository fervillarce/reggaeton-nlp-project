from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Nube de palabras
def print_wordcloud(list_of_words, file_name):
    """
    Receive a list of words and print a wordcloud.
    """
    text = " ".join(list_of_words) # Concatena todas palabras de la lista

    # Create and generate a word cloud image:
    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(file_name)
    return plt.show()


# Hacemos stemming, aunque en español no funciona muy bien
from nltk.stem import SnowballStemmer

def get_stemming(list_of_words):
    """
    Receive a list of words, get stemming and return a new list of words.
    """
    stemmer = SnowballStemmer('spanish')
    stemmed_text = [stemmer.stem(w) for w in list_of_words]
    return stemmed_text

