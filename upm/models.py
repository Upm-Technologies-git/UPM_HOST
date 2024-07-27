from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    text = models.TextField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Newsletter1(models.Model):
    email = models.CharField(max_length=255)
    
    def __str__(self):
        return f'User {self.email or ""}'
    
class Newsletter2(models.Model):
    email = models.CharField(max_length=255)
    
    def __str__(self):
        return f'User {self.email or ""}'
    