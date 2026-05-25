import re
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class signUp(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Raise_issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Solution(models.Model):
    add_solution = models.TextField()

class Voting(models.Model):
    approver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approved_issues', null=True, blank=True)
    rejector = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rejected_issues', null=True, blank=True)