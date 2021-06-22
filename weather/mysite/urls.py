from django.urls import path

from . import views

app_name = 'mysite'#각각의 앱이 관리하는 독립된 이름 공간, html에서 'mysite:index_u' 별칭이랑 같이 사용

#여기는 매핑하는 곳 그리고 별칭을 써야 하드코딩이 안됨
urlpatterns = [
    path('', views.index01,name='index_u'),#name별칭,html에 사용

]