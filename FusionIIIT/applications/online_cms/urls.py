from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.viewcourses, name='viewcourses'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/$', views.course,
        name='course'),
    # course_name will have blank spaces in between which is not possible
    # to send something in the url so as to identify which course it is.
    # students
    # lecturer
    url(r'^(?P<course_code>[A-z]+[0-9]+)/add_documents$', views.add_document,
        name='add_document'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/add_assignment$',
        views.add_assignment, name='add_assignment'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/upload_assignment$', views.upload_assignment,
        name='upload_assignment'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/add_video$', views.add_videos,
        name='add_videos'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/forum$', views.forum,
        name='forum'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/ajax_reply$', views.ajax_reply,
        name='ajax_reply'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/ajax_new$', views.ajax_new,
        name='ajax_new'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/ajax_remove$', views.ajax_remove,
        name='ajax_remove'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/ajax_assess$', views.ajax_assess,
        name='ajax_assess'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/ajax_feedback$', views.ajax_feedback,
        name='ajax_feedback'),
    # url(r'^(?P<course_code>[A-z]+[0-9]+)/ajax_qbank$', views.ajax_qbank,
    #     name='ajax_qbank'),
    url(r'^quiz/(?P<quiz_id>[0-9]+)/$', views.quiz, name='quiz'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/create_quiz/$', views.create_quiz, name='create_quiz'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/edit_quiz/(?P<quiz_code>[0-9]+)/$',
        views.edit_quiz, name='edit_quiz'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/(?P<quiz_id>[0-9]+)/add_question$', views.add_question_topicwise,
        name='add_question_topicwise'),

#    url(r'^(?P<course_code>[A-z]+[0-9]+)/create_prac_quiz/$', views.create_prac_quiz, name='create_prac_quiz'),
#    url(r'^(?P<course_code>[A-z]+[0-9]+)/edit_prac_quiz/(?P<quiz_code>[0-9]+)/$',
#        views.edit_prac_quiz, name='edit_prac_quiz'),

    url(r'^(?P<course_code>[A-z]+[0-9]+)/edit_quiz_details/(?P<quiz_code>[0-9]+)/$',
        views.edit_quiz_details, name='edit_quiz_details'),
    url(r'^(?P<quiz_code>[0-9]+)/ajax$', views.ajax_q, name='ajax_q'),
    url(r'^(?P<quiz_code>[0-9]+)/submit$', views.submit, name='submit'),

    url(r'^(?P<course_code>[A-z]+[0-9]+)/remove_quiz$', views.remove_quiz,
        name='remove_quiz'),

    url(r'^(?P<course_code>[A-z]+[0-9]+)/remove_bank$', views.remove_bank,
        name='remove_bank'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/create_bank$', views.create_bank,
        name='create_bank'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/(?P<qb_code>[0-9]+)/(?P<topic_id>[0-9]+)$', views.edit_qb_topics,
        name='edit_qb_topics'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/(?P<qb_code>[0-9]+)/(?P<topic_id>[0-9]+)/add_question$', views.add_question,
        name='add_question'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/(?P<qb_code>[0-9]+)/(?P<topic_id>[0-9]+)/remove_question$', views.remove_question,
        name='remove_question'),
    url(r'^(?P<course_code>[A-z]+[0-9]+)/edit_bank/(?P<qb_code>[0-9]+)$', views.edit_bank,name='edit_bank')


]
