from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Student, Admin, Supervisor


#  --- STUDENT CREATION FORM ---

class signupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['first_name'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['card_number'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['ssn'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['year_of_study'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['phone_number'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['birth_date'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['birth_place'].widget.attrs.update({
            'class': 'signup-input'
        })

    username = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    card_number = forms.CharField(max_length=12)
    ssn = forms.CharField(max_length=12)
    year_of_study = forms.CharField(max_length=10)
    phone_number = forms.CharField(max_length=20, required=False)
    birth_date = forms.DateField()
    birth_place = forms.CharField(max_length=255, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                  'card_number', 'ssn', 'year_of_study', 'phone_number', 'birth_date', 'birth_place']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            student = Student(user=user,
                              cardNumber=self.cleaned_data['card_number'],
                              ssn=self.cleaned_data['ssn'],
                              yearOfStudy=self.cleaned_data['year_of_study'],
                              phoneNumber=self.cleaned_data['phone_number'],
                              birthDate=self.cleaned_data['birth_date'],
                              birthPlace=self.cleaned_data['birth_place'])
            student.save()
        return user


#  --- ADMIN CREATION FORM ---


class AdminCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['first_name'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['fax'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['phoneNumber'].widget.attrs.update({
            'class': 'signup-input'
        })

        self.fields['dep'].widget.attrs.update({
            'class': 'signup-input'
        })

    username = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    phoneNumber = forms.CharField(max_length=20)
    fax = forms.CharField(max_length=12, required=False)
    dep = forms.ModelChoiceField(queryset=Department.objects.all())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password1', 'password2', 'phoneNumber', 'fax', 'dep']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            admin = Admin.objects.create(
                user=user,
                phoneNumber=self.cleaned_data['phoneNumber'],
                fax=self.cleaned_data['fax'],
                dep=self.cleaned_data['dep'],
            )
        return admin

#  --- SUPERVISOR CREATION FORM ---

class SupervisorSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20)
    fax = forms.CharField(max_length=12, required=False)
    company = forms.ModelChoiceField(queryset=Company.objects.all())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        supervisor = Supervisor(
            user=user,
            phone_number=self.cleaned_data['phone_number'],
            fax=self.cleaned_data['fax'],
            company=self.cleaned_data['company']
        )

        if commit:
            supervisor.save()

        return supervisor


class createInternshipAppForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['studentName'].widget.attrs.update({
            'class': 'create-app-input',
        })

        self.fields['cardNumber'].widget.attrs.update({
            'class': 'create-app-input'
        })

        self.fields['studentFac'].widget.attrs.update({
            'class': 'create-app-input'
        })

        self.fields['studentDep'].widget.attrs.update({
            'class': 'create-app-input'
        })

        self.fields['ssn'].widget.attrs.update({
            'class': 'create-app-input'
        })

        self.fields['diploma'].widget.attrs.update({
            'class': 'create-app-input'
        })

        self.fields['studentNumber'].widget.attrs.update({
            'class': 'create-app-input'
        })

        self.fields['theme'].widget.attrs.update({
            'class': 'create-app-input'
        })

        self.fields['offeredBy'].widget.attrs.update({
            'class': 'create-app-input'
        })

        self.fields['startingDate'].widget.attrs.update({
            'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
            'class': 'create-app-input'
        })

        self.fields['endingDate'].widget.attrs.update({
            'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
            'class': 'create-app-input'
        })

        self.fields['duration'].widget.attrs.update({
            'class': 'create-app-input'
        })

        self.fields['responsible'].widget.attrs.update({
            'class': 'create-app-input'
        })

        self.fields['responsibleEmail'].widget.attrs.update({
            'class': 'create-app-input'
        })

        self.fields['responsibleNumber'].widget.attrs.update({
            'class': 'create-app-input'
        })

        self.fields['supervisor'].widget.attrs.update({
            'class': 'create-app-input'
        })

        self.fields['supervisorEmail'].widget.attrs.update({
            'class': 'create-app-input'
        })

        self.fields['supervisorNumber'].widget.attrs.update({
            'class': 'create-app-input'
        })

        self.fields['applicant'].widget.attrs.update({
            'class': 'create-app-input'
        })

    class Meta:
        model = InternshipApplication
        fields = ['applicant', 'studentName', 'cardNumber',
                  'studentFac', 'studentDep', 'ssn', 'diploma', 'studentNumber', 'theme', 'offeredBy', 'startingDate', 'endingDate', 'duration', 'responsible', 'responsibleEmail', 'responsibleNumber', 'supervisor', 'supervisorEmail', 'supervisorNumber']
