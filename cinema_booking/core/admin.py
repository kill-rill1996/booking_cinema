from django.contrib import admin
from .models import *

admin.site.register(Hall)
admin.site.register(Session)
admin.site.register(Ticket)
admin.site.register(Order)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
