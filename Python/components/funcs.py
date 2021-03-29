import sqlite3


def connect_db(income_func):
	def wrapper(sql_command):
		conn  = sqlite3.connect('test_base.db')
		cur = conn.cursor()
		result = income_func(cur, sql_command)

		conn.commit()
		conn.close()
		return result

	return wrapper



@connect_db
def get_music_info(cur, sql_command):
	cur.execute(sql_command)
	res = cur.fetchall()
	return res
	pass


sel_all_artists = 'SELECT * FROM bands'
sel_band_info = 'SELECT * FROM bands WHERE name ={}'
sel_band_songs = 'SELECT * FROM songs WHERE artist ={}'

#print(get_artist(sel_all_artists))
