from django import template
from django.http import HttpResponse, QueryDict
from django.template import loader
from django.shortcuts import render
from datetime import date

from .models import SocialLink, GeneralConfig, School, DiplomaAward, Experience, Interest, Project, EXPERIENCE_TYPE_CHOICES,PROJECT_TYPE_CHOICES

def build_context():
	return {
		'about': {
			'social_links': SocialLink.objects.order_by('order'),
			'tldr': GeneralConfig.objects.get(key="about_tldr").value,
			'title': GeneralConfig.objects.get(key="about_title").value
		},
		'education': {
			'schools': School.objects.order_by('-year_start'),
			'diplomas': DiplomaAward.objects.filter(type="DIPLOMA").order_by('-year'),
		},
		'awards': DiplomaAward.objects.filter(type="AWARDS").order_by('-year'),
		'experience': {
			'personal': Experience.objects.filter(type__in=[x[0] for x in EXPERIENCE_TYPE_CHOICES[1][1]]).order_by(
				'-date_start'),
			'pro': Experience.objects.filter(type__in=[x[0] for x in EXPERIENCE_TYPE_CHOICES[2][1]]).order_by(
				'-date_start'),
		},
		'interests': {
			'interests': Interest.objects.order_by('order'),
			'tldr': GeneralConfig.objects.get(key="skills_tldr").value,
		},
		'projects': {
			'personal': Project.objects.filter(type__in=[PROJECT_TYPE_CHOICES[1][0]]),
			'school': Project.objects.filter(type__in=[PROJECT_TYPE_CHOICES[2][0]]),
			'tldr': GeneralConfig.objects.get(key="projects_tldr").value,
		},

		'const': {
			'today': date.today(),
			'birthday': date.fromisoformat(GeneralConfig.objects.get(key="about_brithday").value)
		}
	}

def index(request):
	template = loader.get_template('en/index.html')
	return HttpResponse(template.render(build_context(), request))

def index_fr(request):
	template = loader.get_template('fr/index.html')
	return HttpResponse(template.render(build_context(), request))

# Create your views here.
