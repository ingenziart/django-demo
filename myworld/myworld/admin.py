from .models import movie
from django.contrib import admin
from .models import me

admin.site.register(movie)
admin.site.register(me)
