from django.conf.urls import url
from django.contrib import admin

from .import views



from .views import (
reminders,
reminders_add,
reminders_list,
reminders_edit,

reminders_delete,
reminders_detail,
reminders_none,

)
urlpatterns = [
    url(r'^$', reminders ),
    url(r'^add/$', reminders_add),
    # url(r'^list/(?P<id>\d+)/$', reminders_list, name= 'detail'),
    url(r'^(?P<id>\d+)/edit/$', reminders_edit, name= 'edit_reminder'),
   	url(r'^list/(?P<id>\d+)$', reminders_list),
    url(r'^delete/(?P<id>\d+)$', reminders_delete ,name= 'delete_reminder'),
    url(r'^detail/$', reminders_detail),
    url(r'^none/$', reminders_none, name = 'reminders_none'),

]
