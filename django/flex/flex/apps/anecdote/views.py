from django.http import Http404, HttpResponseRedirect

from django.shortcuts import render
from django.urls import reverse

from .models import Anecdote, Comment


def index(request):
    latest_anecdote_list = Anecdote.objects.order_by('pub_date')[:5]
    return render(request, 'anecdote/list.html', {'latest_anecdote_list': latest_anecdote_list})

def detail(request, anecdote_id):
    try:
        a = Anecdote.objects.get(id = anecdote_id)
    except:
        raise Http404("анекдот не найден")
    latest_comments_list = a.comment_set.order_by('id')[:10]
    return render(request, 'anecdote/detail.html', {'anecdote': a, 'latest_comments_list' : latest_comments_list})
def leave_comment(request,anecdote_id):
        try:
            a = Anecdote.objects.get(id = anecdote_id)
        except:
            raise Http404("анекдот не найден")
        a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

        return HttpResponseRedirect(reverse('anecdote:detail', args = (a.id,)))
