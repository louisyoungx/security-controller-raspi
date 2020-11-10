from django.urls import path

from Applications.ControllerGate.views import Token, OpenGate

app_name = 'controller_gate'

urlpatterns = [
    path('Token/', Token.as_view(), name='token'),
    path('open/', OpenGate.as_view(), name='open_gate'),
]