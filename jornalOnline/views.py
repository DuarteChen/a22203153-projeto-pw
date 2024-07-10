from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Article, Comment, Rating
from .forms import ArticleForm, CommentForm, RatingForm

def contextFun(request):
    username = request.user.username if request.user.is_authenticated else 'Guest'
    context = {
        'anoAtual': datetime.today().year,
        'username': username,
    }
    return context

def article_list(request):
    articles = Article.objects.all()
    context = contextFun(request)
    context['articles'] = articles
    return render(request, 'jornalOnline/article_list.html', context)

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comment_form = CommentForm()
    context = contextFun(request)
    context['article'] = article
    context['comment_form'] = comment_form
    return render(request, 'jornalOnline/article_detail.html', context)

@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('jornalOnline:article_detail', article_id=article.id)
    else:
        form = ArticleForm()
    context = contextFun(request)
    context['form'] = form
    return render(request, 'jornalOnline/add_article.html', context)

@login_required
def add_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('jornalOnline:article_detail', article_id=article.id)
    else:
        form = CommentForm()
    context = contextFun(request)
    context['form'] = form
    return render(request, 'jornalOnline/add_comment.html', context)

@login_required
def add_rating(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.article = article
            rating.author = request.user
            rating.save()
            return redirect('jornalOnline:article_detail', article_id=article.id)
    else:
        form = RatingForm()
    context = contextFun(request)
    context['form'] = form
    return render(request, 'jornalOnline/add_rating.html', context)
