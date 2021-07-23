from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.template.defaultfilters import register
from datetime import date

from .models import SocialLink, GeneralConfig, School, DiplomaAward, Experience, Interest, EXPERIENCE_TYPE_CHOICES



def index(request):
	template = loader.get_template('index.html')
	context = {
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

		'const': {
			'today': date.today()
		}
	}
	print()
	return HttpResponse(template.render(context, request))
# Create your views here.
