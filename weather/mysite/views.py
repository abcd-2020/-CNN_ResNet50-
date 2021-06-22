from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect  # 존재하지 않는 페이지에 접속하면 오류 대신 404 페이지를 출력
from .models import Prod_m


from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

from datetime import datetime, timedelta

def day():
    now = datetime.today()
    after_two_day = now + timedelta(days=1)
    after_three_day = after_two_day + timedelta(days=1)
    after_four_day = after_three_day + timedelta(days=1)
    after_five_day = after_four_day + timedelta(days=1)

    return {'after_two_day' :after_two_day,'after_three_day':after_three_day,
            'after_four_day':after_four_day,'after_five_day':after_five_day}



def result():
    html = requests.get('https://search.naver.com/search.naver?query=날씨')
    soup = bs(html.text,'html.parser')
    data1 = soup.find('div',{'class':'info_data'})#오늘날씨
    data2 = data1.findAll('span')
    data3 = data1.findAll('p', {'class': 'cast_txt'})

    return {
    'today_temp' : data2[0].text, #현재온도
    'min_temp' : data2[5].text,
    'max_temp' : data2[8].text,
    'sensible' : data2[11].text,#체감온도
    #'rainfall' : data2[13].text,
    'cast' : data3[0].text }#시간당 강수량


def result2():
    html = requests.get('https://search.naver.com/search.naver?query=날씨')
    soup = bs(html.text,'html.parser')
    data3 = soup.find('div',{'class':'table_info weekly _weeklyWeather'})#미래날씨
    data4 = data3.findAll('dd')
    data5 = data3.findAll('span', {'class': 'num'})
    return {
    'tomorrow1' : data4[1].text,
    'rain2' : data5[2].text,
    'rain3' : data5[3].text
    }

def result3():
    html = requests.get('https://search.naver.com/search.naver?query=날씨')
    soup = bs(html.text,'html.parser')
    data3 = soup.find('div',{'class':'table_info weekly _weeklyWeather'})#미래날씨
    data4 = data3.findAll('dd')
    data5 = data3.findAll('span', {'class': 'num'})
    return {
    'tomorrow2': data4[2].text,
    'rain4' : data5[4].text,
    'rain5' : data5[5].text}

def result4():
    html = requests.get('https://search.naver.com/search.naver?query=날씨')
    soup = bs(html.text,'html.parser')
    data3 = soup.find('div',{'class':'table_info weekly _weeklyWeather'})#미래날씨
    data4 = data3.findAll('dd')
    data5 = data3.findAll('span', {'class': 'num'})
    return {
    'tomorrow3': data4[3].text,
    'rain6': data5[6].text,
    'rain7': data5[7].text,
    }

def result5():
    html = requests.get('https://search.naver.com/search.naver?query=날씨')
    soup = bs(html.text,'html.parser')
    data3 = soup.find('div',{'class':'table_info weekly _weeklyWeather'})#미래날씨
    data4 = data3.findAll('dd')
    data5 = data3.findAll('span', {'class': 'num'})
    return {
    'tomorrow4': data4[4].text,
    'rain8': data5[8].text,
    'rain9': data5[9].text,
    }


def index01(request):#랜덤으로 제품가져오기
    # prod_list_v = Prod_m.objects.all().order_by("?")[:2]
    prod_list = Prod_m.objects.all().order_by("category")
    prod_list_v = prod_list.order_by("?").distinct()[:10]#?는 랜덤이고, 숫자는 갯수
    prod_list_v2 = prod_list.order_by("?")[:3]
    prod_list_v3 = prod_list.order_by("?")[:3]
    prod_list_v4 = prod_list.order_by("?")[:3]
    prod_list_v5 = prod_list.order_by("?")[:3]

    #카테고리별 함수필요

    context = {'prod_list_v_h' : prod_list_v,
               'prod_list_v' : prod_list_v2,
               'prod_list_v2': prod_list_v3,
               'prod_list_v3': prod_list_v4,
               'prod_list_v4': prod_list_v5,
               'weatherlist':result(),
               'tomorrow1': result2(),
               'tomorrow2': result3(),
               'tomorrow3': result4(),
               'tomorrow4': result5(),
               'daylist':day()

               }

    return render(request,'mysite/index.html',context)

'''
#에러 404로 띄우기
def error(request):
    #return HttpResponseNotFound('<h1>not found</h1>')
    raise Http404("Not Found")
'''