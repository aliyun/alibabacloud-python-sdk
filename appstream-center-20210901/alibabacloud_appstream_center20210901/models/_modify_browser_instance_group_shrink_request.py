# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBrowserInstanceGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        browser_config_shrink: str = None,
        browser_instance_group_id: str = None,
        cloud_browser_name: str = None,
        network_shrink: str = None,
        policy_shrink: str = None,
        timers_shrink: str = None,
    ):
        # The browser settings.
        self.browser_config_shrink = browser_config_shrink
        # The ID of the cloud browser to be modified.
        # 
        # This parameter is required.
        self.browser_instance_group_id = browser_instance_group_id
        # The name of the cloud browser.
        self.cloud_browser_name = cloud_browser_name
        # The network configurations.
        self.network_shrink = network_shrink
        # The access policy.
        self.policy_shrink = policy_shrink
        # The timer.
        self.timers_shrink = timers_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_config_shrink is not None:
            result['BrowserConfig'] = self.browser_config_shrink

        if self.browser_instance_group_id is not None:
            result['BrowserInstanceGroupId'] = self.browser_instance_group_id

        if self.cloud_browser_name is not None:
            result['CloudBrowserName'] = self.cloud_browser_name

        if self.network_shrink is not None:
            result['Network'] = self.network_shrink

        if self.policy_shrink is not None:
            result['Policy'] = self.policy_shrink

        if self.timers_shrink is not None:
            result['Timers'] = self.timers_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrowserConfig') is not None:
            self.browser_config_shrink = m.get('BrowserConfig')

        if m.get('BrowserInstanceGroupId') is not None:
            self.browser_instance_group_id = m.get('BrowserInstanceGroupId')

        if m.get('CloudBrowserName') is not None:
            self.cloud_browser_name = m.get('CloudBrowserName')

        if m.get('Network') is not None:
            self.network_shrink = m.get('Network')

        if m.get('Policy') is not None:
            self.policy_shrink = m.get('Policy')

        if m.get('Timers') is not None:
            self.timers_shrink = m.get('Timers')

        return self

