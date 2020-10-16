from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
# from .utils import create_user_key, crypt, get_key


class UserManager(BaseUserManager):
    def create_user(self, email, phoneno=None, password=None, is_active=True, is_staff=False,
                    is_admin=False):
        if not email:
            raise ValueError("User must provide an email")
        if not phoneno:
            raise ValueError("User must provide a phoneno")
        if not password:
            raise ValueError("User must provide a password")

        user = self.model(email=self.normalize_email(email), phoneno=phoneno)
        user.set_password(password)
        user.active = is_active
        user.admin = is_admin
        user.staff = is_staff
        user.save(using=self._db)
        return user

    def create_staff(self, email, phoneno=None, password=None):
        user = self.create_user(email=email, phoneno=phoneno, password=password, is_staff=True)
        return user

    def create_superuser(self, email, phoneno=None, password=None):
        user = self.create_user(email=email, phoneno=phoneno, password=password, is_staff=True,
                                is_admin=True)
        return user

    def get_staffs(self):
        return self.filter(staff=True)

    def get_admins(self):
        return self.filter(admin=True)


class User(AbstractBaseUser):

    def get_levels():
    	return [
	    		('1', 'Beginner'),
	    		('2', 'Intermediate'),
	    		('3', 'Professional'),
    		]

    email = models.EmailField(max_length=255, unique=True)
    phoneno = models.CharField(max_length=15, unique=True, help_text='add country codes like +234')
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    level = models.CharField(max_length=1, choices=get_levels())
    confirmed_email = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["phoneno"]
    USERNAME_FIELD = "email"

    objects = UserManager()

    @property
    def phone(self):
        return self.phoneno

    # @property
    # def username(self):
    #     return self.profile.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f'User {self.email}'

    def get_absolute_url(self):
        return reverse('authentication', args=['login'])

    def email_user(self, subject, message, fail=True):
        return send_mail(subject, message, "nextbrain@mail.io", [self.email], fail)

    

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    		

class Profile(models.Model):
    username = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='profiles', default='profiles/profile.png')
    id_photo = models.ImageField(upload_to='user_ids', default='user_ids/id.png')
    userx = models.OneToOneField(User, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(editable=False, blank=True, null=True)
    address = models.TextField(blank=True)
    geolocation = models.CharField(max_length=255, editable=False, blank=True)
    country = models.CharField(max_length=255,  blank=True)
    state = models.CharField(max_length=255,  blank=True)
    city = models.CharField(max_length=255,  blank=True)

    def __str__(self):
        return f'Profile {self.username}'