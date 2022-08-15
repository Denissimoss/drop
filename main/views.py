from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm
from .models import Name


def create(request):

    if request.method == 'POST':

        form = NameForm(request.POST)

        if form.is_valid():
            # Сохранение формы
            form.save()

            # Редирект на ту же страницу
            return HttpResponseRedirect(request.path_info)

    else:
    # метод GET

        form = NameForm()

        # Получение всех имен из БД.
        names = Name.objects.all()

    # И добавляем names в контекст, чтобы плучить к ним доступ в шаблоне
    return render(request, 'name.html', {'form': form, 'names': names})