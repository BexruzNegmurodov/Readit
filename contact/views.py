from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been accepted')
            return redirect('contact:contact')
    ctx = {
        'form': form
    }
    return render(request, 'contact/contact.html', ctx)
