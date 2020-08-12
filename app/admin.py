from django.contrib import admin

# Register your models here.
from app.models import Test,News


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class TestNews(admin.ModelAdmin):
    list_display = ('id', 'title','tag','up','views','content')

admin.site.register(Test,TestAdmin)
admin.site.register(News,TestNews)
