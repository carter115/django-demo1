# coding=utf-8
from django.shortcuts import render, redirect
from .models import Block
from .models import Article


# Create your views here.
def index(request):
    block_infos = Block.objects.all().order_by("id")
    return render(request, 'index.html', {"blocks": block_infos})


def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    article_objs = Article.objects.filter(block=block, status=0).order_by("id")
    return render(request, 'article_list.html', {"articles": article_objs, "b": block})


def article_create(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    article_objs = Article.objects.filter(block=block, status=0).order_by("id")
    if request.method == "GET":
        return render(request, 'article_create.html', {"b": block})
    else:
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not title or not content:
            return render(request, 'article_create.html', {"b": block, "error": "标题或内容不能为空.","title":title,"content":content})
        elif len(title) > 100 or len(content) > 1000:
            return render(request, 'article_create.html', {"b": block, "error": "标题或内容超过100或1000字符.","title":title,"content":content})
        else:
            article = Article(block=block, title=title, content=content, status=0)
            article.save()
            return redirect("/article/list/%s" % block_id)
