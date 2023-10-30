from django.db import models


class Articles(models.Model):

    objects = True
    title = models.CharField('название', max_length=50)
    anons = models.CharField('анонс', max_length=250)
    full_text = models.TextField('статья')
    date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
