#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from core import mail
import hashlib

class ContactMail(models.Model):
	class Meta:
		verbose_name = _("Contact Mail")
		verbose_name_plural = _("Contact Mails")

	recipient = "webmaster@lschreiner.de"
	subject = _("Anja+David Anfrage: ")
	text_pattern = _("Sender: %(sender)s\nDate: %(date)s\nSubject: %(subject)s\n\n%(content)s")

	name = models.CharField(max_length=100, verbose_name=_("Name"))
	sender = models.EmailField(max_length=128, verbose_name=_("Email address"))
	contact_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Date"))
	sendersubject = models.CharField(max_length=100, verbose_name=_("Subject"))
	content = models.TextField(verbose_name=_("Text"), help_text='Was möchtest Du den beiden sagen?')

	def __unicode__(self):
		return self.subject

	def save(self, *args, **kwargs):
		super(ContactMail, self).save(*args, **kwargs)

		# Send mail
		text = self.text_pattern % {
			'sender' : self.sender,
			'date' 	: str(self.contact_date),
			'subject' : self.sendersubject,
			'content' : self.content
		}
		send_mail(self.subject + self.sendersubject, text, self.sender, [self.recipient])