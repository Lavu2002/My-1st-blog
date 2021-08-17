from django.urls import path,include
from home import views
from django.views.generic import TemplateView
from django.views.generic import RedirectView
# from home.views import AboutView
app_name='home'
urlpatterns=[
    path("",views.home,name='home'),
    # path("about/",views.about,name='about'),
    path("about/",TemplateView.as_view(template_name='home/about.html'),name='about'),
    # path("about/",AboutView.as_view(),name='about'),
    # path("",RedirectView.as_view(url='https://www.amazon.in')),
    path("login/",views.login,name='login'),
    path("contact/",views.contact,name='contact'),
    path("help/",views.help,name='help'),
    path("search/",views.search,name='search'),
    
]