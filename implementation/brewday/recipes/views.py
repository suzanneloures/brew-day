from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Ingredient, Type_Ingredient, Recipe, Recipe_Ingredient, Equipment, Type_Equipment
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

def access(request):
    if request.method == 'POST':
        id_user = request.POST['user'] #pega o valor inserido no campo email
        password =  request.POST['pass']
        auth_user = authenticate(request, username = id_user, password = password)
        if auth_user is None:
            return render(request, "login.html", {"erro": True})
        else:
            login(request,auth_user)
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse('admin:index'))
            else:
                #return render(request, "home.html")
                return HttpResponseRedirect(reverse('home'))

    else:
        if 'message' in request.session:
            message = request.session['message']
            del request.session['message']
        else:
            message = ''
        return render (request, "login.html",{'message': message,})

def register_user(request):
    if request.method  == 'GET':

        return render(request, "register_user.html")
    else:
        name = request.POST['name']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']
        erros = []
        try:
            validate_email(email)
        except:
            erros.append('Email is invalid')
        if(len(name) == 0):
            erros.append("Name can't be blank")
        if(len(lname) == 0):
            erros.append("Last Name can't be blank")
        if(len(password) == 0):
            erros.append("Password can't be blank")

        if(len(erros)==0):
            user = User.objects.create_user(email,email,password)
            user.first_name = name
            user.last_name = lname
            user.save()
            request.session['message'] = 'success'
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, "register_user.html",{'erros': erros,})

def home(request):
	return render(request, "home.html")

def index(request):
	return render(request, "index.html")

def recipes(request):
    malts = Ingredient.objects.filter(type_ingredient_id = 3)
    hops = Ingredient.objects.filter(type_ingredient_id = 1)
    yeasts = Ingredient.objects.filter(type_ingredient_id = 4)
    sugars = Ingredient.objects.filter(type_ingredient_id = 2)
    additives = Ingredient.objects.filter(type_ingredient_id = 5)
    conteudo = {'malts':malts, 'hops': hops, 'yeasts':yeasts, 'sugars': sugars, 'additives': additives}
    if request.method  == 'GET':
	    return render(request, "register_recipes.html", conteudo)
    else:
        name_recipe = request.POST.get('name')
        type_recipe = request.POST.get('type')
        malt = request.POST.get('codmalt')
        description = request.POST.get('description','')
        malt_qtd = request.POST.get('maltquantity',1)
        hop = request.POST.get('codhop')
        hop_qtd = request.POST.get('hopsquantity',1)
        yeast = request.POST.get('codyeast')
        yeast_qtd = request.POST.get('yeastquantity',1)
        sugar = request.POST.get('codsugar')
        sugar_qtd = request.POST.get('sugarquantity',1)
        additive = request.POST.get('codadditive')
        additive_qtd = request.POST.get('additivequantity',1)
        recipe = Recipe()
        recipe.title = name_recipe
        recipe.type_brew = type_recipe
        recipe.description = description
        recipe.save()

        if malt is not None:
            recipe_ingredient_malt = Recipe_Ingredient()
            recipe_ingredient_malt.recipe_id = int(recipe.id)
            recipe_ingredient_malt.ingredient_id = int(malt)
            recipe_ingredient_malt.quantity = int(malt_qtd)
            recipe_ingredient_malt.save()

        if hop is not None:
            recipe_ingredient_hop = Recipe_Ingredient()
            recipe_ingredient_hop.recipe_id = int(recipe.id)
            recipe_ingredient_hop.ingredient_id = int(hop)
            recipe_ingredient_hop.quantity = int(hop_qtd)
            recipe_ingredient_hop.save()

        if yeast is not None:
            recipe_ingredient_yeast = Recipe_Ingredient()
            recipe_ingredient_yeast.recipe_id = int(recipe.id)
            recipe_ingredient_yeast.ingredient_id = int(yeast)
            recipe_ingredient_yeast.quantity = int(yeast_qtd)
            recipe_ingredient_yeast.save()

        if sugar is not None:
            recipe_ingredient_sugar = Recipe_Ingredient()
            recipe_ingredient_sugar.recipe_id = int(recipe.id)
            recipe_ingredient_sugar.ingredient_id = int(sugar)
            recipe_ingredient_sugar.quantity = int(sugar_qtd)
            recipe_ingredient_sugar.save()

        if additive is not None:
            recipe_ingredient_additive = Recipe_Ingredient()
            recipe_ingredient_additive.recipe_id = int(recipe.id)
            recipe_ingredient_additive.ingredient_id = int(additive)
            recipe_ingredient_additive.quantity = int(additive_qtd)
            recipe_ingredient_additive.save()

        conteudo['message']='success'
        return render(request, "register_recipes.html",conteudo)

