import json

from django.core import serializers
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

from app.models import Test, News, HasView, User, Tag


def hello(request):
    return HttpResponse("Hello world ! ")


def test(request):
    articles = Test.objects.all()
    return JsonResponse({
        'code': '0000',
        'data': [a.to_dict() for a in articles],
        'msg': '获取文章列表成功'
    })


def tags(request):
    return JsonResponse({
        'code': 0,
        'data': [a.name for a in Tag.objects.all()],
        'msg': 'sucess'
    })


def newsList(request):
    type = request.GET.get('type', '娱乐')
    page = int(request.GET.get('page', '1'))
    unionid = request.GET.get('unionid', '')
    user = User.objects.filter(unionid=unionid).first()
    if not user:
        User.objects.create(unionid=unionid)
    all = News.objects.exclude(id__in=[v.news.id for v in HasView.objects.filter(user__unionid=unionid).all()]).filter(
        type=type).order_by('-id').all()[(page - 1) * 5:page * 5]
    return JsonResponse({
        'code': 0,
        'data': dict(news=[a.to_dict(ext_props=['imgs'], exc_props=['images', 'content', 'status']) for a in all],
                     page=page, type=type),
        'msg': 'sucess'
    })


def detail(request):
    id = request.GET.get('id', '')
    unionid = request.GET.get('unionid', '')
    one = News.objects.get(id=id)
    one.views += 1
    one.save()
    has = HasView.objects.filter(user__unionid=unionid, news_id=id).first()
    if not has:
        HasView.objects.create(news_id=id, user=User.objects.filter(unionid=unionid).first())
    return JsonResponse({
        'code': 0,
        'data': one.to_dict(ext_props=['imgs'], exc_props=['images', 'status']),
        'msg': 'sucess'
    })


def recommend(request):
    unionid = request.GET.get('unionid', '')
    all = News.objects.exclude(
        id__in=[v.news.id for v in HasView.objects.filter(user__unionid=unionid).all()]).order_by('-views').all()[0:10]
    return JsonResponse({
        'code': 0,
        'data': [a.to_dict(ext_props=['imgs'], exc_props=['images', 'content', 'status']) for a in all],
        'msg': 'sucess'
    })
