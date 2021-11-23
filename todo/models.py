from django.db import models
from django import forms

class Category(models.Model):
    categories = (
        ("1", "University"),
        ("2", "Maktab"),
        ("3", "Usual life"),
        ("4", "Entertainment"),
        ("5", "Others"),
    )

    category = models.CharField(max_length=1, choices=categories, default="1")

    def __str__(self) -> str:
        if (self.category == "1"):
            return "University"
        elif (self.category == "2"):
            return "Maktab"
        elif (self.category == "3"):
            return "Usual life"
        elif (self.category == "4"):
            return "Entertainment"
        elif (self.category == "5"):
            return "Others"


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


