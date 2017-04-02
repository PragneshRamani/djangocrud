from django.conf.urls import url
from .import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import include


urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),

    url(r'^(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()), name='detail'),

    url(r'^add/$', login_required(views.InfoCreate.as_view()), name='add-info'),

    url(r'^(?P<pk>[0-9]+)/update$', login_required(views.InfoUpdate.as_view()), name='update-info'),

    url(r'^(?P<pk>[0-9]+)/delete$', login_required(views.InfoDelete.as_view()), name='delete-info'),

    url(r'^logout/$', views.user_logout, name="logout"),

    url(r'^register/$',login_required(views.register),name="register"),

    url(r'^api/get$',login_required(views.InformationList.as_view()),name="api"),

    url(r'^api/detail/(?P<pk>[0-9]+)$',login_required(views.InfoDetailView.as_view()),name="detailapi"),

    url(r'^filterlist/$',login_required(views.InfoFilterList.as_view()),name="filterlist"),

    url(r'^filter/$',login_required(views.FilterField.as_view()),name="filter"),

    url(r'^search/$',login_required(views.InfoSearchView.as_view()),name="search"),

    url(r'^order/$', login_required(views.InformationOrder.as_view()), name="order"),

    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),




]