from django.urls import path
from contacts.views import (
    MainView,
    RecordDetailView,
    TagDetailView,
    AddBookView,
    AddTagView,
    AddPhoneView,
    AddContactView,
    AddRecordView,
)

urlpatterns = [
    path("contacts/", MainView.as_view(), name="contacts"),  # Сторінка контактів
    path("contacts/<int:page>/", MainView.as_view(), name="contacts_paginate"),
    path(
        "contact/<str:contact_id>/", RecordDetailView.as_view(), name="contact_detail"
    ),
    path("tag/<str:tag_name>/", TagDetailView.as_view(), name="tag_detail"),
    path(
        "tag/<str:tag_name>/page/<int:page>/",
        TagDetailView.as_view(),
        name="tag_detail_paginate",
    ),
    path("add-book/", AddBookView.as_view(), name="add_book"),
    path("add_tags/", AddTagView.as_view(), name="add_tag"),
    path("add-phone/", AddPhoneView.as_view(), name="add_phone"),
    path("contacts/add/", AddContactView.as_view(), name="add_contact"),
    path("contacts/add_record/", AddRecordView.as_view(), name="add_record"),
]
