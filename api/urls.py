from django.urls import include, path

urlpatterns = [
    path('users/', include('users.urls')),
    path('tasks/', include('task.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]
