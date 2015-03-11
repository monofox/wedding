#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.conf.urls import patterns, url
from core import mail
from core.models import ContactMail
from django.contrib import messages
from django.utils.translation import ugettext as _

class ContactMailAdmin(admin.ModelAdmin):
    list_display = ('name', 'sendersubject', 'sender', 'contact_date')

admin.site.register(ContactMail, ContactMailAdmin)
