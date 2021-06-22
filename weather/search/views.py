from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from mysite.models import Prod_m


def search(request):

    # 페이징
    page = request.GET.get('page', '1')  # 페이지
    q = request.GET.get('q', '')#검색
    #post로 넘어온거 담아서
    prod_search_v = Prod_m.objects.all().order_by('?')  # 랜덤으로 담아서

    if q:
        prod_search_v = prod_search_v.filter(Q(name__icontains = q)).distinct()#필터해서 name를 q랑 비교

        # 페이징처리
        paginator = Paginator(prod_search_v, 10)  # 페이지당 5개씩 보여주기
        page_obj = paginator.get_page(page)
        context = {'prod_search_v_h': page_obj, 'page': page, 'q': q}  # page와 kw가 추가
        return render(request, 'search/search.html', context)  # 비교한게 있으면 넘겨줌


    else :
       return render(request, 'search/search.html')


#이거를 아이디에 있는 카테고리 받아와서 재검색하면 좋을 거 같은데..
def kw_search(request, prod_id):# 매개변수 prod_id URL 매핑에 있던 prod_id. search/int/ 페이지가 호출되면 detail 함수의 매개변수 prod_id 2가 전달

    #prod_detail_v = Prod_m.objects.get(id=prod_id),  # 이거는 404안뜨는거
    prod_detail_v = get_object_or_404(Prod_m,id=prod_id)#존재하지 않는 페이지에 접속하면 오류 대신 404 페이지를 출력
    category = prod_detail_v.category
    prod_kw = Prod_m.objects.all().order_by('?')


    if prod_kw:
        prod_kw = prod_kw.filter(Q(category__contains = category)).distinct()

        page = request.GET.get('page', '1')
        paginator = Paginator(prod_kw, 10)  # 페이지당 5개씩 보여주기
        page_obj = paginator.get_page(page)
        context = {'prod_search': page_obj, 'page': page, 'prod_kw': prod_kw,'prod_detail_v':prod_detail_v}  # page와 kw가 추가
        return render(request, 'search/kw_search.html', context)  # 비교한게 있으면 넘겨줌


    else :
        return render(request, 'search/kw_search.html')


