from django.forms.models import model_to_dict
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

	def dict(self, fields):
		return model_to_dict(self, fields=fields)
