import json

from django.shortcuts import render
from app1.models import Links
from django.http import JsonResponse

def index_page(request):
    # вывод в консоль значений из БД(models)
    all_links = Links.objects.all()
    # print(all_links)
    # filtred_link = Links.objects.filter(description="Переводчик")
    # print(filtred_link)
    return render(request, 'index.html')

def history_page(request):
    all_links = Links.objects.all()
    return render(request, 'history.html', {'data': all_links})

def create(request):
    print (request.body)
    if request.method == "POST":
        data = json.loads(request.body)
        link = data['link']
        desc = data['description']
        links = Links()
        links.description = link
        links.link = desc
        links.save()
    return JsonResponse({'success': 'Успех'})