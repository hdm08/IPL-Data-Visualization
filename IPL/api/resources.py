from import_export import resources
from .models import Delivery

class DeliveryResource(resources.ModelResource):
    class Meta:
        model = Delivery