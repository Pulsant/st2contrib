"""Generated test for checking pynos based actions
"""
import xml.etree.ElementTree as ET
from st2tests.base import BaseActionTestCase
from bgp_max_paths import bgp_max_paths

__all__ = [
    'TestBgpMaxPaths'
]


class MockCallback(object):  # pylint:disable=too-few-public-methods
    """Class to hold mock callback and result
    """
    returned_data = None

    def callback(self, call, **kwargs):  # pylint:disable=unused-argument
        """Mock callback method
        """
        xml_result = ET.tostring(call)
        self.returned_data = xml_result


class TestBgpMaxPaths(BaseActionTestCase):
    """Test holder class
    """
    action_cls = bgp_max_paths

    def test_action(self):
        """Generated test to check action
        """
        action = self.get_action_instance()
        mock_callback = MockCallback()
        kwargs = {
            'username': '',
            'paths': '10',
            'afi': 'ipv4',
            'get': False,
            'ip': '',
            'vrf': 'test',
            'password': '',
            'port': '22',
            'rbridge_id': '224',
            'test': True,
            'callback': mock_callback.callback
        }

        action.run(**kwargs)

        expected_xml = (
            '<config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">'
            '<rbridge-id>224</rbridge-id><router><bgp xmlns="urn:brocade.com:m'
            'gmt:brocade-bgp"><vrf-name>test</vrf-name><router-bgp-cmds-holder'
            '><address-family><ipv4><ipv4-unicast><af-common-cmds-holder><maxi'
            'mum-paths><load-sharing-value>10</load-sharing-value></maximum-pa'
            'ths></af-common-cmds-holder></ipv4-unicast></ipv4></address-famil'
            'y></router-bgp-cmds-holder></bgp></router></rbridge-id></config>'
        )

        self.assertTrue(expected_xml, mock_callback.returned_data)
