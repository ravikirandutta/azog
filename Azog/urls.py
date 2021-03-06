from django.conf.urls import patterns, include, url
import notifications
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Azog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'takeaway.views.index', name='home'),
    url(r'^login/$', 'takeaway.views.handlelogin', name='handlelogin'),
    url(r'^logout/$', 'takeaway.views.logoutuser', name='logoutuser'),
    url(r'^takeaway/auth/', 'takeaway.views.logincheck', name='login'),
    url('^inbox/notifications/', include(notifications.urls)),
    url(r'^takeaway/$', 'takeaway.views.home', name='takeawayhome'),
      # ex: /takeaway/course/course_id
    url(r'^takeaway/*/$', 'takeaway.views.coursedetail', name='course_detail'),
    url(r'^takeaway/course/(?P<course_id>[0-9]+)/$', 'takeaway.views.coursedetail', name='course_detail'),
    url(r'^takeaway/session/(?P<session_id>[0-9]+)/$', 'takeaway.views.sessiondetail', name='session_detail'),
    url(r'^takeaway/session/(?P<session_id>[0-9]+)all/$', 'takeaway.views.sessiondetailall', name='session_detailall'),

    url(r'^takeaway/course/(?P<course_id>[0-9]+)/personal/$', 'takeaway.views.personal_course_detail', name='personal_course_detail'),
    url(r'^takeaway/course/(?P<course_id>[0-9]+)/public/$', 'takeaway.views.public_course_detail', name='public_course_detail'),

    url(r'^takeaway/notes/save/', 'takeaway.views.savenotes', name='save_notes'),
    url(r'^takeaway/notes/makepublic/$', 'takeaway.views.make_public', name='make_public'),
    url(r'^takeaway/notes/vote/$', 'takeaway.views.vote', name='vote'),

    url(r'^takeaway/notes/tags/$', 'takeaway.views.tags', name='tags'),

    url(r'^takeaway/notes/edit/$', 'takeaway.views.notes_edit', name='notes_edit'),
    url(r'^takeaway/notes/delete/$', 'takeaway.views.notes_delete', name='notes_delete'),

    url(r'^takeaway/notifications/delete/', 'takeaway.views.mark_as_read', name='notifications_delete'),

    url(r'^takeaway/initload', 'takeaway.views.initload', name='initload'),
)
