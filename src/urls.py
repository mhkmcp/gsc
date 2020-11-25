from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),

    path('intro', introduction, name='intro'),
    path('purpose', introduction, name='purpose'),
    path('president-speech', president_speech, name='president_speech'),
    path('courtesy-speech', courtesy_speech, name='courtesy_speech'),

    path('adviser', adviser, name='adviser'),
    path('management', adviser, name='management'),
    path('general', general, name='general'),
    path('election', election, name='election'),

    path('requirements', requirements, name='requirements'),
    path('how-to-be-member', how_to_be_member, name='how_to_be_member'),
    path('admission-form', admission_form, name='admission_form'),
    path('member-list', member_list, name='member_list'),
    path('general-member', general_member, name='general_member'),
    path('lifetime-member', lifetime_member, name='lifetime_member'),
    path('honorary-member', honorary_member, name='honorary_member'),
    path('member-info', member_info, name='member_info'),
    path('member-share', member_share, name='member_share'),
    path('collection-info', collection_info, name='collection_info'),
    path('audit-report', audit_report, name='audit_report'),
    path('blood-group-dob', blood_group_dob, name='blood_group_dob'),

    path('financial', financial, name='financial'),
    path('other-way', other_way, name='other_way'),

    path('scholarship', scholarship, name='scholarship'),
    path('treatment', treatment, name='treatment'),
    path('training', training, name='training'),

]
