from django.contrib import admin
from .models import Post
# from django import forms
# from redactor.widgets import RedactorEditor
# from blog.models import PostRedactor
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title_post', 'date_post']
    list_filter = ['date_post']
    search_fields = ['id']


'''
class EntryAdminForm(forms.ModelForm):
    class Meta:
        model = PostRedactor
        widgets = {
            'short_text': RedactorEditor(),
        }
        fields = "__all__"


class EntryAdmin(admin.ModelAdmin):
    form = EntryAdminForm
'''

admin.site.register(Post, PostAdmin)
