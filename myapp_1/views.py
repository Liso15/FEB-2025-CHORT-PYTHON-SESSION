import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class CurrentWeatherView(APIView):
    def get(self, request):
        city = request.GET.get('city', 'London')
        api_key = "YOUR_OPENWEATHERMAP_API_KEY"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        return Response(response.json())