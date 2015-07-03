__author__ = 'leia'
from django.contrib import admin
from rango.models import Category, Page, UserProfile, JssorMedia




class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(JssorMedia)