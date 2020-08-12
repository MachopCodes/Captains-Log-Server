from django.urls import path
from .views.trip_views import Trips, TripDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.key_view import Key
from .views.coords_view import Coords
from .views.tide_view import Tide

urlpatterns = [
	# Restful routing
    path('trips/', Trips.as_view(), name='trips'),
    path('trips/<int:pk>/', TripDetail.as_view(), name='trip_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('key/', Key.as_view(), name='key'),
    path('tides/', Tide.as_view(), name='tides'),
    path('coords/<str:key>/', Coords.as_view(), name='coords')
]
