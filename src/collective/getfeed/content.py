# -*- coding: utf-8 -*-
from collective.getfeed.interfaces import IFeed
from collective.getfeed.interfaces import IFeedItem
from plone.dexterity.content import Container
from zope.interface import implementer


@implementer(IFeed)
class Feed(Container):
  """The Feed object"""


@implementer(IFeedItem)
class FeedItem(Container):
  """The Feed Item object."""
