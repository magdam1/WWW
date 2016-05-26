import json
from django.shortcuts import render
from .models import Wojewodztwo, Powiat_Miasto, Gmina_Miasto, Obwod
from .forms import EditForm
from django.forms import ValidationError
from django.http import Http404, HttpResponse
from django.db import transaction

# Wyświetla listę województw.
def first(request):
	woj_list = Wojewodztwo.objects.order_by('nazwa')
	context = { 'query_list' : woj_list }
	return render(request, 'obwody/first.html', context)

# Wyświetla listę powiatów.
def second(request, woj):
	try:
		wojew = Wojewodztwo.objects.get(id = woj)
	except:
		raise Http404("Strona nie istnieje!")

	pow_list = Powiat_Miasto.objects.filter(wojewodztwo = woj).order_by('nazwa')
	context = { 'query_list' : pow_list, 'wojew' : wojew }
	return render(request, 'obwody/second.html', context)

# WYświetla listę gmin, jeśli wybrany uprzednio powiat je posiada, lub w p.p. obwodów.
@transaction.atomic
def third(request, woj, pow):
	try:
		wojew = Wojewodztwo.objects.get(id = woj)
		powi = Powiat_Miasto.objects.get(id = pow)
		flag = Powiat_Miasto.objects.get(id = pow).ma_gminy
	except:
		raise Http404("Strona nie istnieje!")

	if flag:
		gmin_list = Gmina_Miasto.objects.filter(powiat = pow).order_by('nazwa')
		context = { 'query_list' : gmin_list, 'wojew' : wojew, 'powi' : powi }
		return render(request, 'obwody/third.html', context)
	else:
		obwod_list = list(Obwod.objects.select_for_update().filter(miasto = pow, gmina__isnull = True).order_by('nazwa').values_list('id', 'nazwa', 'uprawnionych_do_glosowania', 'wydano_kart', 'ile_zapisalo'))
		context = {	"query_list" : obwod_list, 'wojew' : wojew, 'powi' : powi }
		return render(request, 'obwody/edit_city.html', context)

# Wyświetla listę obwodów należących do uprzednio wybranej gminy.
@transaction.atomic
def fourth(request, woj, pow, gmin):
	try:
		wojew = Wojewodztwo.objects.get(id = woj)
		powi = Powiat_Miasto.objects.get(id = pow)
		gmi = Gmina_Miasto.objects.get(id = gmin)
		obwod_list = list(Obwod.objects.select_for_update().filter(gmina = gmi).order_by('nazwa').values_list('id', 'nazwa', 'uprawnionych_do_glosowania', 'wydano_kart', 'ile_zapisalo'))
	except:
		raise Http404("Strona nie istnieje!")

	context = {	"query_list" : obwod_list, 'wojew' : wojew, 'powi' : powi, 'gmi' : gmi }
	return render(request, 'obwody/edit.html', context)
	
# Funkcja wywoływana podczas kliknięcia na przycisk "Edytuj" oraz "Anuluj"
@transaction.atomic
def edit(request) :
	if request.method != 'POST' :
		raise Http404("Strona nie istnieje!")
	else:
		try:
			id = int(request.POST['obw_id'])
			obw = Obwod.objects.select_for_update().get(id=id)
		except ValueError:
			obw = None

		res = {}
		
		# Zwracamy wartości znajdujące się w bazie.
		res['ile_glosow'] = obw.uprawnionych_do_glosowania
		res['ile_kart'] = obw.wydano_kart
		res['licznik'] = obw.ile_zapisalo

		return HttpResponse(json.dumps(res), content_type="application/json")

# Funkcja pomocnicza służaca do zapisu nowych wartości w bazie.
@transaction.atomic
def save_to_database(values):
	try:
		obw = Obwod.objects.select_for_update().get(id=values['id'])	
	except:
		raise Http404("Strona nie istnieje!")

	licznik_baza = obw.ile_zapisalo
	c = True

	# Wartości w bazie zostały nadpisane.
	if values['licznik'] != licznik_baza :
		c = False
	# W p.p. (jeśli nie próbujemy zapisać do bazy czegoś, co już w niej jest) - zapisujemy nowe dane do bazy.
	elif not (obw.wydano_kart == values['karty'] and obw.uprawnionych_do_glosowania == values['glosy']):
		obw.wydano_kart = values['karty']
		obw.uprawnionych_do_glosowania = values['glosy']
		obw.ile_zapisalo += 1;
		obw.save();

	return c;

# Funkcja wywoływana podczas kliknięca na przycisk "Zapisz"
def accept(request) :
	if request.method != 'POST' :
		raise Http404("Strona nie istnieje!")
	else:
		try:
			values = {}
			values['id'] = int(request.POST['obw_id'])
			values['licznik'] = int(request.POST['obw_licznik'])
			values['karty'] = int(request.POST['karty'])
			values['glosy'] = int(request.POST['glosy'])
		except ValueError:
			obw = None

		c = save_to_database(values)

		obw = Obwod.objects.get(id=values['id'])
		# Zwracamy obecne wartości znajdujące się w bazie.
		res = {}
		res['ile_glosow'] = obw.uprawnionych_do_glosowania
		res['ile_kart'] = obw.wydano_kart
		res['licznik'] = obw.ile_zapisalo
		res['changed'] = c

		return HttpResponse(json.dumps(res), content_type="application/json")

