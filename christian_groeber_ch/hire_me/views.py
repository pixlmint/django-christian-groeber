from django.shortcuts import render, redirect
from portfolio.models import Element
from .models import Resume, Experience


# Create your views here.


def index(request):
    resume = Resume.objects.get(pk=1)
    exp = resume.experiences.all().order_by('-date_from')
    elements = Element.objects.all().order_by('-date_started')
    experiences = []
    for experience in exp:
        experiences.append(ExperienceObject(experience.title, experience.date_from, 'experience', description=experience.description,
                                            date_until=experience.date_until))
    for element in elements:
        element.generate_url()
        experiences.append(ExperienceObject(element.title, element.date_started, 'element', description=element.description,
                                            date_until=element.date_finished, url=element.url))
    sorted_experiences = sorted(experiences, key=lambda test: test.date_from)
    return render(request, 'hire_me/index.html', {'resume': resume, 'experiences': sorted_experiences})


class ExperienceObject:
    def __init__(self, title, date_from, exp_type, description=None, date_until=None, url=None):
        self.title = title
        self.date_from = date_from
        self.description = description
        self.date_until = date_until
        self.exp_type = exp_type
        self.url = url
