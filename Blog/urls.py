from django.urls import path

from.import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.loginfun,name='login'),
    path('index',views.index,name='index'),
    path('blog',views.blogfun,name='blog'),
    path('post/<int:id>',views.post,name='post'),
    path('search>',views.search,name='search'),
    path('signup',views.signup,name='signup'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    






