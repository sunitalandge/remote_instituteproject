from django.shortcuts import render
from .models import ContactData,FeedbackData
from .forms  import ContactForm,FeedbackForm

def home(request):
    return render(request,'institute_home.html')

def contact(request):
    if request.method == "POST":
        cform = ContactForm(request.POST)
        if cform.is_valid():
            name = cform.cleaned_data.get('name','')
            email = cform.cleaned_data.get('email','')
            mobile = cform.cleaned_data.get('mobile','')
            courses = cform.cleaned_data.get('courses','')
            location = cform.cleaned_data.get('location','')
            shift = cform.cleaned_data.get('shift','')

            data = ContactData(
                name=name,
                email=email,
                mobile=mobile,
                courses=courses,
                location=location,
                shift=shift
            )
            data.save()
            cform = ContactForm()
            return render(request,'institute_contact.html',{'cform':cform})
    else:
        cform = ContactForm()
        return render(request,'institute_contact.html',{'cform':cform})

def services(request):
    return render(request,'institute_services.html')

import datetime as dt
date1 = dt.datetime.now()

def feedback(request):
    if request.method == "POST":
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get('name','')
            rating = request.POST.get('rating','')
            feedback = request.POST.get('feedback','')

            data = FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            fform = FeedbackForm()
            feedbacks = FeedbackData.objects.all()
            return render(request, 'institute_feedback.html', {'fform': fform,'feedbacks':feedbacks})
    else:
        fform = FeedbackForm()
        feedbacks = FeedbackData.objects.all()
        return render(request,'institute_feedback.html',{'fform':fform,'feedbacks':feedbacks})

def gallery(request):
    return render(request,'institute_gallery.html')