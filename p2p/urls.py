from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'accounting.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.p2p_accounting, name='p2p_accounting'),

]
