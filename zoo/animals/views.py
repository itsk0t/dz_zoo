from django.shortcuts import render, redirect
from .forms import AnimalListForm
from .models import AnimalList
from django.views.generic import DetailView

def animals(request):
    animals = AnimalList.objects.all()
    return render(request, 'animals/animals_list.html', {'animals': animals})


class AnimalsDetailView(DetailView):
    model = AnimalList
    template_name = 'animals/animal_view.html'
    context_object_name = 'animal'


def create(request):
    error = ''
    if request.method == 'POST':
        form = AnimalListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animals')
        else:
            error = 'Формы былы неверной'

    form = AnimalListForm()

    data = {
        'form': form
    }

    return render(request, 'animals/create.html', data)