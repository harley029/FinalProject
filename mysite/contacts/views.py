from urllib import request
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from contacts.models import Record, Contact, PhoneNumber, Tag

class MainView(ListView):
    model = Record
    template_name = "contacts/index.html"
    context_object_name = "records"

    def get_queryset(self):
        return Record.objects.filter(contact__author=self.request.user)


class RecordDetailView(DetailView):
    model = Contact
    template_name = "contacts/conyact_details.html"
    context_object_name = "contact"
    pk_url_kwargs = "contact_id"


class TagDetailView(View):
    def get(self, tag_name, page=1):
        records = Record.objects.filter(tags__name=tag_name).order_by("id")
        paginator = Paginator(records, 10)
        page_number = request.GET.get("page") or page
        tags_on_page = paginator.get_page(page_number)
        return render(
            request,
            "records/tag_details.html",
            context={"tag": tag_name, "records": tags_on_page},
        )