from django.db import models

# Create your models here.

import uuid
from django.utils.text import slugify

class Film(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # uuid en lugar de id clásica autoincremental
    title = models.CharField(max_length=150, verbose_name="Título")
    year = models.PositiveIntegerField(default=2000, verbose_name="Año")
    review_short = models.TextField(
    null=True, blank=True, verbose_name="Argumento (corto)")
    review_large = models.TextField(null=True, blank=True, verbose_name="Historia (largo)")
    trailer_url = models.URLField(max_length=150, null=True, blank=True, verbose_name="URL youtube")
    genres = models.ManyToManyField( 'FilmGenre', related_name="film_genres",verbose_name="Géneros")

    class Meta:
        verbose_name = "Película"
        ordering = ['title']

    def __str__(self):
        return f'{self.title} ({self.year})'

class FilmGenre(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre", unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "género"
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(FilmGenre, self).save(*args, **kwargs)