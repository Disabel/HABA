# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

class Directors(models.Model):
	TIPO = (('chairman', 'Chairman of the Board'), ('president', 'President'), ('vicepresident', 'Vice President'),('secretary', 'Secretary'), ('treasurer', 'Treasurer'), ('director', 'Director'))
	member_type =  models.CharField(max_length=60, choices=TIPO)
	nombre = models.CharField(max_length=45, help_text='Hasta 45 caracteres')
	def __unicode__(self):
		return self.nombre

class MembersApplication(models.Model):
	names = models.CharField(max_length=70)
	last_name = models.CharField(max_length=70)
	state = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	street_address = models.CharField(max_length=100)
	zip_code = models.IntegerField()
	personal_telephone = models.CharField(max_length=100)
	bussines_telephone = models.CharField(max_length=100,blank=True)
	celular = models.CharField(max_length=100,blank=True)
	fax = models.CharField(max_length=100,blank=True)
	email_address = models.EmailField(max_length=50)
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)

class BankingHistory(models.Model):
	financial_institution = models.CharField(max_length=100)
	position_or_title = models.CharField(max_length=100)
	from_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	to_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	member = models.ForeignKey(MembersApplication)

class Education(models.Model):
	GRADUATED = (('yes','Yes'),('no','No'))
	collage_or_university = models.CharField(max_length=100)
	type_of_degree = models.CharField(max_length=100)
	dates_attended = models.CharField(max_length=100)
	did_you_graduate = models.CharField(max_length=5, choices=GRADUATED)
	course_of_study = models.CharField(max_length=100)
	member = models.ForeignKey(MembersApplication)




