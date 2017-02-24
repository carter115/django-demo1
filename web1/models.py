# coding=utf-8
from django.db import models


# Create your models here.
class Block(models.Model):
    name = models.CharField("模块名称", max_length=100)
    desc = models.CharField("模块描述", max_length=1000)
    manager = models.CharField("管理员", max_length=100)
    status = models.IntegerField("状态", choices=((0, "正常"), (-1, "删除")), default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "模块列表"
        verbose_name_plural = "模块列表"


class Article(models.Model):
    block = models.ForeignKey(Block, verbose_name="模块ID")
    title = models.CharField("文章名称", max_length=100)
    content = models.CharField("文章内容", max_length=1000)
    status = models.IntegerField("状态", choices=((0, "正常"), (1, "删除")))
    create_time = models.DateTimeField("创建时间",auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章列表"
        verbose_name_plural = "文章列表"
