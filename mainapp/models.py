from django.db import models

# Create your models here.

class Profile(models.Model):
    pic = models.ImageField()
    role = models.CharField(max_length=500)
    aboutme = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return self.role

class Skill(models.Model):
    logo = models.ImageField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    image = models.ImageField()
    project_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    techstack = models.CharField(max_length=500)
    github_link = models.CharField(max_length=200)

    def __str__(self):
        return self.project_name