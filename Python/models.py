from config import cursor
#Получаем все фильмы
def get_music_info():
    cursor.execute ("SELECT * FROM `films`")
    data = cursor.fetchall()

    return data
print(get_music_info())










