
from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import AuthorListView, AuthorDetailView, BookListView, BookDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biblio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^autorzy/$', AuthorListView.as_view(), name='author-list'),
    url(r'^autorzy/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^ksiazki/$', BookListView.as_view(), name='book-list'),
    url(r'^ksiazki/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book-detail'),

)