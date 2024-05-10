from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100,unique=True)
    loc=models.CharField(max_length=100)

    def __str__(self):
        return str(self.deptno)


class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    hiredate=models.DateField()
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    job=models.CharField(max_length=100)

    def __str__(self):
        return self.ename

class Salgrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    lowsal=models.DecimalField(max_digits=10,decimal_places=2)
    highsal=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.grade)