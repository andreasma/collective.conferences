# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope.interface import Interface
from zope.interface import provider
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveConferencesLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IVotableLayer(Interface):
    """Marker interface for the Browserlayer
    """


class IVotable(Interface):
    pass


@provider(IFormFieldProvider)
class IVoting(model.Schema):
    pass
