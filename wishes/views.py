#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.db import IntegrityError
from django.utils.translation import ugettext as _
from django.views.generic import ListView
from wishes.models import Wish, WishPriority
import logging

class WishList(ListView):
	model = Wish