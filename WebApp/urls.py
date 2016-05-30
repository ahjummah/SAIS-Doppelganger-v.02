from django.conf.urls import url
from WebApp.views import *	
from . import views

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^register$', RegistrationView.as_view(), name = 'register'),
	url(r'^login$', LoginView.as_view(), name = 'login'),
	url(r'^profile$', StudentView.as_view(), name = 'viewIndexS'),
	url(r'^edit$', EditView.as_view(), name = 'edit'),
<<<<<<< HEAD
	url(r'^enlist$', StudentEnlist.as_view(), name = 'enlist'),
	url(r'^schedule$', StudentViewSchedule.as_view(), name='schedule'),
	url(r'^account$', StudentViewAccount.as_view(), name='account'),
	url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/WebApp/login'}, name='logout'),
=======
	url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/WebApp/login'}, name='logout'),
	url(r'^enlist$', StudentEnlist.as_view(), name = 'enlist'),
	url(r'^schedule$', StudentViewSchedule.as_view(), name='schedule'),
	url(r'^account$', StudentViewAccount.as_view(), name='account')
>>>>>>> 73b3b8f1c8002df24147f4db00c2c3ab429ce9bd
]