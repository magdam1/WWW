# -*- coding: utf-8 -*-

from django.test import TestCase
from obwody.models import Wojewodztwo, Powiat_Miasto, Gmina_Miasto, Obwod
from .views import save_to_database
from random import randint

class TestingSaving(TestCase):

	def setUp(self):
		maz = Wojewodztwo.objects.create(nazwa='mazowieckie')
		otw = Powiat_Miasto.objects.create(wojewodztwo=maz, nazwa='otwocki')
		gmi = Gmina_Miasto.objects.create(powiat=otw, nazwa="Celestynów, gm.")
		obw = Obwod.objects.create(gmina=gmi, nazwa="Testowy obwod")
		print('Test started.')

	def test_saving(self):
		woj = Wojewodztwo.objects.get(nazwa="mazowieckie")
		pow = Powiat_Miasto.objects.get(wojewodztwo=woj, nazwa="otwocki")
		gmi = Gmina_Miasto.objects.get(powiat=pow, nazwa="Celestynów, gm.")
		obw = Obwod.objects.all()

		values = {}
		values['id'] = obw[0].id
		values['licznik'] = obw[0].ile_zapisalo
		values['karty'] = randint(0, 1000000)
		values['glosy'] = randint(0, 1000000)

		save_to_database(values)

		obw_new = Obwod.objects.get(id=values['id'])
		self.assertEqual(values['karty'], obw_new.wydano_kart)
		self.assertEqual(values['glosy'], obw_new.uprawnionych_do_glosowania)	
		


