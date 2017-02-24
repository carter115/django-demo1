# coding=utf-8
from django.shortcuts import render, redirect
from .models import Block
from .models import Article
from .forms import ArticleForm

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
    if request.method == "GET":
        return render(request, 'article_create.html', {"b": block})
    else:
        form =ArticleForm(request.POST)
        if form.is_valid():
            article=form.save(commit=False)
            article.block=Block
            article.status=0
            article.save()
            return redirect("/article/list/%s" % block_id)
        else:
            return render(request,'article_create.html',{"b":block,"form":form})

