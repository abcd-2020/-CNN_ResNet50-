from django.urls import path
from . import views

app_name = 'search'#각각의 앱이 관리하는 독립된 이름 공간, html에서 'mysite:index_u' 별칭이랑 같이 사용

#여기는 매핑하는 곳 그리고 별칭을 써야 하드코딩이 안됨
urlpatterns = [
    path('', views.search, name='search'),
    #index.html에 form검색창 넣고  view에 함수넣고 search_list에 결과 불러오기..아닌가...

    path('<int:prod_id>/', views.kw_search, name='kw_search'),  # 모델 데이터 중 id값이 #인 데이터를 조회,
    # 매핑 규칙에 의해 /pybo/<int:prod_id>/가 적용되어 prod_id에 #라는 값이 저장되고 views.kw_search 함수가 실행
    # int:는 prod_id에 숫자가 매핑되었음을 의미
]