# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.js.rgraph.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of collective.js.rgraph into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.js.rgraph is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.js.rgraph'))

    def test_uninstall(self):
        """Test if collective.js.rgraph is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.js.rgraph'])
        self.assertFalse(self.installer.isProductInstalled('collective.js.rgraph'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICollective.jsRgraphLayer is registered."""
        from collective.js.rgraph.interfaces import ICollective.jsRgraphLayer
        from plone.browserlayer import utils
        self.failUnless(ICollective.jsRgraphLayer in utils.registered_layers())
