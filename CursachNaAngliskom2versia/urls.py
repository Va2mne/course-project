"""
Definition of urls for Курсач2019.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from clown import views
from django.conf.urls import url
from django.conf.urls.static import static
#from django.conf.urls import url, include
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.LoginFormView.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('blogdetails/', views.blogdetails, name='blogdetails'),
    path('actors/', views.actors, name='actors'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    #path('login/',
         #LoginView.as_view
         #(
           #  template_name='app/login.html',
          #   authentication_form=forms.BootstrapAuthenticationForm,
          #   extra_context=
           #  {
            #     'title': 'Log in',
             #    'year' : datetime.now().year,
           #  }
       #  ),
       #  name='login'),
   # path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    url(r'^admin/', admin.site.urls),
    #url(r'^accounts/', include('allauth.urls')),
    #url(r'^', include('post.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
