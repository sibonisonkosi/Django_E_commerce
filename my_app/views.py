from django.shortcuts import render

def default(request):
    return render(request, 'my_app/index.html')
