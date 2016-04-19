from django.conf.urls import url
from django.contrib import admin

from .import views



from .views import (
notes,
notes_add,
notes_list,
notes_edit,

notes_delete,
notes_detail,
notes_filter_note,
notes_filter_title,


)
urlpatterns = [
    url(r'^$', notes ),
    url(r'^add/$', notes_add),
    # url(r'^list/(?P<id>\d+)/$', notes_list, name= 'detail'),
    url(r'^(?P<id>\d+)/edit/$', notes_edit, name= 'edit_note'),
   	url(r'^list/(?P<id>\d+)$', notes_list),
    url(r'^delete/(?P<id>\d+)$', notes_delete ,name= 'delete_note'),
    url(r'^detail/$', notes_detail),
    url(r'^notesnote/$', notes_filter_note),
    url(r'^notestitle/$', notes_filter_title),



]
