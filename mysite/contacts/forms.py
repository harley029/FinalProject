from django import forms

from contacts.models import Tag, PhoneNumber, Contact, Record


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ["contact", "number"]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["full_name", "address", "email", "birthday"]


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["contact", "note", "tags"]
