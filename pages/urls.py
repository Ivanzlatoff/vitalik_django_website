from django.urls import path

from .views import HomePageView, My_WorkView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('my-work/', My_WorkView.as_view(), name='my-work'),
]