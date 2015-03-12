#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from simplemathcaptcha.fields import MathCaptchaField
from core.models import ContactMail
from django.utils.translation import ugettext as _

class ContactForm(forms.ModelForm):
	class Meta:
		model = ContactMail
		fields = ['name', 'sender', 'sendersubject', 'content']

class OrderForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	captcha = MathCaptchaField()
	wishid = forms.IntegerField(min_value=1, widget=forms.HiddenInput)