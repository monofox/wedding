#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig

class WishlistConfig(AppConfig):
	name = 'wishes'
	verbose_name = _('Wishlist')