from django.shortcuts import render,HttpResponseRedirect
import MySQLdb
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import simplejson as json
from datetime import date
from datetime import datetime
import datetime
import webbrowser
import math, random 
import smtplib
from email.message import EmailMessage

def mail(y,ms):
    msg = EmailMessage()
    msg.set_content(ms)
    
    msg['Subject'] = 'RepGov'
    msg['From'] = "responsivegovernance@gmail.com"
    msg['To'] = y
        
    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("responsivegovernance@gmail.com", "ResGov@111")
    server.send_message(msg)
    server.quit()


def sendsms(ph,msg):
    sendToPhoneNumber= "+91"+ph
    userid = "2000022557"
    passwd = "54321@lcc"
    url = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=sendMessage&send_to=" + sendToPhoneNumber + "&msg=" + msg + "&userid=" + userid + "&password=" + passwd + "&v=1.1&msg_type=TEXT&auth_scheme=PLAIN"
    # contents = urllib.request.urlopen(url)
    webbrowser.open(url)

def generateOTP() :   
    # Declare a digits variable   
    # which stores all digits  
    digits = "0123456789"
    OTP = "" 
   # length of password can be chaged 
   # by changing value in range 
    for i in range(4) : 
        print(i)
        OTP += digits[math.floor(random.random() * 10)] 
    return OTP 

# Create your views here.

db = MySQLdb.connect('localhost','root','','respgov')
c = db.cursor()

def AdminHome(request):
    return render(request,'AdminHome.html') 

def CommonHome(request):
    return render(request,'CommonHome.html')

def CustomerHome(request):
    return render(request,'CustomerHome.html')

def DeptHeadHome(request):
    return render(request,'DeptHeadHome.html')

def EmployeeHome(request):
    sid = request.session['sid']
    c.execute("select count(*) from staff_allot where sid = '"+str(sid)+"'")
    data = c.fetchall()
    count = data[0][0]
    return render(request,'EmployeeHome.html',{"data":count})

def SignIn(request):  
    request.session['username']=""
    request.session['NAME']=""
    request.session['cid']=""
    # msg=""
    # if request.POST:
    #     email = request.POST.get("Username")
    #     password = request.POST.get("Password")
    #     c.execute("select * from login where uname='"+ email +"' and pass='"+ password +"' and status='1'")
    #     ds = c.fetchone()
    #     c.execute("select count.* from login where uname='"+ email +"' and pass='"+ password +"' and status='1' ")
    #     q=c.fetchone()
    #     if(q>0):
    ds=""
    msg=""
    if(request.POST):
        email=request.POST.get("Username")
        password=request.POST.get("Password")
        s="select count(*) from login where uname='"+email+"' and pass='"+password+"' and status='1'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            s="select * from login where uname='"+email+"' and pass='"+password+"' and status='1'"
            c.execute(s)
            ds=c.fetchone()   
            request.session['username']=email
            if not bool(ds):
                msg = "Incorrect username or password"
            if ds[2] == 'Admin':
                
                return HttpResponseRedirect('/AdminHome/')
             

            elif ds[2] == 'Customer':
                c.execute("select * from cust_reg where email='"+email+"' and password='"+password+"'")
                ds = c.fetchone()
                request.session['cid'] = ds[0]
                request.session['NAME'] = ds[1]
                request.session['fon'] = ds[5]
                return HttpResponseRedirect('/CustomerHome/')
            elif ds[2] == 'Employee':
                c.execute("select * from employee_reg where email='"+email+"' and password='"+password+"'")
                ds = c.fetchone()
                request.session['sid'] = ds[0]
                request.session['NAME'] = ds[1]
                return HttpResponseRedirect('/EmployeeHome/')
            elif ds[2] == 'DeptHead':
                c.execute("select * from dept_head where email='"+email+"' and password='"+password+"'")
                ds = c.fetchone()
                request.session['deptid'] = ds[0]
                request.session['NAME'] = ds[1]
                request.session['did'] = ds[5]
                return HttpResponseRedirect('/DeptHeadHome/')
        else:
            msg="invalid user"
    return render(request,'Signin.html',{"msg":msg}) 

