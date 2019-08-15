from django.urls import path

from . import views

app_name = 'ratings'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.BusinessListView.as_view(), name='list'),
    # path('<str:id>/', views.DetailView.as_view(), name='detail'),
    path('<str:id>/', views.business_detail_view, name='detail'),
    path('about/', views.about, name='about'),
    # path('report/', views.report, name='report'),
    path('report/', views.ReportView.as_view(), name='report'),
    path('popular/', views.PopularView.as_view(), name='popular'),

]
