from django.contrib import admin
from .models import Belonging,Borrowed,Friend
# Register your models here.

class BelongingAdmin(admin.ModelAdmin):
    list_display=('id','name')
    list_display_links=('id',)
    list_filter=('id','name')
    list_editable = ('name',)
    search_fields=('name',)
    list_per_page=25



admin.site.register(Belonging,BelongingAdmin)

class BorrowedAdmin(admin.ModelAdmin):
    list_display=('id','what','to_who','when','returned')
    list_display_links=('id',)
    list_filter=('id','what','to_who','when','returned')
    list_editable = ('what','to_who','returned')
    search_fields=('id','what','to_ who','when','returned')
    list_per_page=25

admin.site.register(Borrowed,BorrowedAdmin)

class FriendAdmin(admin.ModelAdmin):
    list_display=('id','name')
    list_display_links=('id',)
    list_filter=('id','name')
    list_editable = ('name',)
    search_fields=('name',)



admin.site.register(Friend,FriendAdmin)


