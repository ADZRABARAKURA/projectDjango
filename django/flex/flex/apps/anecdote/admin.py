from django.contrib import admin

from .models import Anecdote, Comment

admin.site.register(Anecdote)
admin.site.register(Comment)
