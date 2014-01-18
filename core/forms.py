from django.contrib.auth.models import User
from core.models import Coordinador

__author__ = 'minrock'
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','first_name', 'last_name', 'email')


class CoordinadorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # magic
        self.user = kwargs['instance'].user
        user_kwargs = kwargs.copy()
        user_kwargs['instance'] = self.user
        self.uf = UserForm(*args, **user_kwargs)
        # magic end

        super(CoordinadorForm, self).__init__(*args, **kwargs)

        self.fields.update(self.uf.fields)
        self.initial.update(self.uf.initial)

        # define fields order if needed
        self.fields.keyOrder = (
            'username',
            'password',

            'last_name',
            'first_name',

            'codigo',

        )

    def save(self, *args, **kwargs):
        # save both forms
        self.uf.save(*args, **kwargs)
        return super(CoordinadorForm, self).save(*args, **kwargs)

    class Meta:
        model = Coordinador