from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'content' : ['Если у вас остались вопросы, задавайте их по телефоу', '+375 (25) 714 85 68']})