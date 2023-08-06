from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':'supraja','age':'24'}
    return render(request,'jinja.html',context=d)
