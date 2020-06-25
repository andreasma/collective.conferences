from plone.app.testing import (PLONE_FIXTURE, FunctionalTesting,
                               IntegrationTesting, PloneSandboxLayer,
                               applyProfile)
from zope.configuration import xmlconfig


class CollectiveConferences(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.conferences
        xmlconfig.file('configure.zcml',
                       collective.conferences,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.conferences:default')

COLLECTIVE_CONFERENCES_FIXTURE = CollectiveConferences()
COLLECTIVE_CONFERENCES_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COLLECTIVE_CONFERENCES_FIXTURE, ),
                       name="CollectiveConferences:Integration")