def Customer_Registration(request):
    msg = ""
    if request.POST:
        cname = request.POST.get("cname")
        address = request.POST.get("address")
        district = request.POST.get("district")
        location = request.POST.get("location")
        email = request.POST.get("Email")
        mobile = request.POST.get("mobile")
        aadhar = request.POST.get("aadhar")
      
        password = request.POST.get("Password")
        type= "Customer"
        qry="insert into cust_reg(cname,address,district,location,mobile,email,aadhar,password) values('"+ cname +"','"+ address +"','"+ district +"','"+ location +"','"+ mobile +"','"+ email +"','"+str(aadhar)+"','"+ password +"')"
        qr ="insert into login values('"+ email +"','"+ password +"','"+ type +"','1')"
        c.execute(qry)
        c.execute(qr)
        db.commit()
        y = email
        msg = "Registartion Completed Successfully."
        ms = "Greetings '"+str(cname)+"'. Registartion Completed Successfully. \n Your login credentials are \nUsername : '"+str(y)+"'\nPassword : '"+str(password)+"'\nWish you a happy day.\n\nDepartment Head - RespGovn\n\nGov Of India "
        mail(y,ms) 

    return render(request,'Signup.html',{"msg":msg})

def AdminAddDepartment(request):
    msg=""
    if request.POST:
        na = request.POST.get("cat")
        qry="insert into department(dename) values('"+ na +"')"
        c.execute(qry)
        db.commit()
        msg = "Department Added Successfully."
    c.execute("select * from department")
    data=c.fetchall() 
    if request.GET:
        a = request.GET.get('id')
        c.execute("delete from department where deid= '"+str(a)+"'")
        db.commit()
        return HttpResponseRedirect("/AdminAddDepartment/")
    return render(request,'AdminAddDepartment.html',{"data":data,"msg":msg})

def AdminAddDepartmentHead(request):
    c.execute("select * from department")
    data=c.fetchall()
    msg=""  
    if request.POST:
        a=request.POST.get("pname")
        b=request.POST.get("pdesc")
        c1=request.POST.get("email")   
        d=request.POST.get('pass')
        e=request.POST.get('cat')
        c.execute("insert into dept_head(dename,phone,email,password,dept) values('"+ str(a) +"','"+ str(b) +"','"+ str(c1) +"','"+ str(d) +"','"+str(e)+"')")
        c.execute("insert into login values('"+c1+"','"+d+"','DeptHead','1')")
        db.commit()       
        msg = "Department Head Alloted Successfully."
    return render(request,"AdminAddDepartmentHead.html",{"cat":data,"msg":msg})

def AdminViewDeptHead(request):
    c.execute("select * from dept_head inner join department on dept_head.dept = department.deid ")
    data=c.fetchall() 
    
    if request.GET:
        eid = request.GET.get('id')
        
        c.execute("delete from dept_head where deptid = '"+str(eid)+"'")
        
        db.commit()
        msg = "Department Head Removed Successfully."
        return HttpResponseRedirect("/AdminViewDeptHead/")
    return render (request,"AdminViewDeptHead.html",{"data":data})
def AdminViewConsumers(request):
    c.execute("select * from cust_reg")
    data=c.fetchall() 
    if request.GET:
        cid = request.GET.get('id')
        
        c.execute("delete from cust_reg where cid = '"+str(cid)+"'")
        db.commit()
        return HttpResponseRedirect("/AdminViewConsumers/")
    return render (request,"AdminViewConsumers.html",{"data":data})
def AdminViewFeedback(request):
    data = ""
    c.execute("select * from cust_reg inner join feedback on cust_reg.cid = feedback.cid")
    data=c.fetchall() 
    return render (request,"AdminViewFeedback.html",{"data":data})

def DeptHeadAddEmployee(request):
    did = request.session['did']
    msg=""  
    if request.POST:
        a=request.POST.get("pname")
        f=request.POST.get("district")
        b=request.POST.get("pdesc")
        c1=request.POST.get("email")   
        d=request.POST.get('pass')
        e=request.POST.get('cat')
        c.execute("insert into employee_reg(ename,district,phone,email,password,dept) values('"+ str(a) +"','"+str(f)+"','"+ str(b) +"','"+ str(c1) +"','"+ str(d) +"','"+str(did)+"')")
        c.execute("insert into login values('"+c1+"','"+d+"','Employee','1')")
        db.commit()       
        msg = "Employee Added Successfully."
    return render(request,"DeptHeadAddEmployee.html",{"msg":msg})

def DeptHeadViewEmployee(request):
    did = request.session['did']
    c.execute("select * from employee_reg where dept ='"+str(did)+"' ")
    data=c.fetchall() 
    if request.GET:
        eid = request.GET.get('id')
        c.execute("delete from employee_reg where eid = '"+str(eid)+"'")
        db.commit()
        return HttpResponseRedirect("/DeptHeadViewEmployee/")
    return render (request,"DeptHeadViewEmployee.html",{"data":data})

