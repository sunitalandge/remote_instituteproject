from django import forms
from multiselectfield import MultiSelectFormField

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    email = forms.EmailField(
        label='Enter Your Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter Your Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Mobile Number'
            }
        )
    )

    COURSE_CHOICES = (
        ('python', 'Python'),
        ('django', 'Django'),
        ('api', 'API'),
        ('ui', 'UI'),
        ('flask', 'Flask')
    )
    courses = MultiSelectFormField(max_length=200, choices=COURSE_CHOICES)

    LOCATION_CHOICES = (
        ('hyd', 'Hyderabad'),
        ('bang', 'Bangalore'),
        ('che', 'Chennai')
    )
    location = MultiSelectFormField(max_length=200, choices=LOCATION_CHOICES)

    SHIFT_CHOICES = (
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('night', 'Night')
    )
    shift = MultiSelectFormField(max_length=200, choices=SHIFT_CHOICES)







class FeedbackForm(forms.Form):
    name = forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    rating = forms.IntegerField(
        label='Enter Your Rating',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )
    feedback = forms.CharField(
        label='Enter Your Feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback'
            }
        )
    )