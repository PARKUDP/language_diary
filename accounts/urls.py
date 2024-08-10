from django.urls import path
from .views import CustomLoginView, signup, CustomLogoutView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
