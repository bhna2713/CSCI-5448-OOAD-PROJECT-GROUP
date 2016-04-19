from django.conf.urls import url
from django.contrib import admin

from .import views



from .views import (
address,
address_add,
address_list,
address_edit,

address_delete,
address_detail,

)
urlpatterns = [
    url(r'^$', address ),
    url(r'^add/$', address_add),
    # url(r'^list/(?P<id>\d+)/$', address_list, name= 'detail'),
    url(r'^(?P<id>\d+)/edit/$', address_edit, name= 'edit_address'),
   	url(r'^list/(?P<id>\d+)$', address_list),
    url(r'^delete/(?P<id>\d+)$', address_delete ,name= 'delete_address'),
    url(r'^detail/$', address_detail),
]
