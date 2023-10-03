from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        API_key = 'daf7f070e9f003b5b6b90e25bfabc4c5'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}'
        response = requests.get(url)
        data = response.json()
        print(data)
        if data['cod'] == 200:
            return render(request,'weatherapp.html',{
            'data': data,
        })
        elif data['cod'] != 200 and data['cod'].isdigit():
            error_message = 'Invalid Ctiy, please enter a valid city name'
            return render(request,'weatherapp.html',{
                'error_message':error_message,
            })
    else:
        return render(request,'weatherapp.html')