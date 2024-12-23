# Generated by Django 5.1.2 on 2024-11-21 12:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_blog', '0002_alter_category_parent_alter_tutorial_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='tutorial',
            options={'verbose_name': 'Навчальний матеріал', 'verbose_name_plural': 'Навчальні матеріали'},
        ),
        migrations.AddField(
            model_name='category',
            name='category_type',
            field=models.CharField(choices=[('tutorials', 'Навчальні матеріали'), ('text', 'Суцільний текст')], default='tutorials', max_length=15, verbose_name='Тип категорії'),
        ),
        migrations.AddField(
            model_name='category',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
