from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.encoding import force_text,force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .tokens import acount_confirm_token
from .forms import UserRegisterForm


def activate_email(request, uidb64, token):
	try:
		uid=force_text(urlsafe_base64_decode(uidb64))
		user=User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user=None
	if user!=None and acount_confirm_token.check_token(user,token):
		user.active=True
		user.confirmed_email=True
		user.save()
		login(request,user)
		messages.success(request,f'{user.name}, your account is now activated successfully, you can now shorten your links')
		return redirect('signup')
	else:
		return render(request, "Url/activation_error.html")


def signup(request):
	form = UserRegisterForm()
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			site=get_current_site(request)
			uid=urlsafe_base64_encode(force_bytes(user.pk))
			token=acount_confirm_token.make_token(user)
			subject=f"{user.email} Xcrome account"
			message=render_to_string("User/activation_email.html",{
				"user": user,
				"uid": uid,
				"token": token,
				"domail": site.domain
			})
			sent=user.email_user(subject,message)
			messages.success(request,f'Account has been created {user.email} successfully, click on the activation link sent to your email to activate your account')
			return redirect("register")
		else:
			print('False data')
	context={
		'user': form
	}
	return render(request, 'User/signup.html', context)