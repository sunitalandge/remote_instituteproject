from django.db import models
from multiselectfield import  MultiSelectField

class ContactData(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()

    COURSE_CHOICES = (
        ('python','Python'),
        ('django','Django'),
        ('api','API'),
        ('ui','UI'),
        ('flask','Flask')
    )
    courses = MultiSelectField(max_length=200, choices=COURSE_CHOICES)

    LOCATION_CHOICES = (
        ('hyd','Hyderabad'),
        ('bang','Bangalore'),
        ('che','Chennai')
    )
    location = MultiSelectField(max_length=200, choices=LOCATION_CHOICES)

    SHIFT_CHOICES = (
        ('morning','Morning'),
        ('afternoon','Afternoon'),
        ('evening','Evening'),
        ('night','Night')
    )
    shift = MultiSelectField(max_length=200, choices=SHIFT_CHOICES)






class FeedbackData(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    date = models.DateField()
    feedback = models.TextField(max_length=500)
