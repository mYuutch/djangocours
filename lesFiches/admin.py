from django.contrib import admin
from django.utils.html import format_html
from lesFiches.models import MovieCard, Acteur, Realisateur

@admin.register(Acteur)
class ActeurAdmin(admin.ModelAdmin):
    list_display =('nom', 'prenom')


@admin.register(Realisateur)
class RealisateurAdmin(admin.ModelAdmin):
    list_display =('nom', 'prenom')


@admin.register(MovieCard)
class MovieCardAdmin(admin.ModelAdmin):
    list_display =('titre', 'date_sortie', 'realisateur')

    @admin.display(empty_value="pas de note")
    def view_note(self, obj):
        if obj.note>10:
            color = 'green'
        else:
            color = 'red'
        return format_html('<span style="color: {}">{}</span>'.format(color, obj.note)) 
# Register your models here.
