# coding=utf-8
from django.contrib import admin

# Register your models here.
from .models import Block,Article

class BlockAdmin(admin.ModelAdmin):
    list_display = ("name","desc","manager","status")

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("block_id","title","create_time","status")

admin.site.register(Block,BlockAdmin)
admin.site.register(Article,ArticleAdmin)