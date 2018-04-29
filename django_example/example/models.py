from django.db import models

# Create your models here.


class Form(models.Model):
    principal_name = models.TextField()
    teacher_name = models.TextField()
