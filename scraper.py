import requests
import bs4
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd


def scrape_reggaeton_lyrics():
    try:
        LETRAS_ROOT_URL = "https://www.letras.com"
        LETRAS_REGGAETON_URL = LETRAS_ROOT_URL + "/mais-acessadas/reggaeton/"

        # OBTENEMOS LA PÁGINA DONDE SALEN TODOS LOS ARTISTAS DE REGGAETON

        response = requests.get(LETRAS_REGGAETON_URL)

        soup = BeautifulSoup(response.text, "html.parser")

        # Achicamos la búsqueda al contenedor
        artists_container = soup.find("ol", {'class': 'top-list_art'})

        # Como ya hemos achicado al contenedor, buscamos el patrón que se repite. En este caso las etiquetas "a"
        artists_html = artists_container.find_all("a")

        # Creamos la lista con las URL de los artistas. Esta lista está compuesta por listas de 2 elementos: URL y nombre del artista.
        artists_href = [[artist.get('href'), artist.text] for artist in artists_html]

        # Creamos un dataframe con las columnas artista, título de la canción y la letra.
        df = pd.DataFrame(columns=['Artist', 'Title', 'Lyrics'])

        for artist_href in artists_href:
            artist_href[0] = LETRAS_ROOT_URL + artist_href[0]

            # OBTENEMOS LA PÁGINA DONDE SALEN LOS TÍTULOS DE LAS TOP 20 CANCIONES DEL ARTISTA

            art_response = requests.get(artist_href[0])
            art_soup = BeautifulSoup(art_response.text, "html.parser")

            # Achicamos la búsqueda al contenedor
            songs_container = art_soup.find("ol", {'class': 'cnt-list cnt-list--num cnt-list--col2'})

            # Como ya hemos achicado al contenedor, buscamos el patrón que se repite. En este caso es la etiqueta "a".
            songs_html = songs_container.find_all("a")

            # Creamos la lista con las URL de las canciones. Esta lista está compuesta por listas de 2 elementos: URL y título de la canción.
            songs_href = [[song.get('href'), song.text] for song in songs_html]

            # Imprimimos las URL de cada una de las canciones de los artistas.
            # pprint(songs_href)

            for song_href in songs_href:
                song_href[0] = LETRAS_ROOT_URL + song_href[0]

                # OBTENEMOS LA PÁGINA DONDE SALE LA LETRA DE LA CANCIÓN

                song_response = requests.get(song_href[0])
                song_soup = BeautifulSoup(song_response.text, "html.parser")

                # Achicamos la búsqueda al contenedor
                paragraphs_container = song_soup.find("div", {'class': 'cnt-letra p402_premium'})

                # Como ya hemos achicado al contenedor, buscamos el patrón que se repite. En este caso las etiquetas "p".
                paragraphs_html = paragraphs_container.find_all("p")

                # Normalmente crearíamos la lista con las letras de las canciones de la siguiente forma.
                # lyrics = [paragraph.text.splitlines() for paragraph in paragraphs_html]
                # Pero no lo voy a hacer así porque no me permite sacar los versos.
                # Voy a sacar las lyrics como paragraphs_html y más adelante le haré un tratamiento con pandas para que
                # cada canción sean una lista con tantas strings como versos tenga.

                # Aprovechando el loop, vamos añadiendo al dataframe cada letra (html), con su título y artista correspondiente.
                # Incluyo "ignore_index=True" para que los index se vayan añadiendo de forma incremental.
                df = df.append({'Artist': artist_href[1], 'Title': song_href[1], 'Lyrics': paragraphs_html} , ignore_index=True)
    except:
        # He hecho este except para poder parar el scraping, y poder seguir con un dataframe aunque esté incompleto.
        print("The web scraping isn't fully done, but at least you got a piece of it.")
    return df

