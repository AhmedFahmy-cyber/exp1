from django.shortcuts import render

# Create your views here.
from django.views import View

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
