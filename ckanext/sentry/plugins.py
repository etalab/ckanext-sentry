# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from ckan import plugins


log = logging.getLogger(__name__)


class SentryPlugin(plugins.SingletonPlugin):
    '''A simple plugin that add the Sentry middleware to CKAN'''
    plugins.implements(plugins.IMiddleware)

    def make_middleware(self, app, config):
        from raven.contrib.pylons import Sentry
        return Sentry(app, config)
