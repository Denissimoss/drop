from re import U
from django.shortcuts import render
from django.http import  HttpResponseRedirect

from main.models import book





def create(request):
    people = book.objects.all()
    return render(request, "create.html", {"people": people})

# сохранение данных в бд
def index(request):
    if request.method == "POST":
        tom = book()
        people = book.objects.all()
        tom.name = request.POST.get("name")
        tom.author = request.POST.get("author")
        tom.number = request.POST.get("number")
        tom.save()
        return render(request, "delete.html", {"people": people})
        return HttpResponseRedirect("index/")
        