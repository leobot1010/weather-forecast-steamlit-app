import requests

API_KEY = "f9f25325c8cca7617edd8440c5573969"


def get_user_data(place, forecast_days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    request = requests.get(url)
    data = request.json()
    filtered = data['list']    # filter the list dict out of all the data
    filtered_days = filtered[: 8 * forecast_days]    # extract user queried no. of days

    if kind == 'Temperature':
        kind_data = [i['main']['temp'] for i in filtered_days]
    elif kind == 'Sky':
        kind_data = [i['weather'][0]['main'] for i in filtered_days]
    # noinspection PyUnboundLocalVariable
    return kind_data


if __name__ == '__main__':
    x = get_user_data(place="Tokyo", forecast_days=1, kind='Sky')

print(x)