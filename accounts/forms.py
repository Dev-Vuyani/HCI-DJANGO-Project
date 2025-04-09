from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class StudentRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    student_id = forms.CharField(max_length=20, required=True)

    class Meta:
        model = Student
        fields = ('username', 'full_name', 'email', 'student_id', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email