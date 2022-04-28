from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL # auth.User

# lets us explicitly set upload path and filename
def upload_to_images(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# lets us explicitly set upload path and filename
def upload_to_certificates(instance, filename):
    return 'certificates/{filename}'.format(filename=filename)

class Portfolio(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=False,null=False)
    image = models.ImageField(upload_to=upload_to_images, blank=True, null=True)
    date_of_birth = models.DateField(blank=False,null=False)
    city = models.CharField(blank=False,null=False,max_length=25)
    adr = models.CharField(blank=False,null=False,max_length=50)
    nationality = models.CharField(blank=False,null=False,max_length=25)
    dev_start = models.DateField(blank=False,null=False)
    

class JobTitle(models.Model):
    title = models.CharField(blank=False,null=False,max_length=50)
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)

class Language(models.Model):
    name = models.CharField(blank=False,null=False,max_length=25)
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)

class Skill(models.Model):
    name = models.CharField(blank=False,null=False,max_length=25)
    pourcentage = models.FloatField(default=0,blank=False,null=False)
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)

class Education(models.Model):
    name = models.CharField(blank=False,null=False,max_length=100)
    type = models.CharField(blank=True,null=True,max_length=100)
    place = models.CharField(blank=False,null=False,max_length=100)
    date_start = models.DateField(blank=False,null=False)
    date_end = models.DateField(blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    certificate = models.FileField(upload_to=upload_to_certificates, blank=True, null=True)
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)

class Experience(models.Model):
    name = models.CharField(blank=False,null=False,max_length=50)
    work_type = models.CharField(blank=False,null=False,max_length=50)
    date_start = models.DateField(blank=False,null=False)
    date_end = models.DateField(blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)

class ProjectType(models.Model):
    name = models.CharField(blank=False,null=False,max_length=20)

class Project(models.Model):
    name = models.CharField(blank=False,null=False,max_length=50)
    description = models.TextField(blank=False,null=False)
    client = models.CharField(blank=False,null=False,max_length=50)
    project_type = models.ForeignKey(ProjectType,on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)

class Stack(models.Model):
    name = models.CharField(blank=False,null=False,max_length=50)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,blank=True)

class Upload(models.Model):
    image = models.ImageField(upload_to=upload_to_images, blank=True, null=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)