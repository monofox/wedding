#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.template import RequestContext
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from django.conf.urls import patterns, url
from django.contrib import messages
from django.utils.html import escape
from django.utils.translation import ugettext as _
from django.contrib.admin import widgets, helpers
from django.contrib.admin.utils import quote, unquote
from wishes.models import WishPriority, Wish
from wishes.forms import WishForm

class WishAdmin(admin.ModelAdmin):
    list_display = ('priority', 'visible', 'dttiord', 'wishtxt')
    #list_display_links = None

    def add_view(self, request, form_url='', extra_context=None):
        if not self.has_add_permission(request):
                raise PermissionDenied

        context = RequestContext(request)
        form = WishForm(request.POST or None)
        if form.is_valid():
            form.save()
            # Add feedback for the user.
            messages.add_message(
                request,
                messages.SUCCESS,
                'Wunsch hinzugefügt.'
            )
            return redirect('admin:wishes_wish_changelist')
        return render_to_response('wishes/wish_backend.html', {'form' : form, 'form_url': form_url}, context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        context = RequestContext(request)

        obj = self.get_object(request, unquote(object_id))

        if not self.has_change_permission(request, obj):
            raise PermissionDenied

        if obj is None:
            raise Http404(_('%(name)s object with primary key %(key)r does not exist.') % {
                'name': 'Wishs', 'key': escape(object_id)})

        if request.method == 'POST':
            print(request)
            form = WishForm(request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form.save()
                # Add feedback for the user.
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Wunsch gespeichert.'
                )
                return redirect('admin:wishes_wish_changelist')
            else:
                new_object = form.instance
        else:
            form = WishForm(instance=obj)

        return render_to_response('wishes/wish_backend.html', {'form' : form, 'form_url': form_url}, context)


    def get_urls(self):
        urls = super(WishAdmin, self).get_urls()
        my_urls = patterns('',
            
        )
        return my_urls + urls

class WishPriorityAdmin(admin.ModelAdmin):
    list_display = ('weight', 'priotxt')

admin.site.register(Wish, WishAdmin)
admin.site.register(WishPriority, WishPriorityAdmin)
