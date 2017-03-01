from django.forms import ModelForm
from .models import Car

class CarForm(ModelForm):
	class Meta:
		model = Car
		fields = ['car_name', 'car_model', 'description', 'image', 'price']
