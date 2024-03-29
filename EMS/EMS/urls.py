
from django.contrib import admin
from django.urls import path
from users import views
from management import views as mviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_user/',views.newuser.as_view(),name="newuser"),
    path('gettoken/',views.gettoken.as_view(),name="gettoken"),
    path('user_login/',views.user_login.as_view(),name="user_login"),
    #path('refreshtoken/',views.refreshtoken.as_view()),
    path('company_register/',views.company_register.as_view()),
    path('user_register/',views.user_register.as_view()),
    path('user_register/<int:id>/',views.user_register.as_view()),
    path('company_profile/',views.company_pofile.as_view(),name="company_profile"),
    path('employer_register/<int:pk>/',views.employer_register.as_view()),
    path('employer_register/',views.employer_register.as_view()),
    path('employer_id/',views.employer_id.as_view()),
    path('employer_profile/',views.employer_profiles.as_view(),name="employer_profile"),
    path('employer_profile/<int:pk>/',views.employer_profiles.as_view(),name="employer_profile_id"),
    path('projects/<int:pk>/',mviews.projects.as_view(),name='projects_id'),
    path('projects/',mviews.projects.as_view(),name='projects'),
    path('leaves/',mviews.leaves.as_view(),name='manage_leaves'),
    path('leaves/<int:pk>/',mviews.leaves.as_view(),name='manage_leaves_id'),
    path('leave_detail/',mviews.leave_detail.as_view(),name="apply_leave"),
    path('salary/<int:pk>/',mviews.salarys.as_view(),name='salary_empid'),
    path('search/<str:name>/',views.search.as_view(),name="search_employer"),
    path('salary/',mviews.salarys.as_view(),name="salary"),
    path('salary_detail/',mviews.salary_detail.as_view(),name="employer_salary"),
    path('departments/',mviews.all_departments.as_view()),
    path('add_department/',mviews.add_department.as_view(),name='add_department'),
    path('add_department/<int:pk>/',mviews.add_department.as_view(),name='add_department_id'),
    path('attendance/',mviews.attendance.as_view(),name="attendance"),
    path('attendance/<int:pk>/',mviews.attendance.as_view(),name="attendance_id"),
    path('my_attendance/',mviews.my_attendance.as_view(),name="my_attendance"),
    path('dashboard/',views.dashboard.as_view(),name='company_dashboard'),
    path('E_dashboard/',views.E_dashboard.as_view(),name='employer_dashboard'),
    path('forget_password/',views.forget_password.as_view(),name='forget_password'),
    path('E_forget_password/',views.E_forget_password.as_view(),name='E_forget_password'),
    path('otp/',views.otp.as_view(),name='otp_verification'),
    path('E_otp/',views.E_otp.as_view(),name='E_otp_verification'),

    path('phases/',mviews.phaseView.as_view(),name='phase'),
    path('phases/<int:id>/',mviews.phaseView.as_view(),name='phase_id'),
    path('questions/',mviews.questionsView.as_view(),name='question'),
    path('questions/<int:id>/',mviews.questionsView.as_view(),name='question_id'),
    path('review/',mviews.reviewView.as_view(),name='review'),
    path('review/<int:id>/',mviews.reviewView.as_view(),name='review_id'),
    path('get_review/<str:year>/<int:month>/<str:week>/<int:id>/',mviews.checkview.as_view()),
    path('get_review/<str:year>/<int:month>/<int:id>/',mviews.checkview.as_view()),
    path('get_review/<int:id>/',mviews.checkview.as_view()),
    path('choices/',mviews.choiceview.as_view()),
    path('choices/<int:id>/',mviews.choiceview.as_view()),
    path('logout/',views.logout.as_view()),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
