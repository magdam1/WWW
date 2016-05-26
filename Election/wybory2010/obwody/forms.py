from django import forms

class EditForm(forms.Form):
	osoby = forms.IntegerField(initial = 0, min_value = 0, required=True)
	karty = forms.IntegerField(initial = 0, min_value = 0, required=True)
	licznik = forms.IntegerField(initial = 0, min_value = 0, required=True) 

	def __init__(self, ticket=None, *args, **kwargs):
		super(EditForm, self).__init__(*args, **kwargs)
		self.NAMES = { 'osoby': '', 'karty': '', 'licznik' : '' }

	def add_prefix(self, field_name):
		field_name = self.NAMES.get(field_name, field_name)
		return super(EditForm, self).add_prefix(field_name)