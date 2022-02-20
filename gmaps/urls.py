from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView

urlpatterns = [
    path('', views.home,name="home"),
    path('adminLogin/', views.uloginpage,name="adminLogin"),
    path('loginForUserandDriver/', views.loginUserandDriver,name="loginForUserandDriver"),
    path('ulogout/', views.ulogout,name="ulogout"),
    
    

    # path('userlogin/', views.uloginpage,name="userlogin"),
    path('userregistration/', views.uregistrationpage,name="userregistration"),
    
    path('drv/', views.drv, name="drv"),
    path('homeFromAdmin/',views.homeFromAdmin,name="homeFromAdmin"),
    path('password/',PasswordsChangeView.as_view(template_name="gmaps/change-password.html"),name="change_password"),
    path('password_success/',views.password_success,name="password_success"),
    path('loginwithphone/',views.loginwithphone,name="loginwithphone"),
    path('loginwithotp/',views.loginwithotp,name="loginwithotp"),
    path('enterotp/',views.enterotp,name="enterotp"),
    path('password2/',PasswordsChangeView.as_view(template_name="gmaps/changePasswordForDriver.html"),name="changePasswordForDriver"),
    
   
    
    
    
    path('addroutes/',views.Addroutes,name="addroutes"),
    path('routes/',views.routes,name="routes"),
    path('routeDetailsAdd/',views.routeDetailsAdd,name="routeDetailsAdd"),
    path('viewRoutes/',views.viewRoutes,name="viewRoutes"),
    path('show/',views.show,name="show"),

    path('driverDetails/', views.driverDetails, name="driverDetails"),
    path('registerUser/', views.registerUser, name="registerUser"),
    path('userHomePage/',views.userHomePage,name="userHomePage"),
    path('findMyBus/',views.findMyBus,name="findMyBus"),
    path('searchMyBus/',views.searchMyBus,name="searchMyBus"),
    path('post_create/',views.post_create,name="post_create"),
   
    path(r'^getDetailsFromDB/(?P<busNo>\d{1,2})/(?P<dest>\d{10,20})$',views.getDetailsFromDB , name="getDetailsFromDB"),
    
    

    path('adddriverdetails/',views.driverdetails,name="adddriverdetails"),
    
    path('find/',views.find,name="find"),
    path('search/',views.find,name="search"),

    # path('showroutes/',views.showroutes,name="showroutes"),
    # path('showbuses/',views.showbus,name="showbuses"),
    # # path('rj_the_pruast/', views.rj_the_pruast, name="rj_the_pruast"),
     path('reset_password2/',
     auth_views.PasswordResetView.as_view(template_name="gmaps/password_reset2.html"),
     name="reset_password2"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="gmaps/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="gmaps/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="gmaps/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="gmaps/password_reset_done.html"), 
        name="password_reset_complete"),
    path("update_session/", views.update_session),
    path('update_marker/',views.update_marker),

    path('profile/', views.profile,name="profile"), 
    path('viewProfile',views.viewProfile,name= "viewProfile"),
    path('viewProfileDriver',views.viewProfileDriver,name= "viewProfileDriver"),
    path('eveningMap/',views.eveningMap,name="eveningMap"),
    path('redirect_to_map/',views.redirect_to_map),
    path('mapSec/',views.mapSec,name="mapSec"),
    path('usercomplaint', views.usercomplaint, name="usercomplaint"),
    path('admincomplaint', views.admincomplaint, name="admincomplaint"),
    path('delete_complaint/<str:pk>/', views.delete_complaint, name="delete_complaint"),
    path('index', views.index, name="index"),
    path('index2', views.index2, name="index2"),
    path('shownotice', views.shownotice, name="shownotice"),
    

]