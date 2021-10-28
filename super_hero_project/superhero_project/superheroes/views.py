from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

# Create your views here.

def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes' : all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk = hero_id)
    context = {
        'single_hero' : single_hero
    }
    return render(request, 'superheroes/details.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catch_phrase = request.POST.get('catch_phrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catch_phrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

def edit(request, hero_id):
    if request.method == "POST":
        hero = Superhero.objects.get(hero_id)
        hero.name = request.POST.get('name')
        hero.alter_ego = request.POST.get('alter_ego')
        hero.primary_ability = request.POST.get('primary')
        hero.secondary_ability = request.POST.get('secondary')
        hero.catch_phrase = request.POST.get('catch_phrase')
        hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        hero = Superhero.objects.get(hero_id)
        return render(request, 'superheroes/edit.html')