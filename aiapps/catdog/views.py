from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import PhotoForm
from .models import Photo

def index(request):
    template = loader.get_template('catdog/index.html')
    context = {'form':PhotoForm()}
    return HttpResponse(template.render(context, request))

def predict(request):
    if not request.method == 'POST':
        return
        redirect('catdog.index')

    print('check')
    form = PhotoForm(request.POST, request.FILES)
    if not form.is_valid():
        raise ValueError('Formが不正です')

    photo = Photo(image=form.cleaned_data['image'])
    predict, percentage = photo.predict()

    template = loader.get_template('catdog/predict.html')
    context = {
        'photo_name': photo.image.name,
        'photo_data': photo.image_src(),
        'predicted': predict,
        'percentage': percentage,
    }
    return HttpResponse(template.render(context, request))

def true_result(request):
    return render(request, 'catdog/true_results.html')

def false_result(request):
    return render(request, 'catdog/false_results.html')