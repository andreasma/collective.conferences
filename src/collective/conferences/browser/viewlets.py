# encoding=utf-8
from collective.conferences import DoVote
from collective.conferences.interfaces import IVoting
from plone import api
from plone.app.layout.viewlets import common as base
from Products.CMFCore.permissions import ViewManagementScreens


class Vote(base.ViewletBase):
    vote = None
    is_manager = None

    def update(self):
        super(Vote, self).update()

        if self.vote is None:
            self.vote = IVoting(self.context)
        if self.is_manager is None:
            self.is_manager = api.user.has_permission(ViewManagementScreens)
            self.can_vote = api.user.has_permission(DoVote)

    def voted(self):
        return self.vote.already_voted(self.request)

    def average(self):
        return self.vote.average_vote()

    def has_votes(self):
        return self.vote.has_votes()
