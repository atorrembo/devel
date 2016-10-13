from django.conf.urls import include, url
from . import views
from .models import Inmueble
from django.conf import settings
from django.contrib.auth.views import login, logout
#from djgeojson.views import GeoJSONLayerView


urlpatterns = [


#    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Inmueble), name='data'),
    url(r'^inmueble/listado/$', views.inmuebles_list, name='home'),
    url(r'^$', views.home, name='main'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^login$', login, {'template_name': 'inmo/login.html'}, name='login'),
    url(r'^logout$', logout, {'template_name': 'inmo/logout.html'}, name='logout'),
    url(r'^inmueble/(?P<inmueble_id>[0-9]+)/$', views.inmueble_detail, name='inmueble_detail'),
    url(r'^inmueble/alta/$', views.alta_inmueble, name='alta_inmueble'),
#   url(r'^accounts/login/$', login, name="login"),
    ]