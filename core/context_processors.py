#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings

def base_settings(request):
  return {'settings': settings}
