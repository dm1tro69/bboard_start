from django.db import models

# Create your models here.

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='название')

    class Meta:
        verbose_name = 'рубрика'
        verbose_name_plural = 'рубрики'
        ordering = ('name',)

    def __str__(self):
        return self.name



class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, null=True)

    class Meta:
       verbose_name = 'обьявление'
       verbose_name_plural = 'обьявления'
       ordering = ('-published',)

    def __str__(self):
        return self.title


