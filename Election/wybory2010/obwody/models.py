from django.db import models

class Wojewodztwo(models.Model):
	nazwa = models.CharField(max_length = 30)

	def __str__(self):
		return self.nazwa

class Powiat_Miasto(models.Model):
	nazwa = models.CharField(max_length = 500)
	wojewodztwo = models.ForeignKey(Wojewodztwo)
	ma_gminy = models.IntegerField(default = 0)

	def __str__(self):
		return self.nazwa

class Gmina_Miasto(models.Model):
	nazwa = models.CharField(max_length = 500)
	powiat = models.ForeignKey(Powiat_Miasto)

	def __str__(self):
		return self.nazwa

class Obwod(models.Model):
	nazwa = models.CharField(max_length = 500)
	miasto = models.ForeignKey(Powiat_Miasto, null = True, blank = True)
	gmina = models.ForeignKey(Gmina_Miasto, null = True, blank = True)
	uprawnionych_do_glosowania = models.PositiveIntegerField(default = 0)
	wydano_kart = models.PositiveIntegerField(default = 0)
	ile_zapisalo = models.PositiveIntegerField(default = 0)

	def __str__(self):
		return self.nazwa
