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
    template_name = "contacts/contact_details.html"
    context_object_name = "contact"
    pk_url_kwarg = "contact_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["phone_numbers"] = PhoneNumber.objects.filter(contact=self.object)
        context["note"] = Record.objects.filter(contact=self.object).first().note
        return context


class TagDetailView(View):
    def get(self, request, tag_name, page=1):
        records = Record.objects.filter(tags__name=tag_name).order_by("id")
        paginator = Paginator(records, 10)
        page_number = request.GET.get("page", page)
        records_on_page = paginator.get_page(page_number)
        return render(
            request,
            "contacts/tag_details.html",
            context={"tag": tag_name, "contacts": records_on_page},
        )
