data = [{
    'dt': 1719576000,
    'main': {'temp': 295.07, 'feels_like': 295.82, 'temp_min': 293.99, 'temp_max': 295.07, 'pressure': 1009,
             'sea_level': 1009, 'grnd_level': 1007, 'humidity': 96, 'temp_kf': 1.08}

}]


sky_conditions = ["Clear", "Clear", "Cloud", "Rain", "Rain", "Clear"]

images = {"Clear": "images/clear.png", "Cloud": "images/clouds.png",
          "Rain": "images/rain.png", "Snow": "images/snow.png"}


result = [images[i] for i in sky_conditions]

print(result)