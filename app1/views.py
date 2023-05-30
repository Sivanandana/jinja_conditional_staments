from django.shortcuts import render

# Create your views here.
d={'name':'siva','age':23,'a':20,'b':30}
def condition(request):
    return render(request,'wish.html',context=d)