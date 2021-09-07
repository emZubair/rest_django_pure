from django.urls import path

from .views import (PizzeriaListAPIView, PizzeriaDetailsAPIView, PizzeriaCreateAPIView, PizzeriaDestroyAPIView,
                    PizzeriaUpdateAPIView)

urlpatterns = [
    path('create', PizzeriaCreateAPIView.as_view(), name='pizza_create'),
    path('', PizzeriaListAPIView.as_view(), name='Pizza listings'),
    path('<pk>', PizzeriaDetailsAPIView.as_view(), name='pizza_details'),
    path('<pk>/delete', PizzeriaDestroyAPIView.as_view(), name='pizza_delete'),
    path('<pk>/update', PizzeriaUpdateAPIView.as_view(), name='pizza_update'),
]