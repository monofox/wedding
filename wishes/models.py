#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import pytz

class WishPriority(models.Model):
	class Meta:
		verbose_name = _('Wish Priority')
		verbose_name_plural = _('Wish Priorities')
		ordering = ['weight']

	weight = models.PositiveSmallIntegerField(verbose_name=_('Weight'))
	priotxt = models.CharField(max_length=125, verbose_name=_('Priority'))
	
	def __str__(self):
		return self.priotxt

class Wish(models.Model):
	class Meta:
		verbose_name = _('Wish')
		verbose_name_plural = _('Wishes')
		ordering = ['priority']

	_subject = _('%(couple)s wish will be fullfilled: %(wish)s')
	_text_pattern = _('Sender: %(sender)s\nDate: %(date)s\n\nWish: \n%(wish)s')

	priority = models.ForeignKey(WishPriority, verbose_name=_('Priority'))
	wishcover = models.ImageField(upload_to='upload/wishes')
	wishtxt = models.TextField(verbose_name=_('The wish'))
	wishisbn = models.CharField(max_length=120)
	visible = models.BooleanField(default=False, verbose_name=_('Visible'))
	dtticrt = models.DateTimeField(auto_now_add=True)
	dttichg = models.DateTimeField(auto_now=True)
	# save the timestamp when somebody says: i ordered it!
	dttiord = models.DateTimeField(default=None, null=True, verbose_name=_('Date of order'))

	def ordered(self, name, email):
		self.dttiord = datetime.now().replace(tzinfo=pytz.timezone(settings.TIME_ZONE)) if settings.USE_TZ else datetime.now()

		# Send mail with detailed information
		if settings.WISH_ORDER_MAIL is not None:
			text = self._text_pattern % {
				'sender': name,
				'date' 	: str(self.dttiord),
				'wish'  : self.wishtxt
			}
			subjectText = self._subject % {
				'couple': '+'.join(settings.COUPLE_NAMES),
				'wish': self.wishtxt[:20]
			}
			send_mail(subjectText, text, email, [settings.WISH_ORDER_MAIL])
