from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='')

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name

class ItemBase(models.Model):
    class Meta:
        abstract = True
    subject = models.CharField(max_length=100, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class Course(ItemBase):
    class Meta:
        unique_together = ('subject', 'category')
    descreption = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models . SET_NULL, null=True)

class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject','course')
        db_table =
    content = models.TextField()
    image = models.ImageField(upload_to='courses/%Y/%m')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)