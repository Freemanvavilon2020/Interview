from flask import Flask, render_template, request, url_for
import requests
from werkzeug.utils import redirect

import components





app = Flask (__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/movies')
def move():
    about_movie = components.movies_today
    return render_template('move.html', about_movie = about_movie)


@app.route('/courses')
def cours():
    courses = components.get_money()
    return render_template('cours.html', courses = courses)


@app.route('/weather', methods=['GET'])
def weather():
    about_weather = components.weath()
    return render_template('weather.html', about_weather = about_weather)

@app.route('/add_message', methods=['POST'])
def add_message():


    res = requests.get ('https://api.openweathermap.org/data/2.5/find?q=' + request.form['city'] +  '&type=like&units=metric&lang=ru&APPID=c7f46481225dc2d017777889f32e4fb7')
    data = res.json ()

    temp_condition = data['list']

    test_list = []

    for item in list (temp_condition):
        test_list.append (item['main']['temp'])
        test_list.append (item['main']['temp_min'])
        test_list.append (item['main']['temp_max'])
        test_list.append (item['weather'][0]['description'])


        return render_template ('weather.html', test=test_list)





@app.route('/user/<name>')
def user(name):
    return '<h1>Hellos %s !!!</h1>' % name


if __name__ == '__main__':
    app.run ()