def DeptHeadViewDetailComplaint(request):
    a = request.session["did"]
    c.execute("select * from complaint_reg inner join cust_reg on complaint_reg.cid = cust_reg.cid where complaint_reg.status = 'Registered' and complaint_reg.did = '"+str(a)+"'")
    #c.execute("select * from complaint_reg,dept_head where complaint_reg.did = '"+str(a)+"' and complaint_reg.district = dept_head.district and complaint_reg.did=dept_head.dept")
    data=c.fetchall() 
    if request.GET:
        coid = request.GET.get('id')
        st = request.GET.get('st')
        fo = request.GET.get('fo')
        di = request.GET.get('di')
       
        if st == "Forward":
            request.session['coid'] = coid
            request.session['st'] = st
            request.session['fo'] = fo
            request.session['di'] = di
            return HttpResponseRedirect("/DeptHeadForwardComplaint/")
        else :
            c.execute("delete from complaint_reg where comid = '"+coid+"'")
            db.commit()
            msg = "Your complaint was rejected."
            sendsms(fo,msg)
            return HttpResponseRedirect("/DeptHeadViewDetailComplaint/")
    return render(request,"DeptHeadViewDetailComplaint.html",{"data":data})

def DeptHeadViewStatusForwarded(request):
    did = request.session['did']
    c.execute("select * from complaint_reg inner join cust_reg on complaint_reg.cid = cust_reg.cid inner join staff_allot on staff_allot.compid = complaint_reg.comid inner join employee_reg on employee_reg.eid = staff_allot.sid where complaint_reg.status = 'Forwarded' or complaint_reg.status = 'Processing' and complaint_reg.did = '"+str(did)+"'")
    data=c.fetchall() 
    
    ms = "Greetings. Your Complaint forwarded. And your complaint ID"
    
    return render (request,"DeptHeadViewStatusForwarded.html",{"data":data})

def DeptHeadForwardComplaint(request):
    di = request.session['di'] 
    de = request.session["did"]
    c.execute("select * from employee_reg where district = '"+di+"' and dept = '"+str(de)+"'")
    data=c.fetchall()
    
    
    if request.POST:
        coid = request.session['coid']
        cat = request.POST.get('cat')
        c.execute("update complaint_reg set status = 'Forwarded' where comid = '"+coid+"'")
        
        c.execute("insert into staff_allot(compid,sid) values('"+coid+"','"+cat+"')")
        db.commit()
        fo = request.session['fo']    

        msg = "Your complaint was forwarded to an employee."
        
        #sendsms(fo,msg)
        return HttpResponseRedirect("/DeptHeadViewDetailComplaint/")
    return render (request,"DeptHeadForwardComplaint.html",{"data":data})

def EmployeeViewComplaints(request):
    sid = request.session['sid']
    c.execute("select * from complaint_reg inner join staff_allot on complaint_reg.comid = staff_allot.compid inner join cust_reg on  cust_reg.cid = complaint_reg.cid where staff_allot.sid = '"+str(sid)+"' and complaint_reg.status = 'Forwarded' or complaint_reg.status = 'Processing'")
    data=c.fetchall()
    if request.GET:
        st = request.GET.get("st")
        coid = request.GET.get("id")
        if st == 'Solved':
            c.execute("update complaint_reg set status = '"+st+"' where comid= '"+str(coid)+"'")
            db.commit()
            return HttpResponseRedirect("/EmployeeViewComplaints/")
        else:
            c.execute("update complaint_reg set status = 'Processing' where comid= '"+str(coid)+"'")
            db.commit()
            return HttpResponseRedirect("/EmployeeViewComplaints/")
    return render (request,"EmployeeViewComplaints.html",{"data":data})

# def EmployeeAddNotification(request):
#     msg=""
#     today = date.today()
#     sid = request.session['sid']
#     if request.POST:
#         na = request.POST.get("pname")
#         qry="insert into department(dename) values('"+ na +"')"
#         c.execute(qry)
#         db.commit()
#         msg = "Department Added Successfully."
#     return render(request,'EmployeeAddNotification.html',{"data":data,"msg":msg})