def view_ingredients(request):
	return render(request, "view_ingredients.html")

def register_ingredient_additives(request):
    if request.method == 'GET':
        return render(request, "register_ingredient_additives.html")
    else:
        additivesname = request.POST['additivesname']
        additivesquantity = request.POST['additivesquantity']
        unity = request.POST.get('additivesgrams',False)
        ingrediente = Ingredient()
        ingrediente.name = additivesname
        ingrediente.quantity = additivesquantity
        if unity:
            ingrediente.unity = 'GR'
        else:
            ingrediente.unity = 'KG'
        ingrediente.type_ingredient = get_object_or_404(Type_Ingredient, pk=5)

        ingrediente.save()
        conteudo = {'message': 'success'}
       # messages.success(request, 'Form submission successful')
        return render(request, "register_ingredient_additives.html", conteudo)

def register_ingredient_hops(request):
    if request.method  == 'GET':
        return render(request, "register_ingredient_hops.html")
    else:
        maltname = request.POST['maltname']
        hopsquantity = request.POST['hopsquantity']
        unity = request.POST.get('hopsgrams',False)
        #maltdescription = request.POST['maltdescription']
        ingrediente = Ingredient()
        ingrediente.name = maltname
        #ingrediente.unity = 0
        ingrediente.quantity = hopsquantity
        if unity:
            ingrediente.unity = 'GR'
        else:
            ingrediente.unity = 'KG'
        ingrediente.type_ingredient = get_object_or_404(Type_Ingredient, pk=1)

        ingrediente.save()

        conteudo = {'message': 'success'}
        return render(request, "register_ingredient_hops.html", conteudo)

def register_ingredient_malt(request):
    if request.method  == 'GET':
        return render(request, "register_ingredient_malt.html")
    else:
        maltname = request.POST['maltname']
        maltquantity = request.POST['maltquantity']
        unity = request.POST.get('maltgrams',False)
        ingrediente = Ingredient()
        ingrediente.name = maltname
        #ingrediente.unity = 0
        ingrediente.quantity = maltquantity
        if unity:
            ingrediente.unity = 'GR'
        else:
            ingrediente.unity = 'KG'
        ingrediente.type_ingredient = get_object_or_404(Type_Ingredient, pk=3)

        ingrediente.save()

        conteudo = {'message': 'success'}
        return render(request, "register_ingredient_malt.html", conteudo)

def register_ingredient_sugar(request):
    if request.method  == 'GET':
        return render(request, "register_ingredient_sugar.html")
    else:
        sugarname = request.POST['sugarname']
        sugarquantity = request.POST['sugarquantity']
        unity = request.POST.get('imeasuregramssugar',False)
        ingrediente = Ingredient()
        ingrediente.name = sugarname
        #ingrediente.unity = 0
        ingrediente.quantity = sugarquantity
        if unity:
            ingrediente.unity = 'GR'
        else:
            ingrediente.unity = 'KG'
        ingrediente.type_ingredient = get_object_or_404(Type_Ingredient, pk=2)

        ingrediente.save()

        conteudo = {'message': 'success'}
        return render(request, "register_ingredient_sugar.html", conteudo)

def register_ingredient_yeasts(request):
    if request.method  == 'GET':
        return render(request, "register_ingredient_yeasts.html")
    else:
        yeastsname = request.POST['yeastsname']
        yeastsquantity = request.POST['yeastsquantity']
        unity = request.POST.get('yeastsgrams',False)
        ingrediente = Ingredient()
        ingrediente.name = yeastsname
        #ingrediente.unity = 0
        ingrediente.quantity = yeastsquantity
        if unity:
            ingrediente.unity = 'GR'
        else:
            ingrediente.unity = 'KG'
        ingrediente.type_ingredient = get_object_or_404(Type_Ingredient, pk=4)

        ingrediente.save()

        conteudo = {'message': 'success'}
        return render(request, "register_ingredient_yeasts.html", conteudo)
def view_equipment(request):
	return render(request, "view_equipment.html")

def register_equipment_fermenter(request):
    if request.method  == 'GET':
        return render(request, "register_equipment_fermenter.html") #MUDAR LINK HTML
    else:
        name = request.POST['fermentername'] #MUDAR NOME QUE ESTA NO HTML
        capacity = request.POST['fermentervolume'] #MUDAR NOME QUE ESTA NO HTML
        medida = request.POST.get('medida',False) #NÃO MUDAR!
        equipment = Equipment()
        equipment.type_equipment = get_object_or_404(Type_Equipment, pk=1) #MUDAR PK PELO ID DO TIPO NO BANCO
        equipment.medida = medida #NÃO MUDAR DAQUI PARA BAIXO
        equipment.capacity = capacity
        equipment.name = name
        #ingrediente.unity = 0
        equipment.save()

        conteudo = {'message': 'success'}
        return render(request, "register_equipment_fermenter.html", conteudo) #MUDAR LINK HTML

