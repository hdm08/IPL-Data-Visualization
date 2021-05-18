from django import forms
from .models import Delivery

class DeliveryData(forms.Form):
	class meta:
		model = Delivery
		fields = '__all__'