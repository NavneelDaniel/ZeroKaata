from django.urls import path
from . import views

app_name = 'chat1'


urlpatterns = [
	path('tictac/',views.head, name='tictac'),
    path('tictac/<username>/', views.head1)
]