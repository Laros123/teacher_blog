from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    CATEGORY_TYPE_CHOICES = [
        ('tutorials', 'Навчальні матеріали'),
        ('text', 'Суцільний текст')
    ]

    category_type = models.CharField(
        max_length=15,
        choices=CATEGORY_TYPE_CHOICES,
        default='tutorials',
        verbose_name='Тип категорії'
    )
    title = models.CharField(max_length=127, verbose_name='Назва')
    parent = models.ForeignKey('Category', blank=True, null=True, on_delete=models.CASCADE, related_name='child', verbose_name='Батьківська категорія')
    text = RichTextField(default='', verbose_name='Текст')

    def __str__(self) -> str:
        if self.parent is None:
            return f'{self.title}'
        return f'{self.title} ({self.parent})'

    def get_absolute_url(self) -> str:
        return reverse('detail-category', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

class Tutorial(models.Model):
    title = models.CharField(max_length=127, verbose_name='Назва')
    text = RichTextField(verbose_name='Текст')
    file = models.FileField(upload_to="tutorials/", blank=True, null=True, verbose_name='Файл')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='tutorial', verbose_name='Категорія')

    def get_other_tutorials(self):
        return Tutorial.objects.filter(category__pk=self.category.pk).all()

    def get_absolute_url(self) -> str:
        return reverse('detail-tutorial', kwargs={'pk': self.category.pk, 'pkt': self.pk})

    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Навчальний матеріал"
        verbose_name_plural = "Навчальні матеріали"

