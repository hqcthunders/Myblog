from django.db import models
# from redactor.fields import RedactorField
# Create your models here.


class Post(models.Model):
    title_post = models.CharField(max_length=30)
    content_post = models.TextField()
    date_post = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30, default='HQCThunders')
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title_post


'''
class PostRedactor(models.Model):
    title_redactor = models.CharField(max_length=30)
    short_text = RedactorField(
        verbose_name=u'Text',
        redactor_options={'lang': 'en', 'focus': True},
    )
'''