from django import forms
from . import models


class LoginForm(forms.Form):

    """Login Form Definition"""

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)  # password 입력시 사용

    def clean(self):
        # 두 fields 가 서로 상관이 있으므로(코드가 중복되므로) clean method 로 함께 관리함
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
                # cleaned_data 를 return 해야 email, password 둘 다 가진 data 가 return
            else:
                self.add_error("password", forms.ValidationError("Incorrect Password"))
                # add_error("field", error) : 어디서 error 가 일어나는지 명확하게 보여줌
                # clean_email() 이나 clean_password() 사용시에는 필요 없음
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User Not Found"))


class SignUpForm(forms.Form):

    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("Already Using Email")
        except models.User.DoesNotExist:
            return email

    def claen_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password does not match")
        else:
            return password

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = models.User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
