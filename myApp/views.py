from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import Grades,Students,Monthreport,Grade
from django.http import JsonResponse
def index(request):
    return HttpResponse("sunck is a good man")
# Create your views here.

def grades(request):
    gradesList=Grades.objects.all()
    return render(request,'myApp/grades.html',{"grades":gradesList})

def students(request):
    studentsList=Students.objects.all()
    username=request.POST.get('username')
    request.session['name']=username
    username1=request.session.get('name')
    return render(request,'myApp/students.html',{"students":studentsList,"username":username1})

def gradeStudents(request,num):
    grade=Grades.objects.get(pk=num)
    studentsList=grade.students_set.all()
    return render(request,'myApp/html/students.html',{"students":studentsList})
def gradeStudents2(request):
    grade=Grades.objects.get(pk=2)
    studentsList=grade.students_set.all()
    return render(request,'myApp/students.html',{"students":studentsList})
def gettest(request):
    a=request.GET.get('a')
    return HttpResponse(a)



#from django.views.decorators.clickjacking import xframe_options_exempt
#@xframe_options_exempt
#主页路由
def zff(request):
    return render(request,'myApp/html/login.html')
def index(request):
    return render(request,'myApp/html/index.html')
#@xframe_options_exempt
def main(request):
    return render(request,'myApp/html/pages/main.html')
def top1(request):
    return render(request,'myApp/html/top1.html')
#@xframe_options_exempt
def tab(request):
    return render(request,'myApp/html/tab.html')
#@xframe_options_exempt
def left1(request):
    return render(request,'myApp/html/left1.html')
def footer(request):
    return render(request,'myApp/html/footer.html')

#月报表查询
def monthreport(request):
    if request.method == 'POST':
        trainstarttime1 = request.POST.get("trainstarttime1")
        trainstarttime2 = request.POST.get("trainstarttime2")
        traintype = request.POST.get("traintype")
        trainproperty = request.POST.get("trainproperty")
        if trainproperty=="全部" and traintype=="":
            mreport = Monthreport.objects.filter(trainstarttime__range=[trainstarttime1, trainstarttime2])
        elif trainproperty=="全部":
            mreport = Monthreport.objects.filter(traintype=traintype,trainstarttime__range=[trainstarttime1,trainstarttime2])
        elif traintype=="":
            mreport = Monthreport.objects.filter(trainproperty=trainproperty,trainstarttime__range=[trainstarttime1, trainstarttime2])
        else:
            mreport = Monthreport.objects.filter(traintype=traintype, trainproperty=trainproperty,trainstarttime__range=[trainstarttime1,trainstarttime2])
        return render(request, 'myApp/html/monthreport/monthreport.html', {'monthreport': mreport,'trainstarttime1':trainstarttime1,
                                                                           'trainstarttime2':trainstarttime2,
                                                                           'traintype':traintype,
                                                                           'trainproperty':trainproperty})
    elif request.method == 'GET':
        mreport = Monthreport.objects.all()
        return render(request, 'myApp/html/monthreport/monthreport.html', {'monthreport': mreport})
#修改月报表
def changetimetofront(stime):#改写时间格式传给前端
    stime=str(stime)
    return stime[0:4]+"-"+stime[5:7]+"-"+stime[8:10]

def modifymonthreport(request):
    trainid=request.GET.get("id")
    mreport=Monthreport.objects.get(id=trainid)
    trainstarttime=changetimetofront(mreport.trainstarttime)
    trainendtime = changetimetofront(mreport.trainendtime)
    theorytime=changetimetofront(mreport.theorytime)
    practisetime=changetimetofront(mreport.practisetime)
    return render(request,"myApp/html/monthreport/modifymonthreport.html",{'contactname':mreport.contactname,'company':mreport.company,'trainstarttime':trainstarttime,'trainendtime':trainendtime,
                                                               'traintype':mreport.traintype,'worktype':mreport.worktype,'operatetype':mreport.operatetype,
                                                               'trainproperty':mreport.trainproperty,'trainplace':mreport.trainplace,
                                                               'theorytime':theorytime,'practisetime':practisetime,
                                                               'trainnumber':mreport.trainnumber,'id':mreport.id})
