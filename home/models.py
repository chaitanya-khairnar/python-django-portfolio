from django.db import models
# from typing import Dict


# Create your models here.
class General_info(models.Model):
    """Model to accept general information of a candidate

    Args:
        models (_type_): Subclass of model

    Returns:
        (str): _description_
    """
    profile_pic = models.ImageField(upload_to='images/', null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    contact_num = models.CharField(max_length=30)
    e_mail = models.EmailField(max_length=50)
    birth_date = models.DateField()
    location = models.CharField(max_length=50)
    summary = models.TextField(max_length=1000, blank=True, null=True)
    skills = models.TextField(max_length=500, blank=True, null=True)
    # programming = models.TextField(max_length=1000, blank=True, null=True)
    # tools = models.TextField(max_length=1000, blank=True, null=True)
    # techniques = models.TextField(max_length=1000, blank=True, null=True)
    certification = models.TextField(max_length=1000, blank=True, null=True)

    class Meta():
        verbose_name_plural = "General info"

    def __str__(self) -> str:
        profile_name = self.first_name + ' ' + self.last_name
        return profile_name


class Jobs(models.Model):
    company_name = models.CharField(max_length=50)
    job_location = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(null=True)
    in_job_experience = models.TextField(max_length=500, null=True)
    # general_info = models.ForeignKey(
    # General_info,
    # related_name="jobs",
    # on_delete=models.DO_NOTHING
    # )

    class Meta():
        verbose_name_plural = "Jobs"

    def __str__(self) -> str:
        return self.company_name


class Experience(models.Model):
    job_experience = models.TextField(max_length=800, null=True)
    company_name = models.ForeignKey(
        Jobs,
        null=True,
        on_delete=models.DO_NOTHING
    )

    class Meta():
        verbose_name_plural = "Experience"

    def __str__(self) -> str:
        return self.job_experience


class Project(models.Model):
    project_choices = [
        ('live', 'live'),
        ('informational', 'informational')]
    image = models.ImageField(upload_to='images/')
    heading = models.CharField(max_length=100)
    subheading = models.CharField(max_length=100, null=True, blank=True)
    summary = models.CharField(max_length=200, null=True, blank=True)
    project_type = models.CharField(choices=project_choices, max_length=250, null=True, blank=True)
    src_link = models.URLField(max_length=1000, null=True, blank=True)
    post = models.TextField(max_length=10000, null=True, blank=True)

    class Meta():
        verbose_name_plural = "Projects"

    def __str__(self) -> str:
        model_name = self.heading + ' - ' + self.subheading
        return model_name
