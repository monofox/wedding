#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.core.mail import send_mail
from wishes.models import Wish, WishPriority
from wishes.views import WishList
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.utils.translation import ugettext as _
from core.forms import ContactForm, OrderForm
from core import mail
import logging

def index(request):
	contactForm = ContactForm()
	# the "order" form will be provided multiple times!
	orderForm = OrderForm()
	wishList = WishList().get_queryset().filter(visible=1, dttiord=None)
	context = RequestContext(request)
	context_dic = {"cform": contactForm, 'wishlist': wishList, 'wishOrderForm': orderForm}

	return render_to_response('core/index.html', context_dic, context)

def static(request, site, content_type="text/html"):
	return render_to_response(
		'core/{0}'.format(site),
		{},
		RequestContext(request),
		content_type=content_type
	)

def send_contactmail(request):
	'''
	Called via ajax.
	'''
	context = RequestContext(request)
	status = False

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			status = True
	else:
		form = ContactForm()

	return render_to_response('core/contact_form.html', {
			'form': form,
			'success': status
		}, context)

def reset_ordered_form(request):
	'''
	Called via ajax.
	'''
	context = RequestContext(request)
	form = OrderForm()

	return render_to_response('wishes/order_form.html', {
			'wishOrderForm': form,
			'wofsuc': '0'
		}, context)

def set_wish_ordered(request):
	'''
	Called via ajax.
	'''
	context = RequestContext(request)
	status = '0'

	form = OrderForm(request.POST or None)
	if form.is_valid():
		if request.POST:
			status = form.cleaned_data['wishid']
			try:
				wish = Wish.objects.get(id=form.cleaned_data['wishid'])
			except Wish.DoesNotExist:
				pass
			else:	
				wish.ordered(form.cleaned_data['name'], form.cleaned_data['email'])
				wish.save()
		form = OrderForm()

	return render_to_response('wishes/order_form.html', {
			'wishOrderForm': form,
			'wofsuc': status
		}, context)