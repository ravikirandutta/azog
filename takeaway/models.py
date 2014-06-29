from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=400)
    
    def __unicode__(self):
        return smart_unicode(self.school_name)
    
class Course(models.Model):
     school = models.ForeignKey(School)
     course_name = models.CharField(max_length=400)
     course_desc = models.TextField()
     created_by = models.CharField(max_length=400)
     students = models.ManyToManyField(User)
     created_dt = models.DateTimeField(auto_now_add=True,auto_now=False)
     updated_dt = models.DateTimeField(auto_now_add=False,auto_now=True)
     
     # Maybe try file field and Image field here to associate a pdf/rtf/txt file for each course and maybe an image for each course
     # models.FileField(upload_to='documents/%Y/%m/%d')
     
     def __unicode__(self):
        return smart_unicode(self.course_name)
    
     def get_enrolled_students(self):
        return self.students
     

class Session(models.Model):
    course = models.ForeignKey(Course)
    session_name = models.CharField(max_length=1000)
    session_dt = models.DateField()
    created_dt = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_dt = models.DateTimeField(auto_now_add=False,auto_now=True)
    
    def __unicode__(self):
        return smart_unicode(self.session_name)
    
    
#class EnrollmentManager(models.Manager):
#    
#    def get_enrolled_students(course_obj):
#        return self.filter(course=course_obj)
#    
#    def get_enrolled_courses(user):
#        return self.filter(student=user)
   
class Enrollment(models.Model):
    student = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    #objects = EnrollmentManager()
    
    #def __unicode__(self):
    #    return smart_unicode(self.student + self.course) 
    
    

class TakeAway(models.Model):
    course = models.ForeignKey(Course) 
    session = models.ForeignKey(Session)
    notes = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_dt = models.DateTimeField(auto_now_add=False,auto_now=True)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return smart_unicode(self.notes[:400])

