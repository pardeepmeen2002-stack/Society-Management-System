from django.contrib import admin
from .models import signUp, Category, Raise_issue, Solution, Voting


# Register your models here.

admin.site.register(signUp)
admin.site.register(Category)
admin.site.register(Raise_issue)
admin.site.register(Solution)
admin.site.register(Voting)

class signUpAdmin(admin.ModelAdmin):
    list_display = ( 'email')

class signUp(admin.ModelAdmin):
    list_display = ('fullname')


