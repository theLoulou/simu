from django import forms

class run_form(forms.Form):
	bd = forms.DecimalField(max_digits=2, decimal_places=1, label="brand_factor")

	def clean_bd(self):
		 bd = self.cleaned_data['bd']
		 if bd<0.1 or bd>2.9:
		 	raise forms.ValidationError("brand_factor must be in [0.1 , 2.9]")
		 return bd


class filter_form(forms.Form):
	age = forms.IntegerField(label="age of agent at t=0 (0 for all)")
	year = forms.IntegerField(label="year number :")
	breed_C = forms.BooleanField(label="breed_c :", required=False)
	breed_NC = forms.BooleanField(label="breed_nc :", required=False)
	gained = forms.BooleanField(label="gained", required=False)
	lost = forms.BooleanField( label='lost',required=False)
	regained = forms.BooleanField(label='regained',required=False)

	def clean_age(self):
		age = self.cleaned_data['age']
		if age<0:
			raise forms.ValidationError('must be superior or equal to 0')
		return age
	def clean_year(self):
		year = self.cleaned_data['year']
		if year>15 or year<0:
			raise forms.ValidationError("year must be in [0 , 15]")
		return year
