from django.urls import path

from . import views



urlpatterns = [
    #path('allTabs', views.list),
    path('allTabs', views.forYouList.as_view(), name="allTabsY.list"),
    path('allTabs/<int:pk>', views.forYouDetailView.as_view(), name="forYou.data"),
    #path('allTabs', views.forTwiList.as_view()),
    path('allTabs/new', views.forYouCreateView.as_view(), name="forYou.new"),
    path('allTabs/<int:pk>/edit', views.forYouUpdateView.as_view(), name="forYou.update"),
    path('allTabs/<int:pk>/delete', views.forYouDeleteView.as_view(), name="forYou.delete"),
    


]