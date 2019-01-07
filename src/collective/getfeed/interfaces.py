# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.supermodel import model


class ICollectivegetfeedCoreLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IFeed(model.Schema):
    """ Feed content type interface
    """


class IFeedItem(model.Schema):
    """ Feed Item content type interface
    """
