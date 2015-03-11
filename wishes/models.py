#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _

class WishPriority(models.Model):
	weight = models.PositiveSmallIntegerField()
	priotxt = models.CharField(max_length=125)

	class Meta:
		verbose_name = 'Wish Priority'
		verbose_name_plural = 'Wish Priorities'
		ordering = ['weight']
	
	def __str__(self):
		return self.priotxt

class Wish(models.Model):
	priority = models.ForeignKey(WishPriority)
	wishcover = models.ImageField(upload_to='upload/wishes')
	wishtxt = models.TextField()
	wishisbn = models.CharField(max_length=120)
	visible = models.BooleanField(default=False)
	dtticrt = models.DateTimeField(auto_now_add=True)
	dttichg = models.DateTimeField(auto_now=True)
	# save the timestamp when somebody says: i ordered it!
	dttiord = models.DateTimeField(default=None, null=True)

	class Meta:
		verbose_name = 'Wish'
		verbose_name_plural = 'Wishes'
		ordering = ['priority']

	pass