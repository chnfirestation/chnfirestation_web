from django.urls import path
from . import views
from django.views.decorators.cache import never_cache



urlpatterns = [
    path('', views.home, name='index'),
    path('index/',views.home, name='index'),      # home page
    path('about/', views.about, name='about'),   # about page
    path('logout/', views.logout, name='logout'), # logout
    path('contact/', views.contact, name='contact'), # contact page
    path('user_login/', views.user_login, name='user_login'),    # login page
    path('admin_login/', views.admin_login, name='admin_login'),  # admin login page
    path('userdashboard/', views.userdashboard, name='userdashboard'), # user dashboard
    path('case-detail/<str:model_type>/<int:case_id>/', views.case_detail, name='case_detail'), # case detail page
    path('reportcase/', views.reportcase, name='reportcase'), # report case page
    path('fireform/', views.fireform, name='fireform'), # fire forms page
    path('waterform/', views.waterform, name='waterform'), # water forms page
    path('generalincidentform/', views.generalincidentform, name='generalincidentform'), # general incident forms page
    path('assistcalls/', views.assistcalls, name='assistcalls'), # assistance calls form page
    path('firewater_report/', views.firewater_report, name='firewater_report'), # fire and water report submission
    path('generalincident_report/', views.generalincident_report, name='generalincident_report'), # general incident report submission
    path('assistancecall_report/', views.assistancecall_report, name='assistancecall_report'), # assistance call report submission
    path('admindashboard/', views.admindashboard, name='admindashboard'), # admin dashboard
    path('admincase-detail/<str:model_type>/<int:case_id>/', views.admincase_detail, name='admincase_detail'), # case detail page
    path('adminreportcase/', views.adminreportcase, name='adminreportcase'), # admin report case page
    path('adminfireform/', views.adminfireform, name='adminfireform'), # admin fire forms page
    path('adminfirewater_report/', views.adminfirewater_report, name='adminfirewater_report'), # admin fire and water report submission
    path('admingeneralincidentform/', views.admingeneralincidentform, name='admingeneralincidentform'), # admin general incident forms page
    path('admingeneralincident_report/', views.admingeneralincident_report, name='admingeneralincident_report'), # admin general incident report submission
    path('adminassistcalls/', views.adminassistcalls, name='adminassistcalls'), # admin assistance calls form page
    path('adminassistancecall_report/', views.adminassistancecall_report, name='adminassistancecall_report'), # admin assistance call report submission
    path('adminwaterform/', views.adminwaterform, name='adminwaterform'), # admin water forms page
    path('adminviewreport/', views.adminviewreport, name='adminviewreport'), # admin view reports page 
    path('edit-case/<str:model_type>/<int:case_id>/', views.edit_case, name='edit_case'),
    path('delete-case/<str:model_type>/<int:case_id>/', views.delete_case, name='delete_case'),
    path('download-reports/', views.download_reports, name='download_reports'), # admin download reports as CSV 
    path('allcase-detail/<str:model_type>/<int:case_id>/', views.allcase_detail, name='allcase_detail'),
    path('adminanalytics/', views.adminanalytics, name='adminanalytics'), # admin analytics page
    path('adminanalytics/download-csv/', views.download_analytics_csv, name='download_analytics_csv'), # admin download analytics data as CSV
    path('adminadduser/', views.adminadduser, name='adminadduser'), # admin add user page
    path('deleteuser/<int:user_id>/', views.deleteuser, name="deleteuser"),
    path('deleteadmin/<int:admin_id>/', views.deleteadmin, name="deleteadmin"),
]
