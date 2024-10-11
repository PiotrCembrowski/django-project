from django.contrib import admin
from blog.models import Post, Profile, Tag
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag