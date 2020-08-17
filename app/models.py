from django.db import models
from tinymce.models import HTMLField
# Create your models here.
from app.base import IdModel


class Test(IdModel):
    name = models.CharField('名称', max_length=20)

class Tag(IdModel):
    name = models.CharField('标签分类', max_length=20)

class User(IdModel):
    unionid = models.CharField('百度unionid', max_length=255,unique=True,db_index=True)


class Img(IdModel):
    url = models.CharField('图片地址', max_length=512)


class News(IdModel):
    title = models.CharField('标题', max_length=64)
    images = models.ManyToManyField(Img, verbose_name='新闻封面')
    tag = models.CharField('标签', max_length=64)
    up = models.CharField('作者', max_length=64)
    type = models.CharField('类型', max_length=64)
    views = models.IntegerField(verbose_name='阅读量', default=0, null=True)
    content = HTMLField()
    status = models.IntegerField(verbose_name='是否上线', default=0, null=True)

    @property
    def imgs(self):
        return [photo.url for photo in self.images.all()]


class HasView(IdModel):
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE, null=True)
    news = models.ForeignKey(News, verbose_name="新闻", on_delete=models.CASCADE, null=True)
