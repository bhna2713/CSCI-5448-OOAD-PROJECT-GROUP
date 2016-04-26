from django.conf.urls import url
from django.contrib import admin

from .import views



from .views import (
appointments,
appointments_add,
appointments_list,
appointments_edit,

appointments_delete,
appointments_detail,
appointments_reset,
appointments_restore,
)
urlpatterns = [
    url(r'^$', appointments ),
    url(r'^add/$', appointments_add),
    # url(r'^list/(?P<id>\d+)/$', appointments_list, name= 'detail'),
    url(r'^(?P<id>\d+)/edit/$', appointments_edit, name= 'edit'),
   	url(r'^list/(?P<id>\d+)$', appointments_list),
    url(r'^delete/(?P<id>\d+)$', appointments_delete ,name= 'delete_appointments'),
    url(r'^detail/$', appointments_detail),
    url(r'^restore/$', appointments_restore),
    url(r'^reset/$', appointments_reset),
]
