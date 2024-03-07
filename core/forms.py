from django import forms
from datetime import datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import User
from django.core.validators import MinLengthValidator

class UniversityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        #self.helper.form_action = reverse_lazy('index')
        #self.helper.form_method = 'POST'
        self.helper.form_id = 'university-form'
        self.helper.attrs = {
            'hx-post':reverse_lazy('index'),
            'hx-target':'#university-form',
            'hx-swap':'outerHTML'
        }
        self.helper.add_input(Submit('submit', 'Submit'))

    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'max':datetime.now().date()}))
    username = forms.CharField(validators=[MinLengthValidator(3)])

    '''
    subject = forms.ChoiceField(choices=User.Subjects.choices)
    name = forms.CharField(widget=forms.TextInput(attrs={
        'hx-get':reverse_lazy('index'),
        'hx-trigger':'keyup'
        }))
    
    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES,
        widget=forms.RadioSelect())
    '''

    class Meta:
        model = User
        fields = ('username', 'password', 'dob', 'subject')
        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
    '''
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) <= 3:
            raise forms.ValidationError('Username is too short')
        return username
    '''

    

    