def modifymonthreportdata(request):
    trainstarttime=request.POST.get('trainstarttime')
    trainendtime = request.POST.get('trainendtime')
    traintype = request.POST.get('traintype')
    worktype = request.POST.get('worktype')
    theorytime = request.POST.get('theorytime')
    practisetime = request.POST.get('practisetime')
    trainplace = request.POST.get('trainplace')
    trainnumber = request.POST.get('trainnumber')
    trainproperty = request.POST.get('trainproperty')
    operatetype=request.POST.get('operatetype')
    company=request.POST.get('company')
    id=request.POST.get('id')
    mreport=Monthreport.objects.get(id=id)
    mreport.trainstarttime=trainstarttime
    mreport.trainendtime=trainendtime
    mreport.trainproperty=trainproperty
    mreport.traintype=traintype
    mreport.trainnumber=trainnumber
    mreport.trainplace=trainplace
    mreport.worktype=worktype
    mreport.company=company
    mreport.theorytime=theorytime
    mreport.practisetime=practisetime
    mreport.operatetype=operatetype
    mreport.save()
    return render(request,'myApp/html/monthreport/success.html')

#增加月报表数据
def addmonthreport(request):
    return render(request,'myApp/html/monthreport/addmonthreport.html')

def addmonthreportdata(request):
    company=request.POST.get("company")
    contactname=request.POST.get("contactname")
    trainstarttime = request.POST.get('trainstarttime')
    trainendtime = request.POST.get('trainendtime')
    traintype = request.POST.get('traintype')
    worktype = request.POST.get('worktype')
    operatetype = request.POST.get('operatetype')
    theorytime = request.POST.get('theorytime')
    practisetime = request.POST.get('practisetime')
    trainplace = request.POST.get('trainplace')
    trainnumber = request.POST.get('trainnumber')
    trainproperty = request.POST.get('trainproperty')
    mreport = Monthreport()
    mreport.contactname=contactname
    mreport.company=company
    mreport.trainstarttime = trainstarttime
    mreport.trainendtime = trainendtime
    mreport.trainproperty = trainproperty
    mreport.traintype = traintype
    mreport.trainnumber = trainnumber
    mreport.trainplace = trainplace
    mreport.worktype = worktype
    mreport.operatetype=operatetype
    mreport.theorytime = theorytime
    mreport.practisetime = practisetime
    mreport.save()
    return render(request, 'myApp/html/monthreport/success.html')
#删除月报表数据
import json
def deletemonthreportdata(request):
    back_dic = {'testdata': None}
    id=request.POST.get("id")
    mreport=Monthreport.objects.get(id=id)
    mreport.delete()
    back_dic['testdata']="数据删除成功！"
    return HttpResponse(json.dumps(back_dic))


#开班情况
def startgrade(request):
    if request.method == 'POST':
        trainstarttime1 = request.POST.get("trainstarttime1")
        trainstarttime2 = request.POST.get("trainstarttime2")
        trainproperty = request.POST.get("trainproperty")
        gradenum = request.POST.get("gradenum")
        if trainproperty == "全部":
            if gradenum:
                sg = Grade.objects.filter(gradenum=gradenum)
            else:
                sg= Grade.objects.filter(gradestarttime__range=[trainstarttime1, trainstarttime2])
        else:
            if gradenum:
                sg = Grade.objects.filter(gradenum=gradenum)
            else:
                sg= Grade.objects.filter(trainproperty=trainproperty,gradestarttime__range=[trainstarttime1,trainstarttime2])
        return render(request, 'myApp/html/startgrade/startgrade.html',
                      {'sgrade': sg, 'trainstarttime1': trainstarttime1,
                       'trainstarttime2': trainstarttime2,
                       'trainproperty': trainproperty, 'gradenum': gradenum})
    elif request.method == 'GET':
        sg = Grade.objects.all()
        return render(request, 'myApp/html/startgrade/startgrade.html',{'sgrade':sg})
