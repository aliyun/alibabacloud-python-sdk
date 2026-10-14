# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNetworkRuleAttributesRequest(DaraModel):
    def __init__(
        self,
        network_rules: str = None,
    ):
        # The port forwarding rules to query. This parameter is a JSON string with the following structure:
        # - **InstanceId**: String type. Required. The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # - **Protocol**: String type. Required. The forwarding protocol type. Valid values: **tcp**, **udp**.
        # - **FrontendPort**: Integer type. Required. The forwarding port.
        # 
        # This parameter is required.
        self.network_rules = network_rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')

        return self

