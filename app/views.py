from django.shortcuts import render
from app.models import *
from django.db.models import Q
from django.db.models.functions import Length
from django.db.models import *
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

    #displaying the details of emp whose sal is greater or equal to average salary
    AVGSAL=Emp.objects.aggregate(sal_avg=Avg('sal'))['sal_avg']
    JDED=Emp.objects.select_related('deptno').filter(sal__gte=AVGSAL)
    JDED=Emp.objects.select_related('deptno').filter(sal__lte=AVGSAL)
    print(JDED)
    #Annotate
    EGAD=Emp.objects.values('deptno').annotate(g_a_s=Avg('sal'))
    print(EGAD)
    #WAQ to display deptno whose dept avg sal is greater than avg sal of all employees
    AEAS=Emp.objects.aggregate(A_E_A_S=Avg('sal'))['A_E_A_S']
    Emp.objects.values('deptno').annotate(G_A_S=Avg('sal')).filter(G_A_S__gte=AEAS)
    print(AEAS)

   
    
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
    
    Aggregate
    EAD=Emp.objects.aggregate(sal_sum=Sum('sal'))# gives dictionary ie key-value pairs
    EAD=Emp.objects.aggregate(sal_sum=Sum('sal'))['sal_sum']# gives only values
    EAD=Emp.objects.aggregate(sal_avg=Avg('sal'))#o/p {'sal_avg': Decimal('7680')}
    EAD=Emp.objects.aggregate(date_max=Max('hiredate'))#o/p {'date_max': datetime.date(2024, 5, 14)}
    EAD=Emp.objects.aggregate(date_min=Min('hiredate'))#o/p {'date_min': datetime.date(2021, 5, 15)}
    EAD=Emp.objects.aggregate(sal_count=Count('sal'))#o/p {'sal_count': 5}
    
    print(EAD)

    d={'EMDJD':EMDJD}
    return render(request,'empmgrdept.html',d)

def update_emp(request):
    #Updating Query

    Emp.objects.filter(ename='Priyanka').update(job='Clerk')#update donot create variable
    Emp.objects.filter(job='Manager').update(sal=2000)#managers sal updated to 2000
    Emp.objects.filter(ename='Jasmin').update(deptno=10)#update method takes VALUE of parent table directly
    Emp.objects.update_or_create(ename='Alekya', defaults={'sal':1500})
    Emp.objects.update_or_create(job='President', defaults={'sal':5000})
    #Emp.objects.update_or_create(job='Analyst', defaults={'deptno':40})#Emp.deptno must be a "Dept" instance
    #Therefore for above statement create an Object bz update_or_create method takes OBJECT of parent table
    DO=Dept.objects.get(deptno=40)
    Emp.objects.update_or_create(job='Analyst', defaults={'deptno':DO})#update_or_create method takes OBJECT
    MO=Emp.objects.get(empno=3333)
    Emp.objects.update_or_create(job='Teacher',defaults={"ename":'Gargi','empno':6666,'hiredate':'1999-03-19','sal':3500,'comm':50,'deptno':DO,'mgr':MO})

    EMPO=Emp.objects.all()
    d={'EMPO':EMPO}
    return render(request,'updateemp.html',context=d)

def delete_emp(request):

    Emp.objects.filter(ename='Gargi').delete()#gargi row deleted
    Emp.objects.filter(job='Manager').delete()
    Emp.objects.filter(deptno=30).delete()
    Dept.objects.filter(dname='Accounting').delete()#delete parent table data, so child table data also deleted
    #Emp.objects.delete().....deletes entire Emp table rows
    DEPO=Emp.objects.all()
    d={'DEPO':DEPO}

    return render(request,'deleteemp.html',d)
