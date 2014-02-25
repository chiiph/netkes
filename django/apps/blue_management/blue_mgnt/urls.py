from django.conf.urls import *
from django.conf import settings as django_settings
from django.views.generic import RedirectView

from views import views
from views import groups
from views import users
from views import managementvm
from views import settings

urlpatterns = patterns('',
    (r'^$', users.users, {}, 'index'),
    (r'^saved/$', users.users, {'saved': True}, 'index_saved'),
    (r'^login/$', views.login_user, {}, 'login'),
    (r'^logout/$', views.logout, {}, 'logout'),
    (r'^escrowlogin/(?P<escrow_username>.+)/$', managementvm.escrow_login, {}, 'escrow_login'),
    (r'^users/$', users.users, {}, 'users'),
    (r'^users/saved/$', users.users, {'saved': True}, 'users_saved'),
    (r'^users/saved/(?P<page>\d+)/$', users.users, {'saved': True}, 'users_saved'),
    (r'^users/csv/download/$', views.users_csv_download, {}, 'users_csv_download'),
    (r'^users/csv/$', views.users_csv, {}, 'users_csv'),
    (r'^users/(?P<email>.+)/saved/$', users.user_detail, {'saved': True}, 'user_detail_saved'),
    (r'^users/(?P<email>.+)/$', users.user_detail, {}, 'user_detail'),
    (r'^groups/$', groups.groups, {}, 'groups'),
    (r'^groups/saved/$', groups.groups, {'saved': True}, 'groups_saved'),
    (r'^groups/(?P<group_id>.+)/$', groups.group_detail, {}, 'group_detail'),
    (r'^shares/$', views.shares, {}, 'shares'),
    (r'^shares/saved/$', views.shares, {'saved': True}, 'shares_saved'),
    (r'^shares/(?P<email>.+)/(?P<room_key>.+)/$', views.share_detail, {}, 'share_detail'),
    (r'^manage/$', views.manage, {}, 'manage'),
    (r'^settings/$', settings.settings, {}, 'settings'),
    (r'^settings/saved/$', settings.settings, {'saved': True}, 'settings_saved'),
    (r'^settings/password/$', settings.password, {}, 'password'),
    (r'^settings/password/saved/$', settings.password, {'saved': True}, 'password_saved'),
    (r'^admingroups/$', groups.admin_groups, {}, 'admin_groups'),
    (r'^admingroups/saved/$', groups.admin_groups, {'saved': True}, 'admin_groups_saved'),
    (r'^logs/$', managementvm.logs, {}, 'logs'),
    (r'^logs/download/$', views.download_logs, {}, 'download_logs'),
    (r'^validate/$', views.validate, {}, 'validate'),
    (r'^favicon\.ico$', RedirectView.as_view(url='/static/blue_mgnt/img/favicon.ico')),
    (r'^codes/$', managementvm.auth_codes, {}, 'auth_codes'),
    (r'^codes/saved/$', managementvm.auth_codes, {'saved': True}, 'auth_codes_saved'),
)
