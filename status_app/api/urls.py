from django.urls import path
from .views import (StatusListSearchAPIView,
                    StatusAPIView,
                    StatusCreateAPIView,
                    StatusDetailsAPIView,
                    StatusUpdateAPIView,
                    StatusDeleteAPIView
                    )

urlpatterns = [
    path(r'', StatusListSearchAPIView.as_view()),
    path(r'status', StatusAPIView.as_view()),
    path(r'create', StatusCreateAPIView.as_view()),
    path(r'<id>/update/', StatusUpdateAPIView.as_view()),
    path(r'<id>', StatusDetailsAPIView.as_view()),
    path(r'<id>/delete/', StatusDeleteAPIView.as_view()),
]

"""
Start with
/api/status/ --> list
/api/status/create/ --> Create
/api/status/1/  --> Details
/api/status/1/update --> Update
/api/status/1/delete --> Delete


End with
/api/status/ --> List CRUD
/api/status/1/ --> Detail CRUD

final

/api/status/ --> CRUD & List
"""