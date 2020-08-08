import json
from django.http import JsonResponse

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.views.generic import View
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator

from .models import User

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
	def post(self, request):
		data = json.loads(request.body)

		user = authenticate(
			username=data['email'],
			password=data['password']
		)

		if user is not None:
			try:
				login(request, user)

				response = user.dict(["id", "username", "first_name", "date_joined"])

				return JsonResponse(response)
			except Exception as e:
				print("---------------- Erro --------------")
				print(e)
				print("------------------------------------")
		else:
			return JsonResponse({"deu": "errado"})

class LogoutView(View):
	def get(self, request):
		logout(request)
		return JsonResponse({"logout": "certo"})

@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):

	def post(self, request):
		try:
			data = json.loads(request.body)

			user = User.objects.filter(username=data['email'])

			if not user:
				user = User.objects.create_user(
					username = data['email'],
					email = data['email'],
					password = data['password'],
					first_name = data['name'],
				)

				login(request, user)

				return JsonResponse({'deu': 'certo'})
			else:
				return JsonResponse({'ja': 'possui email'})

		except Exception as e:
			print("---------------- Erro --------------")
			print(e)
			print("------------------------------------")
			return JsonResponse({'deu': 'errado'})