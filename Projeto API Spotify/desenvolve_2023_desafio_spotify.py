# pip install spotipy --upgrade
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def autenticar_api(client_id, client_secret):
    client_id = client_id
    client_secret = client_secret
    chave_acesso = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    return chave_acesso


def procurar_musica(chave_acesso, musica):
    resultado = chave_acesso.search(
        q=musica, type='track', market='BR', limit=50)
    return resultado


client_id = 'CLIENTE_ID'
client_secret = 'CLIENT_SECRET'
musica = 'beleza'
chave_acesso = autenticar_api(client_id, client_secret)
resultado = procurar_musica(chave_acesso, musica)


for track in resultado['tracks']['items']:
    print('Id: ' + track['id'], end=' - ')
    print('Musica: ' + track['name'], end=' - ')
    # ', '.join([artist['name'] for artist in track['artists']])
    print('Cantor: ' + track['artists'][0]['name'])
