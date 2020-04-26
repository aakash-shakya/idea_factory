from django.urls import path
from .views import IndexView, DashboardView, AboutView,PostDetailView

app_name = 'pages'
urlpatterns = [
    path(
        '',
        IndexView.as_view(),
        name='home-view'
    ),
    path(
        'dashboard/',
        DashboardView.as_view(),
        name='dashboard-view'
    ),
    path(
        'about/',
        AboutView.as_view(),
        name='about-view'
    ),
    path(
        '<slug:slug>/',
        PostDetailView.as_view(),
        name='post-details'

    )
]
