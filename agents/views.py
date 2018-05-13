from django.shortcuts import render, get_object_or_404, redirect
import csv, copy
from agents.models import Ag
from .forms import run_form, filter_form 

def home(request):
	Agents = Ag.objects.all()
	title = 'this is the welcome page'
	return render(request, 'agents/accueil.html', locals())


def read(request):
	Agents = csv.reader(open('Simudyne_Backend_Test.csv',"r", newline=''))
	next(Agents)
	instance=[]
	for agent in Agents:
		if agent[0]=="Breed_C":
			instance.append(Ag(Ag_breedC=True, policy_ID=agent[1], age=agent[2], social_grade=agent[3], Payment=agent[4], attribute_brand=agent[5], attribute_price=agent[6], attribute_promotion=agent[7], auto_renew=agent[8], inertia_switch=agent[9]))
			#try:
				#Ag.objects.create(Ag_breedC=True, policy_ID=agent[1], age=agent[2], social_grade=agent[3], Payment=agent[4], attribute_brand=agent[5], attribute_price=agent[6], attribute_promotion=agent[7], auto_renew=agent[8], inertia_switch=agent[9])
			#except:
				#return redirect('errorDB')
		else:
			instance.append(Ag(Ag_breedC=False, policy_ID=agent[1], age=agent[2], social_grade=agent[3], Payment=agent[4], attribute_brand=agent[5], attribute_price=agent[6], attribute_promotion=agent[7], auto_renew=agent[8], inertia_switch=agent[9]))
			#try: 
				#Ag.objects.create(Ag_breedC=False, policy_ID=agent[1], age=agent[2], social_grade=agent[3], Payment=agent[4], attribute_brand=agent[5], attribute_price=agent[6], attribute_promotion=agent[7], auto_renew=agent[8], inertia_switch=agent[9])
			#except:
				#return redirect('errorDB')
	try:
		Ag.objects.bulk_create(instance)
	except:
		return redirect('errorDB')
	title='csv added to the sqlite database'
	return render(request,'agents/accueil.html', locals())

def delete(request):
	Ag.objects.all().delete()
	title='table cleaned'
	return render(request,'agents/accueil.html', locals())

def errorDB(request):
	title='there is a problem with the DB'
	return render(request,'agents/accueil.html', locals())

def see(request):
	form = filter_form(request.POST)
	if form.is_valid():
		try:
			age = form.cleaned_data['age']
			year = form.cleaned_data['year']
			gained = form.cleaned_data['gained']
			breed_C = form.cleaned_data['breed_C']
			breed_NC = form.cleaned_data['breed_NC']
			lost = form.cleaned_data['lost']
			regained = form.cleaned_data['regained']
			if age!=0:
				Agents = Ag.objects.filter(age=age)
			else:
				Agents = Ag.objects.all()
			Agents2 = []	
			for agent in Agents:
				if ((agent.is_regained(year) == True) and (regained==True)) or ((agent.is_gained(year) == True) and (gained==True)) or ((agent.is_lost(year) == True) and (lost==True)) or ((agent.is_true(year) == True) and (breed_C==True)) or ((agent.is_true(year) == False) and (breed_NC==True)):
					temp = copy.copy(agent)
					temp.age = agent.age + year
					temp.Ag_breedC= agent.is_true(year)
					Agents2.append(temp)
		except:
			return redirect('errorDB')
	else:
		Agents2 = Ag.objects.all
	return render(request, 'agents/see.html', locals())

def run(request):
	form = run_form(request.POST)
	if form.is_valid():
		brand_factor = form.cleaned_data['bd']
		Agents = Ag.objects.all()
		title = 'end of run'
		try:
			for agent in Agents:
				agent.run(brand_factor)
			return render(request, 'agents/accueil.html', locals())
		except:
			return redirect('errorDB')
	return render(request,'agents/run.html',locals())
