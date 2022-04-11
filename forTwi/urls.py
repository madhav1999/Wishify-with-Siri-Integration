from django.urls import path

from . import views

urlpatterns = [
    #path('allTabs', views.list),
    #path('allTabs', views.forYouList.as_view()),
    path('allTabs', views.forTwiList.as_view(), name="allTabsT.list"),
    path('allTabs/<int:pk>', views.forTwiDetailView.as_view(), name="forTwi.data"),
    path('allTabs/new', views.forTwiCreateView.as_view(), name="forTwi.new"),
    path('allTabs/<int:pk>/edit', views.forTwiUpdateView.as_view(), name="forTwi.update"),
    path('allTabs/<int:pk>/delete', views.forTwiDeleteView.as_view(), name="forTwi.delete"),

]