from django import forms
from django.contrib.auth.models import User
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text')


class SignUpForm(forms.Form):
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(),
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(),
    )

    def sign_up(self, request):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )

class SignUpForm(forms.Form):
	username = forms.CharField()
	password1 = forms.CharField()
	password2 = forms.CharField()


	def sign_up (self):
		from .models import MyUser

		if self.cleaned_data['password1'] == self.cleaned_data['password2']:
			return MyUser.objects.create(
				username = self.cleaned_data['username'],
				password = self.cleaned_data['password1'],
			)

		else:
			return False

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

	def login (self):
		from .models import MyUser

		user = MyUser.objects.filter(
			username=self.cleaned_data['username'],
			password=self.cleaned_data['password']
		)

		return user
