from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),

    path('request_blood/',views.request_blood,name='request_blood'),
    path('all_request/',views.see_all_request,name='all_request'),
    path('logout/', views.logout_user, name='logout'),
    path('sign_up/', views.sign_up, name ='sign_up'),
    path('user_login/', views.user_login, name ='user_login'),
    path('search/',views.search,name='search'),
    path('status_detail/',views.req_status_details,name='view_detail'),
    

]
