from django import forms

from .models import Mentor, Team, Department, Project


class DateInput(forms.DateInput):
    input_type = "date"

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

class UpdateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        labels = {"category":"Select Category"}

class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}

class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"
        widgets = {"dateofbirth":DateInput(),"password":forms.PasswordInput(),'fullname': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'})}
