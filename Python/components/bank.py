import requests

moneyurl = 'https://www.nbrb.by/API/ExRates/Rates/Dynamics/145?startDate=2018-9-1&endDate=2018-12-30'
def get_parsed_page( moneyurl ):
    response = requests.get (moneyurl).json()
    date1 = []
    course = []

    for a in list(response):
        date1.append(a['Date'])
        course.append(a['Cur_OfficialRate'])

    return date1, course


print(get_parsed_page(moneyurl))

def get_money():


    url = 'https://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get (url).json ()

    test_list = []
    for p in list (response):

        z = p['Cur_Abbreviation']
        y = p['Cur_Name']
        x = p['Cur_OfficialRate']
        test_list += [z, y, x]
    return test_list


