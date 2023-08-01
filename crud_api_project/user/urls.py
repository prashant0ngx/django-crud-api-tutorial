from django.urls import path
from . import views


urlpatterns = [

    path('login/', views.login , name='login'),
    path('register/', views.register , name='register'),
    path('user/', views.get_all_users , name='user-detail-list'),
    path('user/create/', views.create_user, name='user-create'),
    path('user/<int:pk>/', views.get_user_by_id, name='user-detail-by-id'),
    path('user/update/<int:pk>/', views.update_user_by_id, name='user-update-by-id'),
    path('user/delete/<int:pk>/', views.delete_user_by_id, name='user-delete-by-id'),
  
    
    # path('user/', UserList.as_view() , name='user-list'),
    # path('login/', LoginView.as_view() , name='login'),
    # path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),

]