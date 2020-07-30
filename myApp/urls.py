from django.urls import path,re_path
from . import views
urlpatterns = [
    path('grades', views.grades),
    path('students',views.students),
    path('<int:num>/',views.gradeStudents),
    path('gettest',views.gettest),

   #主页路由
    path('zff',views.zff),
    path('index.html',views.index),
    path('top1',views.top1),
    path('tab',views.tab),
    path('left1',views.left1),
    path('footer',views.footer),

    #月报表增珊改查
    path('monthreport.html',views.monthreport),
    path('main.html',views.main),
    path('modifymonthreport.html',views.modifymonthreport),
    path('modifymonthreportdata',views.modifymonthreportdata),
    path('addmonthreport.html',views.addmonthreport),
    path('addmonthreportdata',views.addmonthreportdata),
    path('deletemonthreportdata',views.deletemonthreportdata),
    #分班
    path('dividestartgrade.html',views.dividestartgrade),

    #开班情况
    path('startgrade.html',views.startgrade),
    path('modifystartgrade.html',views.modifystartgrade),
    path('modifystartgradedata',views.modifystartgradedata),
    path('addstartgrade.html',views.addstartgrade),
    path('addstartgradedata',views.addstartgradedata),
    path('deletestartgradedata',views.deletestartgradedata),


    path('logintest',views.logintest),
    path('upfile',views.upfile),
    path('savefile',views.savefile),

]