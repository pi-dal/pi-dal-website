from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
from django.utils import timezone
from django.urls import reverse
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='类别')
    class Meta:
        verbose_name = '类别'
        verbose_name_plural = '类别'
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='标签')
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'
class Tutorial(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    title = models.CharField(max_length=100, verbose_name='题目')
    text = MDTextField(verbose_name='正文')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='类别')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    create = models.DateTimeField(default=timezone.now, verbose_name='创造时间')
    update = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    def get_absolute_url(self):
        return reverse('tutorial:detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ('-create',)
        verbose_name = '教程'
        verbose_name_plural = '教程'
    def __str__(self):
        return self.title

