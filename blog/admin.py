from django.contrib import admin
from .models import Post

admin.site.site_header = 'Блог'
admin.site.site_title = 'Блог'
admin.site.index_title = 'Добавление новостей'
admin.site.register(Post)
