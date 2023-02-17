from django.db import models

class AnimalList(models.Model):
    #image = models.ImageField('Картинка')
    name = models.CharField('Имя животного', max_length=30)
    type = models.CharField('Название животного', max_length=30)
    animal_cl = models.CharField('Класс', max_length=30)
    intro = models.CharField('Краткое описание', max_length=300)
    text = models.TextField('Полное описание')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животны'