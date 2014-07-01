from django.shortcuts import render,render_to_response,RequestContext, HttpResponseRedirect, HttpResponse
from django.core.context_processors import request
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from takeaway.models import Course,Session,TakeAway,School,Enrollment

# Create your views here.
def home(request):
    #course = Course.objects.create(course_name="MARKETING" , created_by="ravid")
    course_instance_list = Course.objects.filter(students=request.user)
    
    return render_to_response("course_list.html",{'course_instance_list':course_instance_list},RequestContext(request))

def index(request):
    #course = Course.objects.create(course_name="MARKETING" , created_by="ravid")
    user = authenticate(username=request.POST.get('Username'), password=request.POST.get('Password'))   
    course_instance_list = Course.objects.filter(students=user)
    
    return render_to_response("login.html",{'course_instance_list':course_instance_list},RequestContext(request))

def personal_index(request):
    #course = Course.objects.create(course_name="MARKETING" , created_by="ravid")
    course_instance_list = Enrollment.objects.get_enrolled_courses(request.user)
    
    return render_to_response("home.html",{'course_instance_list':course_instance_list},RequestContext(request))

def logincheck(request):
    user = authenticate(username=request.POST.get('Username'), password=request.POST.get('Password'))
    course_obj = Course.objects.get(pk=1)
    course_sessions_list = Session.objects.filter(course=course_obj)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            message = "User is valid, active and authenticated"
            login(request,user)
            logged_user = User.objects.get(username=request.POST.get('Username'))
            course_instance_list = Course.objects.filter(students=logged_user)
            return render_to_response("course_list.html",{'course_instance_list':course_instance_list,'logged_user':logged_user},RequestContext(request))
            #return render_to_response("coursedetail.html",{'course':course_obj,'course_sessions_list':course_sessions_list,'userid':request.user},RequestContext(request))
            
        else:
            message =  "The password is valid, but the account has been disabled!"
            return render_to_response("coursedetail.html",{'course':course_obj,'course_sessions_list':[]},RequestContext(request))
    else:
        # the authentication system was unable to verify the username and password
        message =  "The username and password were incorrect."
        return render_to_response("fku.html",{'course':course_obj,'course_sessions_list':[]},RequestContext(request))
    return HttpResponse( message)
    #return render_to_response("coursedetail.html",{'course':course_obj,'course_sessions_list':course_sessions_list},RequestContext(request))
    
def handlelogin(request):
    
    mode = request.POST.get('Mode')
    username = request.POST.get('Username')
   
    
    if mode == "Register" :
        if User.objects.filter(username=username).count():
            user = authenticate(username=username, password=request.POST.get('Password'))
            
            return HttpResponse( "User : " + username + " already exists")
        else :
            User.objects.create_user(username, username,  request.POST.get('Password'))
            newuser = authenticate(username=username, password=request.POST.get('Password'))
            login(request,newuser)
            Course.objects.get(course_name="STRATEGY").students.add(newuser)
            Course.objects.get(course_name="FINANCE").students.add(newuser)
            course_instance_list = Course.objects.filter(students=newuser)
            return render_to_response("course_list.html",{'course_instance_list':course_instance_list,'logged_user':newuser},RequestContext(request))
        
    
    else:    
        user = authenticate(username=request.POST.get('Username'), password=request.POST.get('Password'))
        course_obj = Course.objects.get(pk=1)
        course_sessions_list = Session.objects.filter(course=course_obj)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                message = "User is valid, active and authenticated"
                login(request,user)
                logged_user = User.objects.get(username=request.POST.get('Username'))
                course_instance_list = Course.objects.filter(students=logged_user)
                return render_to_response("course_list.html",{'course_instance_list':course_instance_list,'logged_user':logged_user},RequestContext(request))
                #return render_to_response("coursedetail.html",{'course':course_obj,'course_sessions_list':course_sessions_list,'userid':request.user},RequestContext(request))
                
            else:
                message =  "The password is valid, but the account has been disabled!"
                return render_to_response("coursedetail.html",{'course':course_obj,'course_sessions_list':[]},RequestContext(request))
        else:
            # the authentication system was unable to verify the username and password
            message =  "The username and password were incorrect."
            return render_to_response("fku.html",{'course':course_obj,'course_sessions_list':[]},RequestContext(request))
    
    
    #return HttpResponse( request.POST.get('Mode'))
    #return render_to_response("coursedetail.html",{'course':course_obj,'course_sessions_list':course_sessions_list},RequestContext(request))

def logoutuser(request):
    logout(request)
    return render_to_response("login.html",RequestContext(request))
    
def coursedetail(request,course_id=1):
    course_obj = Course.objects.get(pk=course_id)
    course_sessions_list = Session.objects.filter(course=course_obj)
    return render_to_response("coursedetail.html",{'course':course_obj,'course_sessions_list':course_sessions_list,'userid':request.user})
    #return HttpResponse( course_sessions_list)
    
def personal_course_detail(request,course_id=1):
    course_obj = Course.objects.get(pk=course_id)
    course_sessions_list = Session.objects.filter(course=course_obj)
    return render_to_response("coursedetail.html",{'course':course_obj,'course_sessions_list':course_sessions_list,'userid':request.user})
    #return HttpResponse( course_sessions_list)

