
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import Regist, Conf, Entrance
from random import randint
import smtplib
from email.message import EmailMessage
from decouple import config

class EmailService:
    @staticmethod
    def send_verification_code(email, code):
        message = EmailMessage()
        message['Subject'] = 'Код для авторизации'
        message['From'] = 'volf.lukonin@bk.ru'
        message['To'] = email
        message.set_content(f'Ваш код для авторизации - {code}\nВведите его на сайте')

        try:
            with smtplib.SMTP_SSL('smtp.mail.ru', 465) as server:
                server.login('volf.lukonin@bk.ru', config('PASSWORD_EMAIL'))
                server.send_message(message)
            return True
        except Exception as e:
            print(f"Ошибка отправки email: {e}")
            return False

class Registration(View):
    def get(self, request):
        form = Regist()
        return render(request, 'entrance/reg.html', {'form': form})

    def post(self, request):
        form = Regist(request.POST)
        if form.is_valid():
            request.session['form_reg'] = request.POST
            kval_code = randint(1000, 9999)
            request.session['code'] = str(kval_code)

            if not EmailService.send_verification_code(request.POST['email'], kval_code):
                return render(request, 'entrance/reg.html', {'form': form, 'error_email': True})

            return redirect('mail_confirmation')  # Используйте именованные URL

        return render(request, 'entrance/reg.html', {'form': form})

class Confirmation(View):
    def get(self, request):
        form = Conf()
        email = request.session['form_reg']['email']
        return render(request, 'entrance/mail_confirmation.html', {'form': form, 'email': email})

    def post(self, request):
        form = Conf(request.POST)
        if form.is_valid() and request.POST['code'] == request.session['code']:
            user_form = Regist(request.session['form_reg'])
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('glavnaya')  # Используйте именованные URL

        return render(request, 'entrance/mail_confirmation.html', {
            'form': Conf(),
            'email': request.session['form_reg']['email'],
            'wrong_code': True
        })

class Glavnaya(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('index')  # Используйте именованные URL
        return render(request, 'entrance/glavnaya_str.html', {
            'last_name': request.user.last_name,
            'first_name': request.user.first_name
        })

    def post(self, request):
        logout(request)
        return redirect('index')  # Используйте именованные URL

class Index(View):
    def get(self, request):
        form = Entrance()
        return render(request, 'entrance/index.html', {'form': form})

    def post(self, request):
        form = Entrance(request.POST)
        user = authenticate(
            request,
            username=request.POST.get('email'),
            password=request.POST.get('password')
        )

        if user:
            login(request, user)
            return redirect('glavnaya')  # Используйте именованные URL

        return render(request, 'entrance/index.html', {'form': form, 'error': True})