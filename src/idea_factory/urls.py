from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path(
        '',
        include('pages.urls', namespace='pages')
    ),
    path(
        'accounts/',
        include('accounts.urls', namespace='accounts')
    ),
    path(
        'idea/posts/',
        include('posts.urls', namespace='posts')
    ),
    path(
        'idea/posts/',
        include('likes.urls', namespace='likes')
    ),
    path(
        'idea/posts/',
        include('unlikes.urls', namespace='unlikes')
    ),
    path(
        'idea/posts/',
        include('comments.urls', namespace='comments')
    ),
    path(
        'idea/profiles/',
        include('profiles.urls', namespace='profiles')
    ),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
