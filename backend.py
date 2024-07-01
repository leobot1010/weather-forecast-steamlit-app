import requests

API_KEY = "f9f25325c8cca7617edd8440c5573969"


def get_user_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    request = requests.get(url)
    print(request)
    data = request.json()
    filtered = data['list']    # filter the list dict out of all the data
    filtered_data = filtered[: 8 * forecast_days]    # extract user queried no. of days
    return filtered_data


if __name__ == '__main__':
    print(get_user_data(place="Dubli", forecast_days=1))

