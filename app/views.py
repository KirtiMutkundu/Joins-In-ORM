from django.shortcuts import render
from app.models import *
from django.db.models import Q
from django.db.models.functions import Length
# Create your views here.
def innerEquijoins(request):
    JDED=Emp.objects.select_related('deptno').all()
    JDED=Emp.objects.select_related('deptno').filter(ename='Kirti')
    JDED=Emp.objects.select_related('deptno').filter(deptno__loc='Dallas')
    JDED=Emp.objects.select_related('deptno').filter(deptno__loc='Chicago',deptno__dname='Sales')
    JDED=Emp.objects.select_related('deptno').filter(Q(deptno='10') | Q(deptno='20'))
    JDED=Emp.objects.select_related('deptno').filter(Q(deptno__dname='Research') | Q(deptno__loc='New York'))
    JDED=Emp.objects.select_related('deptno').filter(Q(ename='Kirti') | Q(deptno__loc='Chicago'))
    JDED=Emp.objects.select_related('deptno').filter(Q(empno='1111') | Q(sal='1000'))
    JDED=Emp.objects.select_related('deptno').filter(sal__gt='700')
    JDED=Emp.objects.select_related('deptno').filter(job__startswith='s')
    JDED=Emp.objects.select_related('deptno').filter(Q(job__startswith='o') | Q(sal__lte='600'))
    JDED=Emp.objects.select_related('deptno').filter(hiredate='2023-07-07')
    JDED=Emp.objects.select_related('deptno').filter(comm='30')
    JDED=Emp.objects.select_related('deptno').filter(deptno__dname='Operations')
    JDED=Emp.objects.select_related('deptno').filter(Q(sal__lte='400') | Q(comm='0'))
    JDED=Emp.objects.select_related('deptno').filter(mgr=None)# no string
    JDED=Emp.objects.select_related('deptno').filter(Q(deptno__dname='Accounting') | Q(sal__gt='600'))
    JDED=Emp.objects.select_related('deptno').filter(Q(hiredate__gt='2024-12-12') | Q(comm__gte='10'))
    JDED=Emp.objects.select_related('deptno').filter(Q(job__startswith='o') | Q(sal__lte='600') |Q(deptno__dname='Accounting'))
    JDED=Emp.objects.select_related('deptno').filter(Q(deptno__dname='Research') | Q(deptno__loc='New York'), ename='Kirti' )
    JDED=Emp.objects.select_related('deptno').filter(Q(deptno='10') | Q(deptno__loc='Dallas'))
    JDED=Emp.objects.select_related('deptno').filter(ename__contains='r')# import Length for contains

    
    d={'JDED':JDED}
    return render(request,'innerEquijoins.html', d)

def selfjoins(request):
    EMJD=Emp.objects.select_related('mgr').all()
    EMJD=Emp.objects.select_related('mgr').filter(sal__lte=400)
    EMJD=Emp.objects.select_related('mgr').filter(mgr__ename='Kirti')
    EMJD=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    EMJD=Emp.objects.select_related('mgr').filter(mgr__isnull=False)


    d={'EMJD':EMJD}
    return render(request,'selfjoins.html',d)

def empmgrdept(request):
    EMDJD=Emp.objects.select_related('deptno','mgr').all()
    EMDJD=Emp.objects.select_related('deptno','mgr').filter(mgr__empno=1111)
    EMDJD=Emp.objects.select_related('deptno','mgr').filter(deptno__loc='Chicago')
    EMDJD=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__contains='s')
    EMDJD=Emp.objects.select_related('deptno','mgr').filter(ename='Priyanka',deptno__dname='Sales',job='Analyst')
    EMDJD=Emp.objects.select_related('deptno','mgr').filter(ename='Priyanka',deptno__dname='Sales')
    EMDJD=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)

    #WRITING RAW QUERIES USING EXTRA METHOD
    EMDJD=Emp.objects.extra(where=["LENGTH(ename) = 5"])
    EMDJD=Emp.objects.extra(where=["ename like'%y_' "])#checks 2nd last letter
    EMDJD=Emp.objects.extra(where=["ename like'%t_' "])#checks 2nd last letter
    EMDJD=Emp.objects.extra(where=["LENGTH(ename) = 5 or LENGTH(ename) = 6 "])
    EMDJD=Emp.objects.extra(where=["ename like'%i' "])#checks last letter
    EMDJD=Emp.objects.extra(where=["ename like'J%' "])#checks first letter

    d={'EMDJD':EMDJD}
    return render(request,'empmgrdept.html',d)


