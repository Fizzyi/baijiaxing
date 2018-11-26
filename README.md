# 项目介绍

## 爬虫项目

爬取地址: http://www.resgain.net/xmdq.html

爬取内容:为该网址下的所有姓氏和姓氏名字

爬取步骤:

- 先爬取所有的姓氏，包括姓氏，姓氏的中文，每个姓氏的URL
- 然后在进每一个姓氏的网址进去爬取每个姓氏下的名字，每个姓氏下都有十页，但是发现并不是每一页都是存在姓名的。
- 最后进每一个姓氏的详细页面，爬取每个姓名的相同人数和五行和三才。

工作环境和爬取的框架： python3  scrapy   

爬取数据量:  姓氏435个  姓名140万数据



## django项目

## 项目介绍
缘由：前几天爬取了姓名大全网站，数据在140万左右，所以想做一个django网站来展示所有的数据，顺便复习下django的知识以及上线的步骤。

前端模版：来自于 [ 凡科网 ](https://ajz.fkw.com/pro11.html?_ta=2298)

环境：python 3.6  Django 1.11



简书地址：https://www.jianshu.com/u/e40231715a90

个人博客地址：http://fizzyi.com/

线上地址 : http://baijiaxing.fizzyi.com/