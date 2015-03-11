#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from wishes.models import Wish, WishPriority

class WishForm(forms.ModelForm):
	class Meta:
		model = Wish
		fields = ['priority', 'wishcover', 'wishisbn', 'wishtxt', 'visible']
		# we have to prepare the priority list!
	
	def __init__(self, data=None, files=None, instance=None):
		super().__init__(data=data, files=files, instance=instance)
		self.fields['priority'].label = 'Priorität'
		self.fields['visible'].label = 'Sichtbar'
		self.fields['visible'].required = False
		self.fields['wishisbn'].required = False
		self.fields['wishcover'].required = False
