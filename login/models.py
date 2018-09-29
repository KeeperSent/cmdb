from django.db import models

# Create your models here.


class M_User(models.Model):

    gender = (
        ('male', '男性'),
        ('female', '女性'),
    )

    name = models.CharField(max_length=128, unique=True, verbose_name='user')
    password = models.CharField(max_length=256, verbose_name='passwd')
    email = models.EmailField(unique=True, verbose_name='mail')
    sex = models.CharField(choices=gender, max_length=32, default='男性', verbose_name='gender')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='inited')
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']
        verbose_name = 'user'
        verbose_name_plural = 'user'




