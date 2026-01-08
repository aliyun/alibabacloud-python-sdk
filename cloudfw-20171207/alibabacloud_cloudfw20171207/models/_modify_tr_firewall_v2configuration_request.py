# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyTrFirewallV2ConfigurationRequest(DaraModel):
    def __init__(
        self,
        firewall_id: str = None,
        firewall_name: str = None,
        lang: str = None,
    ):
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The instance name of the VPC firewall.
        self.firewall_name = firewall_name
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id

        if self.firewall_name is not None:
            result['FirewallName'] = self.firewall_name

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')

        if m.get('FirewallName') is not None:
            self.firewall_name = m.get('FirewallName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

