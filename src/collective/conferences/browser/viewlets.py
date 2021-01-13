from plone.app.layout.viewlets import common as base
from Products.CMFCore.permissions import ViewManagementScreens
from Products.CMFCore.utils import getToolByName

from collective.conferences.interfaces import IVoting


class Vote(base.ViewletBase):

    vote = None
    is_manager = None

    def update(self):
        super(Vote, self).update()

        if self.vote is None:
            self.vote = IVoting(self.context)
        if self.is_manager is None:
            membership_tool = getToolByName(self.context, 'portal_membership')
            self.is_manager = membership_tool.checkPermission(
                ViewManagementScreens, self.context)

    def voted(self):
        return self.vote.already_voted(self.request)

    def average(self):
        return self.vote.average_vote()

    def has_votes(self):
        return self.vote.has_votes()
