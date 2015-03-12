#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from core import mail
import hashlib

class ContactMail(models.Model):
	class Meta:
		verbose_name = _("Contact Mail")
		verbose_name_plural = _("Contact Mails")

	_recipient = settings.CONTACT_MAIL
	_subject = _('%(couple)s request: %(subject)s')
	_text_pattern = _('Sender: %(sender)s\nDate: %(date)s\nSubject: %(subject)s\n\n%(content)s')

	name = models.CharField(max_length=100, verbose_name=_("Name"))
	sender = models.EmailField(max_length=128, verbose_name=_("Email address"))
	contact_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Date"))
	sendersubject = models.CharField(max_length=100, verbose_name=_("Subject"))
	content = models.TextField(verbose_name=_("Message"), help_text=_('What do you want to tell them?'))

	def __unicode__(self):
		return self.subject

	def save(self, *args, **kwargs):
		super(ContactMail, self).save(*args, **kwargs)

		# Send mail
		if self._recipient is not None:
			text = self._text_pattern % {
				'sender' : self.sender,
				'date' 	: str(self.contact_date),
				'subject' : self.sendersubject,
				'content' : self.content
			}
			subjectText = self._subject % {
				'couple': '+'.join(settings.COUPLE_NAMES),
				'subject': self.sendersubject
			}
			send_mail(subjectText, text, self.sender, [self._recipient])