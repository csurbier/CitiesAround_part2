from django.conf.urls import url
from . import views

urlpatterns = [
       url(r'^cities/$',
           views.CitiesListView.as_view(),
           name='cities'),
       url(r'^cities/(?P<pk>\d+)/$',
           views.CitiesDetailView.as_view(),
           name='city'),
       url(r'^users/$',
           views.AppUserListView.as_view(),
           name='users'),
       url(r'^user/(?P<pk>\d+)/$',
           views.AppUserDetailView.as_view(),
           name='user'),
       url(r'^favorites/$',
           views.FavoritesListView.as_view(),
           name='favorites'),
       url(r'^favori/(?P<pk>\d+)/$',
           views.FavoritesDetailView.as_view(),
           name='favori'),
]