def modifystartgrade(request):
    gradeid = request.GET.get("id")
    sgrade = Grade.objects.get(id=gradeid)
    gradestarttime = changetimetofront(sgrade.gradestarttime)
    traintime = changetimetofront(sgrade.traintime)
    examtime= changetimetofront(sgrade.examtime)
    return render(request, "myApp/html/startgrade/modifystartgrade.html",
                  {'gradenum': sgrade.gradenum, 'traintype': sgrade.traintype,
                   'worktype': sgrade.worktype, 'trainproperty':sgrade.trainproperty,
                   'gradenumber': sgrade.gradenumber, 'gradestarttime': gradestarttime,
                   'traintime': traintime, 'examtime': examtime,
                   'teachername':sgrade.teachername,
                   'trainplace': sgrade.trainplace,
                   'id': sgrade.id})


def modifystartgradedata(request):
    gradenum=request.POST.get("gradenum")
    traintype = request.POST.get("traintype")
    worktype = request.POST.get("worktype")
    gradenumber = request.POST.get("gradenumber")
    gradestarttime = request.POST.get("gradestarttime")
    traintime = request.POST.get("traintime")
    examtime = request.POST.get("examtime")
    teachername = request.POST.get("teachername")
    trainplace = request.POST.get("trainplace")
    trainproperty = request.POST.get('trainproperty')
    id = request.POST.get('id')
    sgrade=Grade.objects.get(id=id)
    sgrade.gradenumber=gradenumber
    sgrade.traintype=traintype
    sgrade.worktype=worktype
    sgrade.trainplace=trainplace
    sgrade.gradenum=gradenum
    sgrade.trainproperty=trainproperty
    sgrade.teachername=teachername
    sgrade.gradestarttime=gradestarttime
    sgrade.traintime=traintime
    sgrade.examtime=examtime
    sgrade.save()
    return render(request, 'myApp/html/monthreport/success.html')
#增加开班信息
def addstartgrade(request):
    return render(request, 'myApp/html/startgrade/addstartgrade.html')
def addstartgradedata(request):
    gradenum = request.POST.get("gradenum")
    traintype = request.POST.get("traintype")
    worktype = request.POST.get("worktype")
    gradenumber = request.POST.get("gradenumber")
    gradestarttime = request.POST.get("gradestarttime")
    traintime = request.POST.get("traintime")
    examtime = request.POST.get("examtime")
    teachername = request.POST.get("teachername")
    trainplace = request.POST.get("trainplace")
    trainproperty = request.POST.get('trainproperty')
    sgrade = Grade()
    sgrade.gradenumber = gradenumber
    sgrade.traintype = traintype
    sgrade.worktype = worktype
    sgrade.trainplace = trainplace
    sgrade.gradenum = gradenum
    sgrade.trainproperty = trainproperty
    sgrade.teachername = teachername
    sgrade.gradestarttime = gradestarttime
    sgrade.traintime = traintime
    sgrade.examtime = examtime
    sgrade.save()
    return render(request, 'myApp/html/monthreport/success.html')
#删除开班信息
def deletestartgradedata(request):
    back_dic = {'testdata': None}
    id = request.POST.get("id")
    sgrade = Grade.objects.get(id=id)
    sgrade.delete()
    back_dic['testdata'] = "数据删除成功！"
    return HttpResponse(json.dumps(back_dic))

#文件上传
def upfile(request):
    return render(request,'myApp/upfile.html')



import os
from django.conf import settings
def savefile(request):
    #判断请求，上传文件必须是post请求
    if request.method=='POST':
        f=request.FILES.get("file")
        filePath=os.path.join(settings.MDEIA_ROOT,f.name)
        with open(filePath,'wb') as fp:
            for info in f.chunks():
                fp.write(info)
        return HttpResponse('上传成功')
    else:
        return HttpResponse('上传失败')


def dividestartgrade(request):
    id=request.GET.get('id')
    mreport=Monthreport.objects.get(id=id)
    return render(request,'myApp/html/monthreport/dividestartgrade.html',{'mr':mreport})

def logintest(request):
    username=request.session.get('name',"游客")
    return render(request,'myApp/logintest.html',{'name':username})


def json_test(request):
    data = {}
    studentjson = Students.objects.values()
    data['list'] = list(studentjson)
    print(data)
    return JsonResponse(data)


