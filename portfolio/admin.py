from django.contrib import admin
from .models import Project, Certification, Experience, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'created_at')


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'completion_date')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'role',
        'organization',
        'experience_type',
        'start_date',
        'end_date',
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')