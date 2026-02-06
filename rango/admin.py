from django.contrib import admin
from rango.models import Category,Page

class PageAdmin(admin.ModelAdmin):

    list_display = ('title', 'category', 'url')

admin.site.register(Category)  #zhu ce moXing,ran ta houTai xianShi
admin.site.register(Page,PageAdmin)

# Register your models here.
