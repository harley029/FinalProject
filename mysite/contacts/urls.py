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
    SearchView,
    DeleteView,
    PhoneDeleteListView,
    PhoneDeleteConfirmView,
    TagDeleteListView,
    TagDeleteConfirmView,
    NoteDeleteListView,
    NoteDeleteConfirmView,
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
    path("delete_book/", DeleteView.as_view(), name="delete_book"),
    path("search/", SearchView.as_view(), name="main_search"),
    path("phones/delete/", PhoneDeleteListView.as_view(), name="phone_number_delete_list"),
    path("phone/<int:pk>/delete/", PhoneDeleteConfirmView.as_view(), name="phone_delete_confirm"),
    path("tags/delete/", TagDeleteListView.as_view(), name="tag_delete_list"),
    path("tag/<int:pk>/delete/", TagDeleteConfirmView.as_view(), name="tag_delete_confirm"),
    path("notes/delete/", NoteDeleteListView.as_view(), name="note_delete_list"),  # новий маршрут
    path("note/<int:pk>/delete/", NoteDeleteConfirmView.as_view(), name="note_delete_confirm"),  # новий маршрут
]
