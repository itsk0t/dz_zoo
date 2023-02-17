from .models import AnimalList
from django.forms import ModelForm, TextInput, Textarea

class AnimalListForm(ModelForm):
    class Meta:
        model = AnimalList
        fields = ['name', 'type', 'animal_cl', 'intro', 'text']

        widgets = {
            "name": TextInput(attrs={
                'placeholder': 'Имя животного'
            }),

            "type": TextInput(attrs={
                'placeholder': 'Тип животного'
            }),

            "animal_cl": TextInput(attrs={
                'placeholder': 'Класс'
            }),

            "intro": TextInput(attrs={
                'placeholder': 'Краткое описание'
            }),

            "text": Textarea(attrs={
                'placeholder': 'Полное описание'
            })
        }