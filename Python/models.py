from config import cursor

def get_music_info():
    cursor.execute ("SELECT * FROM `films`")
    data = cursor.fetchall()

    return data
print(get_music_info())










