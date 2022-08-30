from django.db import models

# Create your models here.
class General_info(models.Model):
    profile_pic = models.ImageField(upload_to='images/')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    contact_num = models.CharField(max_length=30, null=True)
    e_mail = models.EmailField(max_length=50)
    birth_date = models.DateField()
    location = models.CharField(max_length=50)
    summary = models.TextField(max_length=1000, null=True)
    programming = models.TextField(max_length=1000, null=True)
    tools = models.TextField(max_length=1000, null=True)
    techniques = models.TextField(max_length=1000, null=True)
    certification = models.TextField(max_length=1000, null=True)

    class Meta():
        verbose_name_plural = "General info"

    def __str__ (self):
        profile_name = self.first_name + ' ' + self.last_name
        return profile_name

class Jobs(models.Model):
    company_name = models.CharField(max_length=50)
    job_location = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(null=True)
    in_job_experience = models.TextField(max_length=500, null=True)
    # general_info = models.ForeignKey(General_info, related_name="jobs", on_delete=models.DO_NOTHING)

    class Meta():
        verbose_name_plural = "Jobs"

    def __str__(self):
        return self.company_name

class Experience(models.Model):
    job_experience = models.TextField(max_length=800, null=True)
    company_name = models.ForeignKey(Jobs, null=True, on_delete=models.DO_NOTHING)

    class Meta():
        verbose_name_plural = "Experience"

    def __str__(self):
        return self.job_experience

class Project(models.Model):
    project_choices = [
        ('live', 'live'),
        ('informational', 'informational'),]
    image = models.ImageField(upload_to='images/')
    heading = models.CharField(max_length=100)
    subheading = models.CharField(max_length=100, null=True, blank=True)
    summary = models.CharField(max_length=200, null=True, blank=True)
    project_type = models.CharField(choices=project_choices, max_length=250, null=True, blank=True)
    src_link = models.URLField(max_length=1000,null=True, blank=True)
    post = models.TextField(max_length=10000, null=True, blank=True)

    class Meta():
        verbose_name_plural = "Projects"

    def __str__(self):
        model_name = self.heading + ' - ' + self.subheading
        return model_name
