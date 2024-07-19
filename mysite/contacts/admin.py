from django.contrib import admin

from contacts.models import Contact, PhoneNumber, Tag, Record

admin.site.register(Contact)
admin.site.register(PhoneNumber)
admin.site.register(Tag)
admin.site.register(Record)
