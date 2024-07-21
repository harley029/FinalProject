from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.views.generic import DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
# from django.views.decorators.http import require_POST

from contacts.models import Record, Contact, PhoneNumber, Tag
from contacts.forms import TagForm, PhoneNumberForm, ContactForm, RecordForm


@method_decorator(login_required, name="dispatch")
class MainView(ListView):
    model = Record
    template_name = "contacts/index.html"
    context_object_name = "records"

    def get_queryset(self):
        return Record.objects.filter(contact__author=self.request.user).order_by("contact__full_name")


@method_decorator(login_required, name="dispatch")
class RecordDetailView(DetailView):
    model = Contact
    template_name = "contacts/contact_details.html"
    context_object_name = "contact"
    pk_url_kwarg = "contact_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["phone_numbers"] = PhoneNumber.objects.filter(contact=self.object)
        # Отримуємо першу нотатку або None, якщо записів немає
        record = Record.objects.filter(contact=self.object).first()
        context["note"] = record.note if record else "No notes available"
        return context


@method_decorator(login_required, name="dispatch")
class TagDetailView(View):
    def get(self, request, tag_name, page=1):
        records = Record.objects.filter(tags__name=tag_name).order_by('contact__full_name')
        paginator = Paginator(records, 10)
        page_number = request.GET.get("page", page)
        records_on_page = paginator.get_page(page_number)
        return render(
            request,
            "contacts/tag_details.html",
            context={"tag": tag_name, "contacts": records_on_page},
        )


@method_decorator(login_required, name="dispatch")
class AddBookView(TemplateView):
    template_name = "contacts/add_book.html"


@method_decorator(login_required, name="dispatch")
class AddTagView(TemplateView):
    template_name = "contacts/add_tag.html"

    def get(self, request, *args, **kwargs):
        form = TagForm()  # припустимо, що у вас є форма для додавання тегу
        return self.render_to_response({"form": form})

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect("add_book")
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_tag")  # перенаправлення після успішного збереження
        return self.render_to_response({"form": form})


@method_decorator(login_required, name="dispatch")
class AddPhoneView(TemplateView):
    template_name = "contacts/add_phone.html"

    def get(self, request, *args, **kwargs):
        form = (
            PhoneNumberForm()
        )  # припустимо, що у вас є форма для додавання номера телефону
        return self.render_to_response({"form": form})

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect("add_book")
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_phone")  # перенаправлення після успішного збереження
        return self.render_to_response({"form": form})


@method_decorator(login_required, name="dispatch")
class AddContactView(TemplateView):
    template_name = "contacts/add_contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()  # Використовуйте форму
        return self.render_to_response({"form": form})

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect("add_book")
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = (
                request.user
            )  # Призначення поточного користувача автором контакту
            contact.save()
            return redirect("add_contact")  # Перенаправлення після успішного збереження
        return self.render_to_response({"form": form})


@method_decorator(login_required, name="dispatch")
class AddRecordView(TemplateView):
    template_name = "contacts/add_record.html"

    def get(self, request, *args, **kwargs):
        form = RecordForm()  # Створіть форму для GET запиту
        return self.render_to_response({"form": form})

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect("add_book")
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.author = (
                request.user
            )  # Призначити поточного користувача, якщо потрібно
            record.save()
            return redirect("add_record")  # Перенаправлення після успішного збереження
        return self.render_to_response({"form": form})


@method_decorator(login_required, name="dispatch")
class SearchView(TemplateView):
    template_name = "contacts/search_main.html"


@method_decorator(login_required, name="dispatch")
class DeleteView(TemplateView):
    template_name = "contacts/delete/delete_main.html"


@method_decorator(login_required, name="dispatch")
class PhoneDeleteListView(View):
    def get(self, request):
        phone_numbers = PhoneNumber.objects.all()
        return render(
            request, "contacts/delete/delete_phone_list.html", {"phone_numbers": phone_numbers}
        )


@method_decorator(login_required, name="dispatch")
class PhoneDeleteConfirmView(View):
    def get(self, request, pk):
        phone_number = get_object_or_404(PhoneNumber, pk=pk)
        return render(
            request, "contacts/delete/confirm_delete_phone.html", {"object": phone_number}
        )

    def post(self, request, pk):
        phone_number = get_object_or_404(PhoneNumber, pk=pk)
        phone_number.delete()
        return redirect("phone_number_delete_list")


@method_decorator(login_required, name="dispatch")
class TagDeleteListView(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, "contacts/delete/delete_tag_list.html", {"tags": tags})


@method_decorator(login_required, name="dispatch")
class TagDeleteConfirmView(View):
    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        return render(
            request, "contacts/delete/confirm_delete_tag.html", {"object": tag}
        )

    def post(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        tag.delete()
        return redirect("tag_delete_list")


@method_decorator(login_required, name="dispatch")
class NoteDeleteListView(View):
    def get(self, request):
        notes = Record.objects.filter(
            note__isnull=False
        ).distinct()  # Отримати всі записи з нотатками
        return render(
            request, "contacts/delete/delete_note_list.html", {"notes": notes}
        )


@method_decorator(login_required, name="dispatch")
class NoteDeleteConfirmView(View):
    def get(self, request, pk):
        note_record = get_object_or_404(Record, pk=pk)
        return render(
            request, "contacts/delete/confirm_delete_note.html", {"object": note_record}
        )

    def post(self, request, pk):
        note_record = get_object_or_404(Record, pk=pk)
        note_record.note = None  # Видалити нотатку
        note_record.save()
        return redirect("note_delete_list")


# @login_required
# @require_POST
# def delete_phone_number(request, pk):
#     phone_number = get_object_or_404(PhoneNumber, pk=pk)
#     if request.method == "POST":
#         phone_number.delete()
#         return redirect(reverse_lazy("phone_number_delete_list"))
#     return render(
#         request, "contacts/confirm_delete_phone.html", {"object": phone_number}
#     )
