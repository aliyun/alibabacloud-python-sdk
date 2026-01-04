# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNetworkRuleAttributesRequest(DaraModel):
    def __init__(
        self,
        network_rules: str = None,
    ):
        # The details of the port forwarding rule. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **InstanceId**: the ID of the instance. This field is required and must be of the STRING type.
        # *   **Protocol**: the forwarding protocol. This field is required and must be of the STRING type. Valid values: **tcp** and **udp**.
        # *   **FrontendPort**: the forwarding port. This field is required and must be of the INTEGER type.
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

