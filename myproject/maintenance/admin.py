from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Author)

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("body", )
    list_display = ["id", "title", "images"]
    list_editable = ["title"]

admin.site.register(Post,PostAdmin)

admin.site.register(Work_request)
