from django.urls import path
from contacts.views import MainView, RecordDetailView, TagDetailView

urlpatterns = [
    path("", MainView.as_view(), name="root"),
    path("<int:page>/", MainView.as_view(), name="root_paginate"),
    path("contact/<str:contact_id>/", RecordDetailView.as_view(), name="contact_detail"),
    path("tag/<str:tag_name>/", TagDetailView.as_view(), name="tag_detail"),
    path("tag/<str:tag_name>/page/<int:page>/", TagDetailView.as_view(), name="tag_detail_paginate"),
]
