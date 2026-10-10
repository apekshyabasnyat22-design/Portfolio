import logging

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .models import Project, Certification, Experience
from .forms import ContactForm


logger = logging.getLogger(__name__)


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
            contact_message = form.save()

            subject = (
                f"Portfolio Contact: {contact_message.subject}"
            )

            message = (
                f"You received a new message through your portfolio.\n\n"
                f"Name: {contact_message.name}\n"
                f"Email: {contact_message.email}\n"
                f"Reason: {contact_message.get_reason_display()}\n"
                f"Subject: {contact_message.subject}\n\n"
                f"Message:\n{contact_message.message}\n"
            )

            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                    reply_to=[contact_message.email],
                )
            except Exception:
                logger.exception(
                    "Contact form email could not be sent."
                )

                form.add_error(
                    None,
                    "Your message was saved, but the email "
                    "could not be sent. Please try again later "
                    "or contact me on LinkedIn."
                )

                return render(
                    request,
                    'portfolio/contact.html',
                    {'form': form}
                )

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