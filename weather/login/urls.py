from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'login_ua'

urlpatterns = [#
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login_u'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_u'),
    path('join/', views.join, name='join_u'),
]

#django.contrib.auth 앱을 사용할 것이므로 login/views.py 파일은 수정할 필요가 없다.
# 여기서는 django.contrib.auth 앱의 LoginView 클래스를 사용