from django import forms
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.hashers import check_password
from .models import User, Profile
from django.contrib.auth.password_validation import MinimumLengthValidator
# 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',

# class LoginForm(forms.Form):
# 	password=forms.CharField(widget=forms.PasswordInput())
# 	email=forms.CharField(widget=forms.EmailInput())
# 	def clean(self):
# 		data=super(LoginForm, self).clean()
# 		email = data.get('email')
# 		password = data.get('password')
# 		try:
# 			user = User.objects.get(email=email)
# 			if not check_password(password, user.password):
# 				self.add_error('password', forms.ValidationError('Your password is not correct'))
# 		except User.DoesNotExist as e:
# 			pass
# 		return data
# 	def clean_email(self):
# 		email=self.cleaned_data.get("email")
# 		validate_email(email)
# 		try:
# 			user = User.objects.get(email=email)
# 		except User.DoesNotExist as e:
# 			raise forms.ValidationError("Email user matched no account")
# 		return email

# class ChangeForm(forms.Form):
# 	email=forms.CharField(widget=forms.EmailInput())

# 	def clean_email(self):
# 		email=self.cleaned_data.get("email")
# 		validate_email(email)
# 		try:
# 			user = User.objects.get(email=email)
# 		except User.DoesNotExist as e:
# 			raise forms.ValidationError("Email user matched no account")
# 		return email

class ChangePassword(forms.ModelForm):
	password_old=forms.CharField(label="Old password",widget=forms.PasswordInput)
	password1=forms.CharField(label="New password",widget=forms.PasswordInput)
	password2=forms.CharField(label="Confirm password",widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=("password_old","password1","password2",)
	
	def clean_password2(self):
		#Validating if password1 and 2 are correct
		password1=self.cleaned_data.get("password1")
		password2=self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("New passwords do not match")
		return password2

class UserUpdateProfile(forms.ModelForm):
	class Meta:
		model=Profile
		fields=("image",'username','id_photo','address','country','state','city',)

class UserRegisterForm(forms.ModelForm):
	password=forms.CharField(label="Password",widget=forms.PasswordInput, min_length=8, help_text='Must be similar to first password to pass verification')
	password2=forms.CharField(label="Confirm password",widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=("email","phoneno","password","password2",)
	"""Override clean on password2 level to compare similarities of password"""
	def clean_password2(self):
		ps1=self.cleaned_data.get("password")
		ps2=self.cleaned_data.get("password2")
		if (ps1 and ps2) and (ps1 != ps2):
			raise forms.ValidationError("The passwords does not match")
		return ps2
	""" Override the default save method to use set_password method to convert text to hashed """
	def save(self, commit=False):
		user=super(UserRegisterForm, self).save(commit=False)
		user.set_password(self.cleaned_data.get("password"))
		if commit:
			user.save()
		return user

# class UserUpdateForm(forms.ModelForm):
# 	password=ReadOnlyPasswordHashField()
# 	class Meta:
# 		model=User
# 		fields=("email","phoneno","password","active","staff","admin",)
# 		def clean_password(self):
# 			# Regardless of what the user provides, return the initial value.
# 			# This is done here, rather than on the field, because the
# 			# field does not have access to the initial value
# 			return self.initial["password"]