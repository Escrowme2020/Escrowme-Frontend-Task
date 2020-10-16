from .models import Profile, User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance,created,**kwargs ):
	if created:
		x=Profile.objects.create(user=instance)
		print(x)
		
@receiver(post_save, sender=User)
def save_profile(sender, instance,**kwargs ):
	print('saved')
	instance.profile.save()


# def post_save_user(sender, instance, *args, **kwargs):
#     try:
#         instance.profile
#     if not instance.profile:
#         print(instance)
#         instance.profile = Profile(user=instance)
#         instance.save()

# post_save.connect(post_save_user, User)