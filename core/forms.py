from django import forms

class UniversityForm(forms.Form):
    SUBJECT_CHOICES = (
        (1, 'Web Dev'),
        (2, 'Programming'),
        (3, 'Data'),
    )

    name = forms.CharField()
    age = forms.IntegerField()
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
    dob = forms.DateField()