from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import uuid
from django.utils import timezone

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    status=models.CharField(max_length=2000,blank=True,null=True, default="Student")
    image_profile=models.ImageField(null=True, blank=True, default='blank.png',upload_to='user_profile/')
    shortBio=models.CharField(max_length=2000, blank=True, null=True)
    detail=RichTextField(null=True, blank=True)
    github=models.URLField(null=True, blank=True)
    youtube=models.URLField(null=True, blank=True)
    twitter=models.URLField(null=True, blank=True)
    facebook=models.URLField(null=True, blank=True)
    instagram=models.URLField(null=True, blank=True)
    linkedin=models.URLField(null=True, blank=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True , primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class Organization(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

class Teacher(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

class Student(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    

class Tags(models.Model):
    name=models.CharField(max_length=2000,blank=True, null=True)
    
class Course(models.Model):
    name = models.CharField(max_length=2000,blank=True,null=True)
    organisation = models.ForeignKey(Organization, on_delete=models.CASCADE)
    teacher=models.ManyToManyField(Teacher, blank=True, null=True)
    students=models.ManyToManyField(Student,blank=True, null=True)
    tags=models.ManyToManyField(Tags, blank=True, null=True)
    description=RichTextField(null=True, blank=True)
    image_course=models.ImageField(null=True, blank=True, default='blank.png',upload_to='course/')
    price = models.DecimalField(null=True, blank=True, default=0, max_digits=100, decimal_places=2)
    small_description = models.TextField(null=True, blank=True)
    description=RichTextField(null=True, blank=True)
    learned = RichTextField(null = True, blank = True)


class Module(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=2000,blank=True,null=True)
    description=RichTextField(null=True, blank=True)

class Video(models.Model):
    video=models.FileField(null=True, blank=True)
    module=models.ForeignKey(Module, on_delete=models.CASCADE, blank=True, null=True)

class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    description=RichTextField(null=True, blank=True)


class SubComment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE,null=True,blank=True)
    description=RichTextField(null=True, blank=True)

class Notes(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    description=RichTextField(null=True, blank=True)    

class Monitor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    ip=models.CharField(max_length=2000,blank=True,null=True)
    country=models.CharField(max_length=2000,blank=True,null=True)
    city=models.CharField(max_length=2000,blank=True,null=True)
    region=models.CharField(max_length=2000,blank=True,null=True)
    timeZone=models.CharField(max_length=2000,blank=True,null=True)