from django.db import models
from user.models import User

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    completion_at = models.DateField(default=None)
    
    def __str__(self):
        return str(self.title)
    