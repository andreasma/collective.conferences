# encoding=utf-8
from .interfaces import IVoting
from zope.interface import implementer


KEY = "collective.conferences.behavior.voting.Vote"


@implementer(IVoting)
class Vote(object):
    pass
