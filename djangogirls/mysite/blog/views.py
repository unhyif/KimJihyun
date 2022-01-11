from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {}) # model에서 필요한 정보를 받아 template에 전달