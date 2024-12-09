from cProfile import label
from termios import VINTR

from django import forms
from .models import Reg


class Regist(forms.ModelForm):
    class Meta:
        model=Reg
        fields=['last_name','first_name','patronymic','email','password']
        labels={'last_name':'Фамилия: ','name':'Имя: ', 'patronymic': 'Отчество: ','date_of_birth':'Дата рождения: ','email':'Почта: '}
        error_messages = {'last_name': {'max_length':'Слишком длинное имя','min_length':'Слишком короткое имя'},
                          'first_name': {'max_length':'Слишком длинная фамилия','min_length':'Слишком короткая фамилия'},
                          'patronymic': {'max_length':'Слишком длинное отчество','min_length':'Слишком короткое отчество'},\
                          'email':{'unique':'Пользователь с такой почтой уже существует'},
                          'password':{'min_length':'Слишком короткий пароль (минимум 10 символов)'}}


class Conf(forms.Form):
    code=forms.IntegerField()

class Entrance(forms.Form):
    email=forms.EmailField(max_length=250, label='Почта:')
    password=forms.CharField(max_length=250, label='Пароль:')
