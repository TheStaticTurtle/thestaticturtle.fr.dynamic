from django.db import models

EXPERIENCE_TYPE_CHOICES = (
	('Personal', (
		('ASC', 'Association'),
	)),
	('Professional', (
		('CDD', 'Fixed term contract'),
		('CDI', 'Permanent contract'),
		('INTERNSHIP', 'Internship'),
		('APPRENTICE', 'Apprenticeship'),
	)),
)
EXPERIENCE_FRENCH_TYPE_CHOICES = (
	('Personal', (
		('ASC', 'Association'),
	)),
	('Professional', (
		('CDD', 'CDD'),
		('CDI', 'CDI'),
		('INTERNSHIP', 'Stage'),
		('APPRENTICE', 'Apprentisage'),
	)),
)

DIPLOMA_TYPE_CHOICES = (
	('DIPLOMA', 'Diploma'),
	('AWARD', 'Award'),
)
DIPLOMA_FRENCH_TYPE_CHOICES = (
	('DIPLOMA', 'Diplome'),
	('AWARD', 'Prix'),
)

PROJECT_TYPE_CHOICES = (
	('PERSONAL', 'Personal'),
	('SCHOOL', 'School'),
)
PROJECT_FRENCH_TYPE_CHOICES = (
	('PERSONAL', 'Personel'),
	('SCHOOL', 'Scolaire'),
)

class GeneralConfig(models.Model):
	key = models.CharField(max_length=50, unique=True)
	value = models.CharField(max_length=10000)
	def __str__(self):
		return str(self.key)

class SocialLink(models.Model):
	order = models.IntegerField(default=0)
	icon_class = models.CharField(max_length=50)
	tooltip = models.CharField(max_length=50)
	link = models.CharField(max_length=100, default=None, blank=True, null=True)
	html = models.CharField(max_length=1000, default=None, blank=True, null=True)
	def __str__(self):
		return "SocialLink \""+str(self.tooltip)+"\" order:"+str(self.order)+" link:"+str(self.link)+""

# Generic representation of an entity (school/company/association/.....)
class Entity(models.Model):
	name = models.CharField(max_length=50)
	website = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	contact_email = models.EmailField(max_length=50, default=None, blank=True, null=True)
	contact_phone = models.CharField(max_length=50, default=None, blank=True, null=True)
	address = models.CharField(max_length=100, default=None, blank=True, null=True)

	french_description = models.CharField(max_length=1000, default=None, blank=True, null=True)
	def __str__(self):
		return str(self.name)

# Definition of a school including the potential obtained diploma
class School(models.Model):
	year_start = models.DateField()
	year_end = models.DateField(default=None, blank=True, null=True)
	diploma_type = models.CharField(max_length=50)
	entity = models.ForeignKey(Entity, default=None, blank=True, null=True, on_delete=models.DO_NOTHING)
	diploma_description = models.CharField(max_length=100)
	diploma_description_link = models.CharField(max_length=100)

	french_diploma_type = models.CharField(max_length=50, default=None, blank=True, null=True)
	french_diploma_description = models.CharField(max_length=1000, default=None, blank=True, null=True)
	def __str__(self):
		return str(self.diploma_type) + " at " +str(self.entity.name)

# Definition of diplomas / awards with a link to an school/entity
class DiplomaAward(models.Model):
	year = models.DateField()
	type = models.CharField(max_length=50, choices=DIPLOMA_TYPE_CHOICES)
	obtained_at_school = models.ForeignKey(School, default=None, blank=True, null=True, on_delete=models.DO_NOTHING)
	delivered_by = models.ForeignKey(Entity, default=None, blank=True, null=True, on_delete=models.DO_NOTHING)
	description = models.CharField(max_length=100)
	see_more_link = models.CharField(max_length=100)

	french_type = models.CharField(max_length=50, default=None, blank=True, null=True, choices=DIPLOMA_FRENCH_TYPE_CHOICES)
	french_description = models.CharField(max_length=1000, default=None, blank=True, null=True)
	def __str__(self):
		return str(self.type).upper() + " / " + str(self.description) + " at " +str(self.delivered_by.name)

# Professional experiences
class Experience(models.Model):
	date_start = models.DateField()
	date_end = models.DateField(default=None, blank=True, null=True)
	detailed_date = models.BooleanField(default=True)
	type = models.CharField(max_length=50, choices=EXPERIENCE_TYPE_CHOICES)
	entity = models.ForeignKey(Entity, default=None, blank=True, null=True, on_delete=models.DO_NOTHING)
	description = models.CharField(max_length=100)
	see_more_link = models.CharField(max_length=100, default=None, blank=True, null=True)

	french_type = models.CharField(max_length=50, default=None, blank=True, null=True, choices=EXPERIENCE_FRENCH_TYPE_CHOICES)
	french_description = models.CharField(max_length=1000, default=None, blank=True, null=True)
	def __str__(self):
		return str(self.type).upper() + " / " + str(self.description) + " at " +str(self.entity.name)

# Interests
class Interest(models.Model):
	order = models.IntegerField(default=0)
	name = models.CharField(max_length=100)
	icons = models.CharField(max_length=100, default=None, blank=True, null=True)
	description = models.CharField(max_length=1000)

	french_name = models.CharField(max_length=50, default=None, blank=True, null=True)
	french_description = models.CharField(max_length=1000, default=None, blank=True, null=True)

	def icons_as_list(self):
		return self.icons.split(',')

	def __str__(self):
		return str(self.name)+" order:"+str(self.order)

# Interests
class Project(models.Model):
	name = models.CharField(max_length=100)
	type = models.CharField(max_length=50, choices=PROJECT_TYPE_CHOICES)
	description = models.CharField(max_length=1000)
	image_url = models.CharField(max_length=200)
	github_url = models.CharField(max_length=200, default=None, blank=True, null=True)
	blog_url = models.CharField(max_length=200, default=None, blank=True, null=True)
	docs_url = models.CharField(max_length=200, default=None, blank=True, null=True)
	download_url = models.CharField(max_length=200, default=None, blank=True, null=True)
	did_at_school = models.ForeignKey(School, default=None, blank=True, null=True, on_delete=models.DO_NOTHING)

	french_description = models.CharField(max_length=1000, default=None, blank=True, null=True)
	# icons = models.CharField(max_length=100, default=None, blank=True, null=True)
	# def icons_as_list(self):
	# 	return self.icons.split(',')

	def __str__(self):
		return str(self.type) + " / " + str(self.name)
