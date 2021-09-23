from django.urls import path, re_path
from .views import (StatusListSearchAPIView,
                    StatusAPIView,
                    StatusDetailsAPIView
                    )


app_name = 'status_app'

urlpatterns = [
    path(r'', StatusAPIView.as_view(), name='list'),
    path(r'<pk>', StatusListSearchAPIView.as_view(), 'detail_status'),
    path(r'<id>', StatusDetailsAPIView.as_view(), name='sim'),
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