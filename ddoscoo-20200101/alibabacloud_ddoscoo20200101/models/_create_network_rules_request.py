# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNetworkRulesRequest(DaraModel):
    def __init__(
        self,
        ip_mode: str = None,
        network_rules: str = None,
    ):
        self.ip_mode = ip_mode
        # The details of the port forwarding rules, expressed as a character string in JSON format with the following structure:
        # - **InstanceId**: String. Required. The Anti-DDoS Pro or Anti-DDoS Premium instance ID.
        # - **Protocol**: String. Required. The forwarding protocol type. Valid values: **tcp**, **udp**.
        # - **FrontendPort**: Integer. Required. The Redirection Port.
        # - **BackendPort**: Integer. Required. The origin server port.
        # - **RealServers**: JSON array. Required. The list of origin server IP addresses. A maximum of 20 IP addresses are supported.
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
        if self.ip_mode is not None:
            result['IpMode'] = self.ip_mode

        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpMode') is not None:
            self.ip_mode = m.get('IpMode')

        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')

        return self

