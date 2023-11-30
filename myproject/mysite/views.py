# from django.http import HttpResponse # 삭제
from django.shortcuts import render
from .models import MainContent
def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)