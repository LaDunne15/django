# Generated by Django 4.0.3 on 2022-04-12 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія для публікації', 'verbose_name_plural': 'Категорії для публікацій'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, verbose_name='Слаг'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='app_blog.category', verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='article',
            name='main_page',
            field=models.BooleanField(default=False, help_text='Показувати на головній сторінці', verbose_name='Головна'),
        ),
    ]
