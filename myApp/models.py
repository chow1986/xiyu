from django.db import models

# Create your models here.
class Grades(models.Model):
    gname=models.CharField(max_length=20)
    gdate=models.DateTimeField()
    ggirlnum=models.IntegerField()
    gboynum=models.IntegerField()
    isDelete=models.BooleanField(default=False)
    def _str_(self):
        return self.gname

class Students(models.Model):
    sname=models.CharField(max_length=20)
    sgender=models.BooleanField()
    sage=models.IntegerField()
    scontend=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    #关联外键
    sgrade=models.ForeignKey("Grades",on_delete=models.CASCADE)
    def _str_(self):
        return self.sname

#浙江省安全生产管理与特种作业人员培训考核计划月报表
class Monthreport(models.Model):
    #单位
    company=models.CharField(max_length=30)
    #联系人姓名
    contactname=models.CharField(max_length=20)
    #联系电话
    contactphone=models.CharField(max_length=20)
    #培训开始时间
    trainstarttime=models.DateField()
    #培训结束时间
    trainendtime=models.DateField()
    #培训性质(初训、复训)
    trainproperty=models.CharField(max_length=10)
    #培训类型
    traintype=models.CharField(max_length=20)
    #培训工种
    worktype=models.CharField(max_length=20)
    #操作项目
    operatetype=models.CharField(max_length=20)
    #培训地点
    trainplace=models.CharField(max_length=20)
    #培训人数
    trainnumber=models.IntegerField()
    #理论时间
    theorytime=models.DateField()
    #实践时间
    practisetime=models.DateField()
    #备注
    remark1=models.CharField(max_length=30)
    remark2=models.CharField(max_length=30)

#开班一览表
class Grade(models.Model):
    #开班编号
    gradenum=models.CharField(max_length=10)
    #开班项目
    traintype=models.CharField(max_length=20)
    #开班工种
    worktype=models.CharField(max_length=20)
    #培训性质
    trainproperty=models.CharField(max_length=20)
    #培训人数
    gradenumber=models.IntegerField()
    #开班时间
    gradestarttime=models.DateField()
    #实操时间
    traintime=models.DateField()
    #授课教师
    teachername=models.CharField(max_length=20)
    #考试时间
    examtime=models.DateField()
    #开班地点
    trainplace=models.CharField(max_length=20)
    #备注
    remark=models.CharField(max_length=20)