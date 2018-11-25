import json

import pinyin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.models import Baijiaxing, Xingming


#获取所有的姓氏
def get_all(request):
    xingshi_lists = Baijiaxing.objects.all()
    the_max_leng = len(xingshi_lists)
    the_xingshi_list = []
    for i in range(0,len(list(xingshi_lists)),6):
        the_list = []
        for m in range(i,i+6):
            if m < the_max_leng:
                the_list.append(xingshi_lists[m])
        the_xingshi_list.append(the_list)
    return render(request,'index.html',{'the_xingshi_list':the_xingshi_list})


#获取每个姓氏的所有姓名并且进行分页
def get_one_xingshi(request,xingshi_id):
    try:
        xingshi = Baijiaxing.objects.filter(id=xingshi_id)[0]

        content = Xingming.objects.filter(xingshi_id = int(xingshi_id)).order_by('id')
        page_num = int(request.GET.get('page',1))
        paginator = Paginator(content,70)
        page = paginator.page(page_num)
        if not content:
            msg = '暂无此姓氏名字，快点击右上角添加吧'
        else:
            msg = ''
        return render(request,'components.html',{'page':page,'xingshi':xingshi,'msg':msg})
    except:
        return HttpResponse('暂无数据')

#获取每个姓名的信息
def get_one_info(request,xingming_id):
    try:
        the_info = Xingming.objects.filter(id = int(xingming_id))[0]
        return render(request,'tutorial.html',{'the_info':the_info})
    except:
        return HttpResponse('暂无数据')

#添加姓名
def add_one_xingming(request):
    if request.method == 'GET':
        return render(request,'landing.html')
    if request.method == 'POST':
        #获取传回来的数据
        xingshi = request.POST.get('xingshi')
        xingming = request.POST.get('xingming')
        five_elements = request.POST.get('five_elements')
        three_talents = request.POST.get('three_talents')
        #判断是否是真的没有这个姓名
        the_name = Xingming.objects.filter(name=xingming)
        if not the_name:
            #查询数据库中是否有该形式，有 只在姓名表上添加，没有 要在百家姓和姓名表都添加
            if not Baijiaxing.objects.filter(xingshi_zhongwen=xingshi):
                #没有这个姓氏
                #将姓氏转换为pinyin+数字  数字代表拼音
                the_xingshi = pinyin.get(xingshi, format='numerical', delimiter=" ")
                Baijiaxing.objects.create(xingshi=the_xingshi,xingshi_zhongwen=xingshi)
            the_xingshi_id = Baijiaxing.objects.filter(xingshi_zhongwen=xingshi).first().id
            Xingming.objects.create(name=xingming,five_elements=five_elements,three_talents=three_talents,xingshi_id=the_xingshi_id)
            return HttpResponseRedirect(reverse('app:index'))
        else:
            the_xingming = the_name.first()
            msg = '该姓名已经存在'
            return render(request,'landing.html',{'the_xingming':the_xingming,'msg':msg})

