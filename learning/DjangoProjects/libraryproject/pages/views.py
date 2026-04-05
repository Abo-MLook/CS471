from django.shortcuts import render
# Create your views here.


def index(request):
    x = {'name': 'marwan fahad khalid alayed', 'age': 14}
    # now take the var x into html using dtl
    return render(request, 'pages/index.html', x)


def about(request):
    return render(request, 'pages/about.html')
