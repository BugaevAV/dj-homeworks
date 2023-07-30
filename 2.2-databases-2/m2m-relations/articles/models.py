from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):

    articles = models.ManyToManyField(Article, through='Scope')
    name = models.CharField(max_length=200, verbose_name='Имя тега')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
    
    def __str__(self) -> str:
        return self.name
    

class Scope(models.Model):

    article = models.ForeignKey(Article, related_name='scopes', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='scopes', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='ОСНОВНОЙ')

    class Meta:
        verbose_name = 'тэг статьи'
        verbose_name_plural = 'Тэги статьи'
        ordering = ['-is_main', 'tag']
