from django.shortcuts import render, redirect
from .models import (
    Coffee,
    Feedback,
)

def home(request):
    coffee = Coffee.objects.filter(is_about=False, is_blog=False)
    about = Coffee.objects.filter(is_about=True, is_blog=False).first()
    blogs = Coffee.objects.filter(is_about=False, is_blog=True)
    feedbacks = Feedback.objects.filter(is_approved=True)
    
    if request.method == 'POST':
        first_name = request.POST.get("name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        message = request.POST.get("message")
        feedback = Feedback(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            message=message
        )
        feedback.save()
        return redirect('home')
    
    context = {
        'coffees': coffee,
        'about': about,
        'blogs': blogs,
        'feedbacks': feedbacks,
    }
    return render(request, 'index.html', context)


def coffee1(request):
    coffee = Coffee.objects.filter(is_about=False, is_blog=False)


    context = {
            'coffees': coffee,
        }
    return render(request , 'coffees1.html', context)

def about(request):
    about = Coffee.objects.filter(is_about=True, is_blog=False).first()


    context = {
        'about': about,
    }
    return render(request , 'about.html', context)



def blog(request):
    blogs = Coffee.objects.filter(is_about=False, is_blog=True)


    context = {
        'blogs': blogs,
    }
    return render(request , 'blog.html', context)


def contact(request):
    feedbacks = Feedback.objects.filter(is_approved=True)

    if request.method == 'POST':
        first_name = request.POST.get("name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        message = request.POST.get("message")
        feedback = Feedback(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            message=message
        )
        feedback.save()
        return redirect('contact')
    
    context = {
        'feedbacks': feedbacks,
    }
    return render(request , 'contact.html', context)