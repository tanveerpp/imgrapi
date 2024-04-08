from django.shortcuts import render
import requests
def useapi(request):
    data=requests.get('https://mejevo.pythonanywhere.com/emps/')
    d=data.json()
    return render(request,'index.html',{'data':d})
