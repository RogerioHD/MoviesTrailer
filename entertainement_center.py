import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story', 'A boy and his toy',
                        'https://upload.wikimedia.org/wikipedia/pt/d/'
                        'dc/Movie_poster_toy_story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

rocky_balboa = media.Movie('Rocky Balboa', 'A history of Boxing',
                           'https://upload.wikimedia.org/wikipedia/commons'
                           '/8/8a/Philly042107-014-RockyStatue.jpg',
                           'https://www.youtube.com/watch?v=8tab8fK2_3w')

terminator = media.Movie('The Terminator', 'One that came to Kill',
                         'https://upload.wikimedia.org/wikipedia/pt/5/'
                         '5a/Terminator1984.jpg',
                         'https://www.youtube.com/watch?v=k64P4l2Wmeg')

sixth_sense = media.Movie('The Sixth Sense', 'I see death people',
                          'https://upload.wikimedia.org/wikipedia'
                          '/pt/6/66/The_sixth_sense.jpg',
                          'https://www.youtube.com/watch?v=VG9AGf66tXM')

blade_runner = media.Movie('Blade Runner', 'The future is in 2049',
                           'https://upload.wikimedia.org/wikipedia'
                           '/pt/b/bb/BladeRunner-P%C3%B4ster.jpg',
                           'https://www.youtube.com/watch?v=gCcx85zbxz4')

matrix = media.Movie('Matrix', 'I choose the red pill',
                     'https://upload.wikimedia.org/wikipedia/'
                     'pt/c/c1/The_Matrix_Poster.jpg',
                     'https://www.youtube.com/watch?v=m8e-FF8MsqU')
# Lista de filmes que irá popular o site
moviesArray = [rocky_balboa, toy_story, terminator,
               sixth_sense, blade_runner, matrix]
# Função do fresh_tomatoes que popula o site tendo uma lista como parâmetro
fresh_tomatoes.open_movies_page(moviesArray)
