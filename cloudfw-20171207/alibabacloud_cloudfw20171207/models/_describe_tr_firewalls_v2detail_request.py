# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTrFirewallsV2DetailRequest(DaraModel):
    def __init__(
        self,
        firewall_id: str = None,
        lang: str = None,
    ):
        # The instance ID of the virtual private cloud (VPC) firewall.
        # > FirewallId is required. If this parameter is not specified, ErrorParameters(400) is returned. You can call DescribeTrFirewallsV2List to query existing FirewallId values. If no VPC firewall exists, create a CEN instance and a transit router first, and then call CreateTrFirewallV2 to obtain a FirewallId.
        self.firewall_id = firewall_id
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese
        # - **en**: English
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

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

