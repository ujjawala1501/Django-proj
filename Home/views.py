from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    #context is a set of variable which gets sent from here to index.html
    context ={
        "variable1" : "this is sent from views.py ",
        "variable2" : "this is sent for variable2"
    }
    return render(request,'index.html',context)
    #return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    return HttpResponse("this is contact page")
