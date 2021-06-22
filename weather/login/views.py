from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from login.join_forms import UserForm


def join(request):
    """
    계정생성
    """
    if request.method == "POST":#POST 요청인 경우 화면에서 입력한 데이터로 새로운 사용자를 생성 get이면 return경로
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')#화면에서 입력한 값을 얻기 위해 사용하는 함수 cleaned_data.get
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # authenticate, login 함수는 django.contrib.auth 패키지에 있는 함수로 사용자 인증과 로그인을 담당
            return redirect('index_u')
    else:
        form = UserForm()
    return render(request, 'login/join.html', {'form': form})