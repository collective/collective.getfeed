# -*- coding: utf-8 -*-
from .interfaces import IFeed
from .interfaces import IFeedItem
from plone.dexterity.content import Container
from zope.interface import implementer


@implementer(IFeed)
class Feed(Container):
  """"""


@implementer(IFeedItem)
class FeedItem(Container):
  """"""
