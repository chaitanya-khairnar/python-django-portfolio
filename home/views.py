from django.shortcuts import render, get_object_or_404
from .models import General_info, Project, Jobs, Experience, Education
from django.contrib import messages
from django.core.mail import send_mail


def BASE(request):
    return render(request, 'base.html')


def home(request):
    projects = Project.objects
    general_info = General_info.objects.all()
    experience = Experience.objects.all()
    jobs = Jobs.objects.all().order_by('-from_date')
    education = Education.objects.all()
    # exp = Experience.objects.all()
    inpage_links = {
        "home": "home",
        "project": "project",
        "resume": "resume",
        "contact": "contact",
    }
    page_id = 'home'

    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        subject = request.POST['subject']
        message = request.POST['message']
        formatted_message = 'Name: '+name+' \n Subject: '+subject+'\n Mail: '+mail+' \nMessage:\n ' + message
        send_mail(
            name + '  ' + subject,
            formatted_message,
            mail,
            ['info@chaitanyakhairnar.io'],
        )
        messages.success(request, 'Thanks for your email will respond shortly!')

    return render(request, 'home/home.html', {
            'projects': projects,
            'experience': experience,
            'general_info': general_info,
            'jobs': jobs,
            'education': education,
            'inpage_links': inpage_links,
            'page_id': page_id,
        }
    )


def detail(request, project_id):
    project_details = get_object_or_404(Project, pk=project_id)

    outpage_links = {
        "home": "home",
        "project": "project",
        "resume": "resume",
        "contact": "contact",
    }

    return render(request, 'home/details.html', {
        'project': project_details,
        'outpage_links': outpage_links,
    })
