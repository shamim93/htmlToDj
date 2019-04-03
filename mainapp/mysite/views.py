from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):

    return render(request, 'mysite/base.html')

def blog(request):

    return render(request, 'mysite/blog.html')
