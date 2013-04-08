from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from iReceptes.models import Recepta, Categoria, Aliment, MetodePreparacio, Recepta, Pas, Ingredient

def mainpage(request):
  template = get_template('mainpageB.html')
  variables = Context({
      'titlehead': 'Receptes de laguela',
      'pagetitle': 'Welcome to the Receptes  app',
      'user': request.user
    })
  output = template.render(variables)
  return HttpResponse(output)

def receptes_list(request):
  template = get_template('receptesB.html')
  variables = Context({
      'titlehead': 'Llista de totes les Receptes',
      'pagetitle': 'Receptes  app',
      'Receptas' : Recepta.objects.all      
    })
  output = template.render(variables)
  return HttpResponse(output)

def recepta_desc(request):
  template = get_template('recepta.html')
  variables = Context({
      'titlehead': 'Descripcio de la Recepta: ',
      'pagetitle': 'Receptes  app',
      'Recepta' : Recepta.objects.all      
    })
  output = template.render(variables)
  return HttpResponse(output)

def ingredients_list(request):
  template = get_template('ingredientsB.html')
  variables = Context({
      'titlehead': 'Llista de tots els Ingredients',
      'pagetitle': 'Receptes  app',
      'Ingredients' : Ingredient.objects.all      
    })
  output = template.render(variables)
  return HttpResponse(output)

def recepta_detail(request, recepta_name):
  try:
    recepta = Recepta.objects.get(nom=recepta_name)
    #passos = Pas.objects.get(recepta.nom=recepta_name)
    #ingredients = Ingredient.objects.get(recepta.nom=recepta_name)
    param = {
        'titlehead' : "Detalls recepta",
			  'nom_recepta' : recepta.nom ,
        'descripcio_recepta' : recepta.description,
        'Passos' : passos ,
			  'Ingredients' : ingredients }
  except Recepta.DoesNotExist:
    raise Http404
  return render_to_response('receptaB.html',param,context_instance=RequestContext(request))

def aliments_list(request):
  template = get_template('alimentsB.html')
  variables = Context({
      'titlehead': 'Llista de tots els Aliments',
      'pagetitle': 'Receptes  app',
      'Aliments' : Aliment.objects.all      
    })
  output = template.render(variables)
  return HttpResponse(output)


