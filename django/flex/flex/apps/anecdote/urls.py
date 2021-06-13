from django.urls import path

from . import views

app_name = 'anecdote'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:anecdote_id>/', views.detail, name='detail'),
    path('<int:anecdote_id>/leave_comment/', views.leave_comment, name='leave_comment'),
]
