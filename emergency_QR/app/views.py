from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is Home page")
    return render(request,'home.html')
