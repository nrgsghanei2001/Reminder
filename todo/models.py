from django.db import models
from django import forms


class Category(models.Model):

    category = models.CharField(max_length=3, unique=True)

    def __str__(self) :
        return self.category


class Task(models.Model):

    priorities = (
        ("High","1"),
        ("Medium","2"),
        ("Low","3"),
    )

    title = models.CharField(max_length=100, blank=False)
    explanation = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    priority = models.CharField(max_length=6, choices=priorities, default="Medium")
    deadline = models.DateField(blank=False)

    def __str__(self) -> str:
        return self.title


