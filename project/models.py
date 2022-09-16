from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Courses(models.Model):
    courseTitle = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    course_pic =  models.FileField(blank=True, null=True, upload_to="upload/")
    start_date = models.DateField()
    duration = models.CharField(max_length=50)
    
    def __str__(self):
        return self.courseTitle
    
    

class Authors(models.Model):
    name = models.CharField(max_length=100)
    author_pic = models.FileField(blank=True, null=True, upload_to="upload/")
    price = models.DecimalField(max_digits= 10, decimal_places = 2)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    # course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Registration(models.Model):
    creg = models.ForeignKey(Courses, on_delete=models.CASCADE)
    reg_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.creg
    
    
class Review(models.Model):
    fullname = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    review = models.CharField(max_length=200)
    rating = models.CharField(max_length=5)
    def __str__(self):
        return self.fullname
    
    
class ContactUs(models.Model):
    fullname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    messages = models.CharField(max_length=200)
    def __str__(self):
        return self.fullname
    
    
class Profile(models.Model):
    GENDER = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=7, choices=GENDER)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=30)
    profile_pic = models.FileField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.fname
    