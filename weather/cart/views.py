from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404



from cart.models import CartList
from mysite.models import Prod_m

def cart(request):#카트에 담긴것
    try:
        user = User.objects.get(pk=request.user.pk)
        cart_item = CartList.objects.filter(user = user)

    except cart.DoesNotExist:
        pass

    page = request.GET.get('page', '1')  # 페이지
    paginator = Paginator(cart_item,10)
    page_obj = paginator.get_page(page)
    context = {'cart_item': page_obj, 'page': page}

    return render(request, 'cart/cart.html', context)



def add_cart(request):#카트에 담기

    prod_id = request.GET.get('prod_id')
    user = User.objects.get(pk=request.user.pk)
    product = Prod_m.objects.get(id = prod_id)
    if not CartList.objects.filter(product=product, user=user).exists():#중복금지
        cart = CartList.objects.create(
            user = user,
            product = product
        )
        cart.save()
        return redirect('/cart')
    else:
        return redirect('/cart')


def delete(request):#전체삭제는 유저만, 하나삭제는 둘 다 필요
    prod_id = request.GET.get('prod_id')
    user_id = request.user.id
    cartList = CartList.objects.all()

    if cartList:
        product = cartList.filter(Q(user = user_id) & Q(product = prod_id))
        product.delete()
        return redirect('/cart')
    else:
        return redirect('/cart')

    # prod_id = request.GET.get('prod_id')
    # user = User.objects.get(pk=request.user.pk)
    # product = Prod_m.objects.get(id = prod_id)
    # cart = CartItem.objects.get(product_pk=product.pk, user__id=request.user.pk)






# @login_required
# def cart(request, prod_id):
#     product = Prod_m.objects.get(pk=prod_id)
#
#     try:
#         # 장바구니는 user 를 FK 로 참조하기 때문에 save() 를 하기 위해 user 가 누구인지도 알아야 함
#         cart = CartItem.objects.get(product_pk=product.pk, user__id=request.user.pk)
#         if cart:
#             if cart.product.name == product.name:
#                 cart.save()
#     except CartItem.DoesNotExist:
#         user = User.objects.get(pk=request.user.pk)
#         cart = CartList(
#             user=user,
#             product=product
#         )
#         cart.save()
#     return redirect('cart:cart')
#
#
