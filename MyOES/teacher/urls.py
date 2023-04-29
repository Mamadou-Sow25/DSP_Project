from django.urls import path
from teacher import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('teacherclick', views.teacherclick_view),
path('teacherlogin', LoginView.as_view(template_name='teacher/teacherlogin.html'),name='teacherlogin'),
path('teachersignup', views.teacher_signup_view,name='teachersignup'),
path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
path('teacher-exam', views.teacher_exam_view,name='teacher-exam'),
path('teacher-add-exam', views.teacher_add_exam_view,name='teacher-add-exam'),
path('teacher-view-exam', views.teacher_view_exam_view,name='teacher-view-exam'),
path('delete-exam/<int:pk>', views.delete_exam_view,name='delete-exam'),
path('update-exam/<int:exam_id>', views.teacher_update_exam_view,name='update-exam'),
path('profile_user', views.profile_teacher,name='profile_teacher'),
path('teacher-question', views.teacher_question_view,name='teacher-question'),
path('teacher-add-question', views.teacher_add_question_view,name='teacher-add-question'),
path('teacher-update-question/<int:question_id>', views.teacher_update_question_view,name='update-question'),
path('teacher-view-question', views.teacher_view_question_view,name='teacher-view-question'),
path('see-question/<int:pk>', views.see_question_view,name='see-question'),
path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),

path('teacher_student_view/', views.teacher_student_view,name='teacher_student_view'),
path('teacher_view_student_view/', views.teacher_view_student_view,name='teacher_view_student_view'),
path('delete_student_view/<int:pk>', views.delete_student_view,name='delete_student_view'),
path('teacher_view_student_marks_view/', views.teacher_view_student_marks_view,name='view_marks'),

]