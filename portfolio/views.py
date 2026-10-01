from django.shortcuts import render, redirect
from .models import Project, Certification, Experience
from .forms import ContactForm


def home(request):
    projects = Project.objects.all()
    experiences = Experience.objects.all()

    return render(
        request,
        'portfolio/home.html',
        {
            'projects': projects,
            'experiences': experiences,
        }
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


def skills(request):
    return render(request, 'portfolio/skills.html')


def certifications(request):
    all_certifications = Certification.objects.all()

    return render(
        request,
        'portfolio/certifications.html',
        {'certifications': all_certifications}
    )


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
    return render(
        request,
        'portfolio/contact_success.html'
    )