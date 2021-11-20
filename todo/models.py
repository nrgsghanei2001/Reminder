from django.db import models
from django import forms


class Task(models.Model):
    categories = (
        ("1", "University"),
        ("2", "Maktab"),
        ("3", "Usual life"),
        ("4", "entertainment"),
        ("5", "others"),
    )

    title = models.CharField(max_length=100, blank=False)
    explanation = models.TextField(blank=False)
    category = models.CharField(max_length=1, choices=categories, default="1")
    priority = models.IntegerField(blank=False)
    deadline = models.DateField(blank=False)

    def __str__(self) -> str:
        return self.title
