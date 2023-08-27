from django.urls import path

from accounts.views import loginView, logoutAccount, signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', logoutAccount, name="logout"),
    path('login/', loginView, name='login')
]
