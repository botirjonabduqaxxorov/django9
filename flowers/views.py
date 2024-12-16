from django.shortcuts import render, get_object_or_404
from .models import Flower, FlowerType

def flower_list(request):
    flowers = Flower.objects.all()
    return render(request, 'flowers/flower_list.html', {'flowers': flowers})

def flower_by_type(request, type_id):
    flower_type = get_object_or_404(FlowerType, id=type_id)
    flowers = flower_type.flowers.all()
    return render(request, 'flowers/flower_by_type.html', {'flower_type': flower_type, 'flowers': flowers})

def flower_detail(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    return render(request, 'flowers/flower_detail.html', {'flower': flower})

def flower_type_list(request):
    flower_types = FlowerType.objects.all()
    return render(request, 'flowers/flower_type_list.html', {'flower_types': flower_types})
