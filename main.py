import telebot
from telebot import types
import json
import os

API_TOKEN = '7633045825:AAFLA9DhelnnVpE30T4W01SJX9Qy3A6N8Jk'
bot = telebot.TeleBot(API_TOKEN)

# Файл для хранения фильмов
data_file = 'movies.json'

# Загрузка фильмов из файла
def load_movies():
    if os.path.exists(data_file):  # Проверка существования файла
        with open(data_file, 'r') as f:
            return json.load(f)  # Загрузка данных из файла JSON
    return {}  # Возврат пустого словаря, если файл не найден

# Сохранение фильмов в файл
def save_movies(movies):
    with open(data_file, 'w') as f:
        json.dump(movies, f, indent=4)  # Запись данных в JSON-файл с отступами

# Инициализация фильмов
user_movies = load_movies()

# Обработка команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, 
        "Привет! Я бот-киноман. Давайте составим ваш список фильмов для просмотра!\n"
        "Используйте команды: /add, /view, /edit, /delete."
    )

# Обработка команды /add для добавления фильма
@bot.message_handler(commands=['add'])
def add_movie(message):
    msg = bot.send_message(
        message.chat.id, 
        "Введите информацию о фильме в формате: Название, Год выпуска, Жанр"
    )
    bot.register_next_step_handler(msg, process_movie)

# Обработка добавления фильма
def process_movie(message):
    try:
        movie_data = message.text.split(',')
        title, year, genre = movie_data[0].strip(), movie_data[1].strip(), movie_data[2].strip()

        user_id = str(message.chat.id)

        if user_id not in user_movies:
            user_movies[user_id] = []

        user_movies[user_id].append({'title': title, 'year': year, 'genre': genre})
        save_movies(user_movies)
        bot.send_message(message.chat.id, f'Фильм "{title}" ({year}, {genre}) добавлен в ваш список.')
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка в формате данных. Пожалуйста, введите информацию снова.')

# Обработка команды /view для просмотра фильмов
@bot.message_handler(commands=['view'])
def view_movies(message):
    user_id = str(message.chat.id)
    if user_id in user_movies and user_movies[user_id]:
        movies_list = '\n'.join(
            [f'{m["title"]} ({m["year"]}, {m["genre"]})' for m in user_movies[user_id]]
        )
        bot.send_message(message.chat.id, f'Ваш список фильмов:\n{movies_list}')
    else:
        bot.send_message(message.chat.id, 'Ваш список фильмов пуст.')

# Обработка команды /delete для удаления фильма
@bot.message_handler(commands=['delete'])
def delete_movie(message):
    user_id = str(message.chat.id)
    if user_id in user_movies and user_movies[user_id]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
        for movie in user_movies[user_id]:
            markup.add(movie['title'])
        msg = bot.send_message(message.chat.id, 'Выберите фильм для удаления:', reply_markup=markup)
        bot.register_next_step_handler(msg, process_delete_movie)
    else:
        bot.send_message(message.chat.id, 'Удалять нечего.')

# Обработка удаления фильма
def process_delete_movie(message):
    user_id = str(message.chat.id)
    movie_title = message.text

    user_movies[user_id] = [m for m in user_movies[user_id] if m['title'] != movie_title]
    save_movies(user_movies)
    bot.send_message(message.chat.id, f'Фильм "{movie_title}" удален из вашего списка.')

# Обработка команды /edit для редактирования фильма
@bot.message_handler(commands=['edit'])
def edit_movie(message):
    user_id = str(message.chat.id)
    if user_id in user_movies and user_movies[user_id]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
        for movie in user_movies[user_id]:
            markup.add(movie['title'])
        msg = bot.send_message(message.chat.id, 'Выберите фильм для редактирования:', reply_markup=markup)
        bot.register_next_step_handler(msg, process_edit_movie)
    else:
        bot.send_message(message.chat.id, 'Редактировать нечего.')

# Обработка редактирования фильма
def process_edit_movie(message):
    user_id = str(message.chat.id)
    movie_title = message.text

    for movie in user_movies[user_id]:
        if movie['title'] == movie_title:
            msg = bot.send_message(
                message.chat.id, 
                'Введите новую информацию о фильме в формате: Название, Год выпуска, Жанр'
            )
            bot.register_next_step_handler(msg, lambda msg: update_movie(msg, movie))
            return
    bot.send_message(message.chat.id, 'Фильм не найден.')

# Обновление информации о фильме
def update_movie(message, movie):
    try:
        movie_data = message.text.split(',')
        title, year, genre = movie_data[0].strip(), movie_data[1].strip(), movie_data[2].strip()

        movie.update({'title': title, 'year': year, 'genre': genre})
        save_movies(user_movies)
        bot.send_message(
            message.chat.id, 
            f'Фильм обновлен: {title} ({year}, {genre})'
        )
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка в формате данных. Попробуйте снова.')

# Обработка неизвестных команд
@bot.message_handler(func=lambda message: True)
def fallback(message):
    bot.send_message(
        message.chat.id, 
        'Извините, я не понял команду. Пожалуйста, используйте /start для начала работы.'
    )

# Запуск бота
bot.polling()