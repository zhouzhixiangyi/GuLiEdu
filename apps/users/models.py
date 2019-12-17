from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    image = models.ImageField(upload_to='user/', max_length=200, verbose_name='用户头像', null=True, blank=True)
    nick_name = models.CharField(max_length=20, verbose_name='昵称', null=True, blank=True)
    birthday = models.DateField(verbose_name='用户生日', null=True, blank=True)
    gender = models.DateField(choices=(('girl', '女'), ('boy', '男')), max_length=10, verbose_name='用户性别', default='girl')
    address = models.CharField(max_length=200, verbose_name='用户地址', null=True, blank=True)
    phone = models.CharField(max_length=11, verbose_name='用户电话', null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class BannerInfo(models.Model):
    image = models.ImageField(upload_to='banner/', verbose_name='轮播图片', max_length=200)
    url = models.URLField(default='http://www.atguigu.com', verbose_name='图片链接', max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = '轮播图信息'
        verbose_name_plural = verbose_name


class EmailVerifyCode(models.Model):
    code = models.CharField(max_length=20, verbose_name='邮箱验证码')
    email = models.EmailField(max_length=200, verbose_name='验证码邮箱')
    type = models.CharField(choices=((1, 'register'), (2, 'forget'), (3, 'change')), verbose_name='验证码类型', max_length=10)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = '邮箱验证码信息'
        verbose_name_plural = verbose_name