def sessiondetail(request,session_id=1):
    session_obj = Session.objects.get(pk=session_id)
    course_obj = session_obj.course
    sessions_notes_list = TakeAway.objects.filter(session=session_obj).filter(user=request.user)
    return render_to_response("takeawaydetail.html",{'course':course_obj,'session':session_obj,'sessions_notes_list':sessions_notes_list},RequestContext(request))

def sessiondetailall(request,session_id=1):
    session_obj = Session.objects.get(pk=session_id)
    course_obj = session_obj.course
    sessions_notes_list = TakeAway.objects.filter(session=session_obj)
    return render_to_response("takeawaydetail.html",{'course':course_obj,'session':session_obj,'sessions_notes_list':sessions_notes_list},RequestContext(request))

def savenotes(request):
    takeaway = request.POST.get('text')
    session_id = request.POST.get('session.id')
    #return HttpResponse( request.user)
    session_obj = Session.objects.get(pk=session_id)
    course_obj = session_obj.course
    takeaway =  TakeAway( course=course_obj,session=session_obj,notes=takeaway,user=request.user)
    takeaway.save()
    sessions_notes_list = TakeAway.objects.filter(session=session_obj).filter(user=request.user)
    return render_to_response("takeawaydetail.html",{'course':course_obj,'session':session_obj,'sessions_notes_list':sessions_notes_list},RequestContext(request))
    
def initload(request):
    User(username="atluri",password="abc123").save()
    User(username="ravi",password="abc123").save()
    
    user1=User.objects.get(username="atluri")
    user2=User.objects.get(username="ravi")
    School(school_name="EMORY").save()
    School(school_name="STANFORD").save()
    School(school_name="COX").save()  
    school1= School.objects.get(school_name="EMORY")
    school1= School.objects.get(school_name="STANFORD")
    school1= School.objects.get(school_name="COX")
    
    Course(school=school1,course_name="STRATEGY",created_by="admin", course_desc="Today's corporate leaders must be able to account for and leverage digital technology and novel operating practices. By studying systems and processes that define the operating and information practices in firms, markets and society, Goizueta students will have the tools to manage as globalization and emerging digital technologies continue to transform the structure, form and governance of these systems and processes.").save()
    Course(school=school1,course_name="FINANCE",created_by="admin", course_desc="Today's corporate leaders must be able to account for and leverage digital technology and novel operating practices. By studying systems and processes that define the operating and information practices in firms, markets and society, Goizueta students will have the tools to manage as globalization and emerging digital technologies continue to transform the structure, form and governance of these systems and processes.").save()
    Course(school=school1,course_name="MARKETING",created_by="admin", course_desc="Today's corporate leaders must be able to account for and leverage digital technology and novel operating practices. By studying systems and processes that define the operating and information practices in firms, markets and society, Goizueta students will have the tools to manage as globalization and emerging digital technologies continue to transform the structure, form and governance of these systems and processes.").save()
    course1 = Course.objects.get(course_name="STRATEGY")
    course2 = Course.objects.get(course_name="FINANCE")
    course3 = Course.objects.get(course_name="MARKETING")
    course1.add(students=[user1,user2])
    Session(course=course1,session_name="Week 1 : Introduction to Strategic Planning",session_dt="2014-06-23").save()
    Session(course=course1,session_name="Week 2 : Dynamics of Strategic Planning",session_dt="2014-06-23").save()
    Session(course=course1,session_name="Week 3 : Mastering Strategic Planning",session_dt="2014-06-23").save()
    Session(course=course2,session_name="Week 1 : Introduction to Finance",session_dt="2014-06-23").save()
    Session(course=course2,session_name="Week 2 : Manage your personal Finances",session_dt="2014-08-23").save()
    Session(course=course3,session_name="Week 1 : Introduction to Marketing",session_dt="2014-09-23").save()
    
    session1 = Session.objects.get(session_name="Week 1 : Introduction to Strategic Planning",course=course1)
    session2 = Session.objects.get(session_name="Week 2 : Dynamics of Strategic Planning",course=course1)
    session3 = Session.objects.get(session_name="Week 3 : Mastering Strategic Planning",course=course1)
    session4 = Session.objects.get(session_dt="2014-06-23",course=course2)
    
    takeaway1 = TakeAway(course=course1,session=session1,user=user1,notes="This is a long long long long long long long long long long long long long long long long long long TAKEAWAY").save()
    takeaway2 = TakeAway(course=course1,session=session2,user=user1,notes="This is a long long long long long long long long long long long long long long long long long long TAKEAWAY").save()
    takeaway3 = TakeAway(course=course1,session=session3,user=user2,notes="This is Ravi's long long long long long long long long long long long long long long long long long long TAKEAWAY").save()
    takeaway4 = TakeAway(course=course2,session=session4,user=user2,notes="This is Ravi's long long long long long long long long long long long long long long long long long long TAKEAWAY").save()
    
    Enrollment(student=user1,course=course1).save()
    Enrollment(student=user1,course=course2).save()
    Enrollment(student=user2,course=course2).save()
    Enrollment(student=user2,course=course3).save()
    return HttpResponse( "Successfully Loaded init data")