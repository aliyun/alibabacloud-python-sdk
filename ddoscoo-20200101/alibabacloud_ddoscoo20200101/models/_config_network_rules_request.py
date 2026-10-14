# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigNetworkRulesRequest(DaraModel):
    def __init__(
        self,
        network_rules: str = None,
    ):
        # The details of the port forwarding rules. The value is a JSON format character string that contains the following structure:
        # - **InstanceId**: String. Required. The instance ID of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # - **Protocol**: String. Required. The forwarding protocol type. Valid values: **tcp**, **udp**.
        # - **FrontendPort**: Integer. Required. The Redirection Port.
        # - **BackendPort**: Integer. Required. The origin server port.
        # - **RealServers**: JSON array. Required. The list of origin server IP addresses. A maximum of 20 IP addresses are supported.
        # 
        # > When you edit port forwarding rules, you can modify only **RealServers**, which specifies the origin server IP addresses.
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

