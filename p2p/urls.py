from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'accounting.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^p2p_accounting/', views.p2p_accounting, name='p2p_accounting'),
    url(r'^invoice_price_variance_accounting/', views.ipv_accounting, name='ipv_accounting'),

]
