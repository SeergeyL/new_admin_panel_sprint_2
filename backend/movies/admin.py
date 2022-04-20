from django.contrib import admin
from .models import Filmwork, Genre, Person, GenreFilmwork, PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmwork


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline, PersonFilmworkInline)

    list_display = ('title', 'type', 'creation_date', 'rating',)
    list_filter = ('type',)
    search_fields = ('title', 'description', 'id')

    def get_queryset(self, request):
        qs = super().get_queryset(request) \
            .prefetch_related('persons') \
            .prefetch_related('genres')
        return qs


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
