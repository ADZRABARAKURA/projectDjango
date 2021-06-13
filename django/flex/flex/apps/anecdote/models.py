import datetime
from django.db import models

from django.utils import timezone

class Anecdote(models.Model):
    anecdote_title = models.CharField('Название статьи', max_length = 200)
    anecdote_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.anecdote_title

    def was_published_recently(self):
            return self.pub_date >= (timezone.now() - datatime.timedelta(days = 7))
    class Meta:
            verbose_name = 'Анекдот'
            verbose_name_plural = 'Анекдоты'

class Comment(models.Model):
    anecdote = models.ForeignKey(Anecdote, on_delete = models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.CharField('текст комментария', max_length = 200)
    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
