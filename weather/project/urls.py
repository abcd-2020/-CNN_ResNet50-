
from django.contrib import admin
from django.urls import path, include
from mysite import views
#이미지업로드
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index01, name='index_u'),#views.index는 views.py 파일의 index 함수,로그인하면 이거 타고감
    path('mysite/', include('mysite.urls')),#mysite/urls.py 파일에 있는 URL 매핑을 참고하여 처리
    path('login/', include('login.urls')),
    path('search/', include('search.urls')),
    path('cart/', include('cart.urls')),


]
# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
