from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300)
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True
    )
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Certification(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    completion_date = models.CharField(max_length=100, blank=True)
    image = models.ImageField(
        upload_to='certifications/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class Experience(models.Model):
    role = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    experience_type = models.CharField(
        max_length=100,
        blank=True
    )
    description = models.TextField()
    start_date = models.CharField(max_length=100, blank=True)
    end_date = models.CharField(max_length=100, blank=True)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.role} - {self.organization}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"