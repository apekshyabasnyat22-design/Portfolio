
from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactForm


def home(request):
    projects = Project.objects.all()

    return render(
        request,
        'portfolio/home.html',
        {'projects': projects}
    )


def projects(request):
    all_projects = Project.objects.all()

    return render(
        request,
        'portfolio/projects.html',
        {'projects': all_projects}
    )


def about(request):
    return render(request, 'portfolio/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(
        request,
        'portfolio/contact.html',
        {'form': form}
    )


def contact_success(request):
    return render(request, 'portfolio/contact_success.html')