def register_equipment_filter(request):
    if request.method  == 'GET':
        return render(request, "register_equipment_filter.html") #MUDAR LINK HTML
    else:
        name = request.POST['filtername'] #MUDAR NOME QUE ESTA NO HTML
        capacity = request.POST['filtervolume'] #MUDAR NOME QUE ESTA NO HTML
        medida = request.POST.get('medida',False) #NÃO MUDAR!
        equipment = Equipment()
        equipment.type_equipment = get_object_or_404(Type_Equipment, pk=2) #MUDAR PK PELO ID DO TIPO NO BANCO
        equipment.medida = medida #NÃO MUDAR DAQUI PARA BAIXO
        equipment.capacity = capacity
        equipment.name = name
        #ingrediente.unity = 0
        equipment.save()

        conteudo = {'message': 'success'}
        return render(request, "register_equipment_filter.html", conteudo) #MUDAR LINK HTML

def register_equipment_grinder(request):
    if request.method  == 'GET':
        return render(request, "register_equipment_grinder.html") #MUDAR LINK HTML
    else:
        name = request.POST['grindername'] #MUDAR NOME QUE ESTA NO HTML
        capacity = request.POST['grindervolume'] #MUDAR NOME QUE ESTA NO HTML
        medida = request.POST.get('medida',False) #NÃO MUDAR!
        equipment = Equipment()
        equipment.type_equipment = get_object_or_404(Type_Equipment, pk=3) #MUDAR PK PELO ID DO TIPO NO BANCO
        equipment.medida = medida #NÃO MUDAR DAQUI PARA BAIXO
        equipment.capacity = capacity
        equipment.name = name
        #ingrediente.unity = 0
        equipment.save()

        conteudo = {'message': 'success'}
        return render(request, "register_equipment_grinder.html", conteudo) #MUDAR LINK HTML

def register_equipment_kettle(request):
    if request.method  == 'GET':
        return render(request, "register_equipment_kettle.html") #MUDAR LINK HTML
    else:
        name = request.POST['kettlename'] #MUDAR NOME QUE ESTA NO HTML
        capacity = request.POST['kettlevolume'] #MUDAR NOME QUE ESTA NO HTML
        medida = request.POST.get('medida',False) #NÃO MUDAR!
        equipment = Equipment()
        equipment.type_equipment = get_object_or_404(Type_Equipment, pk=4) #MUDAR PK PELO ID DO TIPO NO BANCO
        equipment.medida = medida #NÃO MUDAR DAQUI PARA BAIXO
        equipment.capacity = capacity
        equipment.name = name
        #ingrediente.unity = 0
        equipment.save()

        conteudo = {'message': 'success'}
        return render(request, "register_equipment_kettle.html", conteudo) #MUDAR LINK HTML

class view_recipes(ListView):
    model = Recipe
    template_name = 'view_recipes.html'

class IngredientsView(ListView):
    model = Ingredient
    template_name = 'view_ingredients.html'

class EquipmentsView(ListView):
    model = Equipment
    template_name = 'view_equipment.html'

def production(request):
    recipes = Recipe.objects.all
    content = {'recipes':recipes,}
    return render(request, "production.html", content)

def productionHistory(request):
	return render(request, "production_history.html")

class RecipeDelete(DeleteView):
    template_name = 'recipe_confirm_delete.html'
    model = Recipe
    success_url = reverse_lazy('view_recipes')

class IngredientsEdit(SuccessMessageMixin,UpdateView):
    model = Ingredient
    template_name = 'edit_ingredients.html'
    fields = ['name', 'unity', 'quantity', 'type_ingredient']
    success_message = 'Ingrediente editado'
    success_url = reverse_lazy('view_ingredients')

class IngredientDelete(DeleteView):
    template_name = 'ingredient_confirm_delete.html'
    model = Ingredient
    success_url = reverse_lazy('view_ingredients')


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'view_recipe.html'

class EquipmentsEdit(SuccessMessageMixin,UpdateView):
    model = Equipment
    template_name = 'edit_equipments.html'
    fields = ['name', 'medida', 'capacity', 'type_equipment']
    success_message = 'Equipamento Editado'
    success_url = reverse_lazy('view_equipment')

class EquipmentDelete(DeleteView):
    template_name = 'equipment_confirm_delete.html'
    model = Equipment
    success_url = reverse_lazy('view_equipment')
