import requests
from django.shortcuts import render



def fetchapi(request):
   response = requests.get('http://127.0.0.1:8000/api/matchapi/')
   data=response.json()
   for d in data['results']:
      print(d)
   return render(request,'fetchapi.html',{'todos':data})
