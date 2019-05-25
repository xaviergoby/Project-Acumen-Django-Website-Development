from django.urls import path
from users import views as users_views

# urlpatterns = [path('', users_views.home_page_view, name="home_page_view"),
urlpatterns = [path('', users_views.HomePageCBV.as_view()),
               path('profile/', users_views.ProfileInfoCBV.as_view()),
               # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]