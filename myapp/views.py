from django.shortcuts import render

def index(request):
    context = {'title': 'Головна сторінка'}
    return render(request, 'myapp/index.html', context)

def view1(request):
    context = {'title': 'Сторінка 1'}
    return render(request, 'myapp/view1.html', context)

def view2(request):
    context = {'title': 'Сторінка 2'}
    return render(request, 'myapp/view2.html', context)

def view3(request):
    context = {'title': 'Сторінка 3'}
    return render(request, 'myapp/view3.html', context)

def view4(request):
    context = {'title': 'Сторінка 4'}
    return render(request, 'myapp/view4.html', context)

def view5(request):
    context = {'title': 'Сторінка 5'}
    return render(request, 'myapp/view5.html', context)