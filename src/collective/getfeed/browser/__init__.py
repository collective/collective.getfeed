# -*- coding: utf-8 -*-
from collective.getfeed.interfaces import IFeed
from collective.getfeed.interfaces import IFeedItem
from plone.dexterity.browser.view import DefaultView


class FeedView(DefaultView):
    """Defaul view for Feed content type."""


class FeedItemView(DefaultView):
    """Defaul view for Feed Item content type."""
