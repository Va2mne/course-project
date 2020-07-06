"""
Definition of views.
"""
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
#from .models import *
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

# Опять же, спасибо django за готовую форму аутентификации.
from django.contrib.auth.forms import AuthenticationForm

# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

#Email
from django.http import HttpResponse
from django.core.mail import send_mail
import django
from django.conf import settings

#Models
from .models import *

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name =  "clown/index.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "clown/index.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    title='Главная страница'
    auth = "True"
    if request.user.is_authenticated():
        auth = "True"
        user = request.user
    else:
        auth = "False"
        user = "null"
    return render(
        request, 
        'clown/index.html',
       locals()
    )

def actors(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request, 
        'clown/actors.html',
        {
            'title':'Актеры',
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    title='Контакты'
    
    name = request.POST.get('Name')
    email = request.POST.get('Email')
    subject = request.POST.get('Subject')
    message = request.POST.get('Message')
    data = """
Hello there!

I wanted to personally write an email in order to welcome you to our platform.\
 We have worked day and night to ensure that you get the best service. I hope \
that you will continue to use our service. We send out a newsletter once a \
week. Make sure that you read it. It is usually very informative.

Cheers!
~ Yasoob
    """

    if name != '':
        send_mail('Welcome!', data, "Yasoob", [email], fail_silently=False)
    return render(
        request,
        'clown/contact.html',
        
    )

def gallery(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'clown/gallery.html',
        {
            'title':'Галлерея',
        }
    )

def blogdetails(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    comments = comment.objects.all()
    title = 'Blog Details'
    if request.POST:
        mes =  request.POST.get('Message')
        comment.save(['alex', mes])
    return render(
        request,
        'clown/blogdetails.html',
        locals()
    )