def CustomerAddComplaint(request):
    c.execute("select * from department")
   
    data=c.fetchall()
    cid = request.session['cid']
    y = request.session['username']
    fon = request.session['fon']
    today = date.today()
    msg=""  
    maxid=""
    if request.POST:
        a=request.POST.get("district")
        b=request.POST.get("pname")
        h=request.POST.get("consnum")
        c1=request.POST.get("cat")   
        c.execute("insert into complaint_reg(cid,did,district,complaint,cdate,status,consumer_no) values('"+ str(cid) +"','"+ str(c1) +"','"+ str(a) +"','"+ str(b) +"','"+str(today)+"','Registered','"+ str(h) +"')")
       
        db.commit()  
        c.execute("select max(comid) from complaint_reg")   
        maxid = c.fetchone() 
        mid = maxid[0]
        msg = "Greetings. Your Complaint Registerd Successfully. And your complaint ID is "+ str(mid)
        ms = "Greetings. Your Complaint Registerd Successfully. And your complaint ID"+ str(mid)+"\nYou can check the status of complaint through RepGov Website.\n\nWish you a happy day.\n\nDepartment Head - RespGovn\n\nGov Of India "
        mail(y,ms)     
        #sendsms(fon,msg)
    return render(request,"CustomerAddComplaint.html",{"cat":data,"msg":msg})

def CustomerViewComplaintStatus(request):
    cid = request.session['cid']
    data = ""
    if request.POST:
        comp = request.POST.get('comp')
        c.execute("select * from complaint_reg inner join staff_allot on complaint_reg.comid = staff_allot.compid inner join employee_reg on employee_reg.eid = staff_allot.sid where comid = '"+str(comp)+"' and cid = '"+str(cid)+"'")
        print("select * from complaint_reg inner join staff_allot on complaint_reg.comid = staff_allot.compid inner join employee_reg on employee_reg.eid = staff_allot.sid where comid = '"+str(comp)+"' and cid = '"+str(cid)+"'")
        data = c.fetchall()
    return render(request,"CustomerViewComplaintStatus.html",{"data":data})
def Customerviewprofile(request):
    msg=""
    data=""
    item=""
    cid = request.session['cid']
    s="select * from cust_reg where cid='"+str(cid)+"'"
    data=c.execute(s)
    print(s)
    data=c.fetchall()
    c.execute("select uname from login,cust_reg where login.uname=cust_reg.email and cust_reg.cid='"+str(cid)+"'")
    dd=c.fetchone()
    cemail=dd[0]
    print(data)
    c.execute("select * from login where uname='"+str(cemail)+"'")
    item=c.fetchall()
    print(data)
    if(request.POST):
        na=request.POST.get('t1')
        add=request.POST.get('t2')
        loc=request.POST.get('t3')
        dis=request.POST.get('t4')
        mob=request.POST.get('t5')
        email=request.POST.get('t6')
        aadhar=request.POST.get('t7')
        password=request.POST.get('t8')
        c.execute("update cust_reg set cname='"+str(na)+"',address='"+str(add)+"',district='"+str(loc)+"',location='"+str(dis)+"',mobile='"+str(mob)+"',email='"+str(email)+"',aadhar='"+str(aadhar)+"',password='"+str(password)+"' where cid='"+str(cid)+"'")
        db.commit() 
        c.execute("update login set uname='"+ str(email) +"',pass='"+str(password) +"' where uname='"+str(cemail)+"' ")
        db.commit()
        msg="updated successfully"
        # data.cname=na
        # data.address=add
        # data.district=loc
        # data.location=dis
        # data.mobile=mob
        # data.email=email
        # data.aadhar=aadhar
        # data.ksebcno=kno
        # data.waternum=wno
        # data.password=password
        # item.uname=email
        # item[1]=password
        # data.save()
        # item.save()
        
    return render(request,"CustomerViewprofile.html",{"data":data,"item":item,"msg":msg})

def CustomerAddFeedback(request):
    c.execute("select * from department")
    data=c.fetchall()
    msg=""
    cid = request.session['cid']  
    if request.POST:
        a=request.POST.get("pname")
        e=request.POST.get('cat')
        b = date.today()
        c.execute("insert into feedback(cid,feedback,fdate,diid) values('"+str(cid)+"','"+a+"','"+str(b)+"','"+str(e)+"')")
        db.commit()
        msg = "Feedback Added Successfully."
    return render(request,"CustomerAddFeedback.html",{"cat":data,"msg":msg})

def CustomerViewNotification(request):
    cid = request.session['cid']
    data = ""
    if request.POST:
        comp = request.POST.get('comp')
        c.execute("select * from complaint_reg inner join staff_allot on complaint_reg.comid = staff_allot.compid inner join employee_reg on employee_reg.eid = staff_allot.sid where comid = '"+str(comp)+"' and cid = '"+str(cid)+"'")
        data = c.fetchall()
    return render(request,"CustomerViewNotification.html",{"data":data})



def DeptHeadViewFeedback(request):
    j = request.session['did']
    data = ""
    c.execute("select * from cust_reg inner join feedback on cust_reg.cid = feedback.cid and feedback.diid = '"+str(j)+"'")
    data=c.fetchall() 
    return render (request,"DeptHeadViewFeedback.html",{"data":data})

