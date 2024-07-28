from django.shortcuts import render, redirect
from .models import contact, Newsletter1, Newsletter2
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        
        myuser = Newsletter1.objects.create(email=email)
        myuser.save()
        return redirect("index")
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            
            html = render_to_string("newcontact.html",{
                'name':name,
                'email':email,
                'text':text,
            })
            send_mail('The contact form subject', 'This is the message', 'noreply@mohanrajlenova.com', ['mohanrajlenova@gmail.com'], html_message=html)
            form.save()                    
            messages.info(request, "Message Sent Successfully")
            return redirect('contact')
    return render(request, "contact.html", {'form':form})

def project(request):
    return render(request, "project.html")

def service(request):
    return render(request, "service.html")

def team(request):
    return render(request, "team.html")


def r404(request):
    return render(request, "404.html")

def web(request):
    return render(request, "WebT.html")

def poster(request):
    return render(request, "posterT.html")