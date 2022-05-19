import random

movies = [{'nome' : 'Homem de Ferro', 'genero' : 'Super Herói', 'duracao' : 126},
          {'nome' : 'Circulo de Fogo', 'genero' : 'Ficção Científica', 'duracao' : 132},
          {'nome' : 'Perdido em Marte', 'genero' : 'Ficção Científica', 'duracao' : 141},
          {'nome' : 'O Óleo de Lorenzo', 'genero' : 'Drama', 'duracao' : 129}]

genres = {movie['genero'] for movie in movies} # Utilizando set pra evitar duplicatas

genres = list(genres) # Casting pra lista pra conseguir acessar os elementos via índice

print('Você tem alguma preferência de filme?')
print('(0) Sem preferência')
for index, genre in enumerate(genres):
    print(f'({index+1}) {genre}')

genre_choice = int(input())

if genre_choice != 0:
    pref_genre = genres[genre_choice - 1]

    # Filtra a lista pelo gênero
    filtered_obj = filter(lambda movie : pref_genre == movie['genero'], movies)

    # filter retorna um gerador, daí o casting
    movies = list(filtered_obj)

choice = random.choice(movies)

print('Você vai assistir:', choice)