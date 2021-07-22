from django.db import models


class SocialLink(models.Model):
	order = models.IntegerField(default=0)
	icon_class = models.CharField(max_length=50)
	popover_text = models.CharField(max_length=50)
	link = models.CharField(max_length=100, default=None, blank=True, null=True)
	html = models.CharField(max_length=100, default=None, blank=True, null=True)
	def __str__(self):
		return "SocialLink \""+str(self.popover_text)+"\" order:"+str(self.order)+" link:"+str(self.link)+">"

# Generic representation of an entity (school/company/association/.....)
class Entity(models.Model):
	name = models.CharField(max_length=50)
	website = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	short_description = models.CharField(max_length=100, default=None, blank=True, null=True)
	contact_email = models.EmailField(max_length=50, default=None, blank=True, null=True)
	contact_phone = models.CharField(max_length=50, default=None, blank=True, null=True)

# Definition of a school including the potential obtained diploma
class School(models.Model):
	year_start = models.DateField()
	year_end = models.DateField(default=None, blank=True, null=True)
	diploma_type = models.CharField(max_length=50)
	entity = models.ForeignKey(Entity, default=None, blank=True, null=True, on_delete=models.DO_NOTHING)
	diploma_description = models.CharField(max_length=50)
	diploma_description_link = models.CharField(max_length=100)

# Definition of diplomas / awards with a link to an school/entity
class DiplomaAward(models.Model):
	TYPE_CHOICES = (
		('UNDEFINED', '-'),
		('DIPLOMA', 'Diploma'),
		('AWARD', 'Award'),
	)
	year = models.DateField()
	type = models.CharField(max_length=50, choices=TYPE_CHOICES)
	obtained_at_school = models.ForeignKey(School, default=None, blank=True, null=True, on_delete=models.DO_NOTHING)
	delivered_by = models.ForeignKey(Entity, default=None, blank=True, null=True, on_delete=models.DO_NOTHING)
	description = models.CharField(max_length=100)
	see_more_link = models.CharField(max_length=100)

# Professional experiences
class Experience(models.Model):
	TYPE_CHOICES = (
		('UNDEFINED', '-'),
		('Personal', (
			('ASC', 'Association'),
		)),
		('Professional', (
			('CDD', 'FixedTerm contract'),
			('CDI', 'Permanent contract'),
			('INTERNSHIP', 'Internship'),
			('APPRENTICE', 'Apprentice'),
		)),

	)
	date_start = models.DateField()
	date_end = models.DateField(default=None, blank=True, null=True)
	type = models.CharField(max_length=50, choices=TYPE_CHOICES)
	entity = models.ForeignKey(Entity, default=None, blank=True, null=True, on_delete=models.DO_NOTHING)
	description = models.CharField(max_length=100)
	see_more_link = models.CharField(max_length=100, default=None, blank=True, null=True)
