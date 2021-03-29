import requests






def weath():
    city_id = 536203
    appid = "c7f46481225dc2d017777889f32e4fb7"
    res = requests.get ("https://api.openweathermap.org/data/2.5/forecast",
                        params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})

    data = res.json ()


    temp_condition = data['list']

    test_list = []
    for item in list(temp_condition):
        test_list.append(item['main']['temp'])
        test_list.append(item['weather'][0]['description'])
    return test_list





