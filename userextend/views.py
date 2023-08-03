import datetime
from random import randint

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from BrakelessBikeStore.settings import EMAIL_HOST_USER
from userextend.forms import UserForm
# from userextend.models import History


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)  # salvam datele in tabela auth_user
            new_user.first_name = new_user.first_name.title()
            # atribui valoarea new_user.first_name.title() campului first_name al obictului new_user
            new_user.last_name = new_user.last_name.title()

            # new_user.username = f'{new_user.first_name[0].lower()}{new_user.last_name.lower().replace(" ", "")}_{randint(100000, 999999)}'
            # new_user.username = new_user.username.title()
# Comenteaza linita din form linia cu username din forms
            new_user.save()

            # Trimiterea de mail FARA template
            # subject = 'Confirmare cont nou!'
            # message = f'Salut, {new_user.first_name} {new_user.last_name}. Numele tau de utilzator este: {new_user.username}'
            # send_mail(subject, message, EMAIL_HOST_USER, [new_user.email])

            # Add history
            # history_text = f'Userul a fost adaugat la data de {datetime.datetime.now()}. Firstname {new_user.first_name},' \
            #                 f'Last name: {new_user.last_name}, Email: {new_user.email}, Username:{new_user.username}.'

            # History.objects.create(text=history_text, created_at=datetime.datetime.now())

            # # Trimiterea de mail CU TEMPLATEA
            # details_user = {
            #     'fullname': f'{new_user.first_name} {new_user.last_name}',
            #     'username': new_user.username,
            # }
            # subject = 'Confirmare cont nou in aplicatie'
            # message = get_template('mail.html').render(details_user)
            #
            # mail = EmailMessage(subject, message, EMAIL_HOST_USER, [new_user.email])
            # mail.content_subtype = 'html'
            # mail.send()

        return super().form_valid(form)

# argumentul commit=False il folosm pentru a NU salva datele imediat in tabela
# argumentul commit=True il folosm pentru a  salva datele imediat in tabela
