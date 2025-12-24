from django.db import models
from employees.models import Employee

class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
