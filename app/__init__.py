from django.apps import AppConfig
import os


#重写类IndexConfig
class IndexConfig(AppConfig):
    verbose_name = '网站首页'       #这个就是汉化后的名称。
