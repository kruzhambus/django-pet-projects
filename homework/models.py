from django.db import models

# Create your models here.

class Homework(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    group = models.IntegerField()
    body_text = models.TextField(verbose_name="Содержимое")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновление публикации")
    specifications = models.FileField(upload_to="photos/%Y/%m/%d/", verbose_name="Документ")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    link = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Домашка"
        verbose_name_plural= "Домашка"
        ordering = ['-created_at']

