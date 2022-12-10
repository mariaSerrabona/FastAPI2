# Generated by Django 3.1.2 on 2020-10-24 20:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilmGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'género',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('year', models.PositiveIntegerField(default=2000, verbose_name='Año')),
                ('review_short', models.TextField(blank=True, null=True, verbose_name='Argumento (corto)')),
                ('review_large', models.TextField(blank=True, null=True, verbose_name='Historia (largo)')),
                ('trailer_url', models.URLField(blank=True, max_length=150, null=True, verbose_name='URL youtube')),
                ('genres', models.ManyToManyField(related_name='film_genres', to='films.FilmGenre', verbose_name='Géneros')),
            ],
            options={
                'verbose_name': 'Película',
                'ordering': ['title'],
            },
        ),
    ]