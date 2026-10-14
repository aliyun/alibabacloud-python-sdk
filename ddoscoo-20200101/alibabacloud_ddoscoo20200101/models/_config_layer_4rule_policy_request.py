# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigLayer4RulePolicyRequest(DaraModel):
    def __init__(
        self,
        listeners: str = None,
    ):
        # The port forwarding rules.
        # 
        # This parameter is a string that represents a JSON array converted from a character string. Each element in the JSON array represents a created port forwarding rule. You can specify up to one port forwarding rule at a time.
        # 
        # > You can invoke [DescribeNetworkRules](https://help.aliyun.com/document_detail/157484.html) to query all created port forwarding rules.
        # 
        # Each port forwarding rule contains the following fields:
        # 
        # - **InstanceId**: string. Required. The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # - **Protocol**: string. Required. The forwarding protocol type. Valid values: **tcp**, **udp**.
        # - **FrontendPort**: integer. Required. The Redirection Port.
        # - **BackendPort**: integer. Required. The origin server port.
        # - **PriRealServers**: JSON array. Required. The list of primary origin server IP addresses. Each element in the JSON array represents a primary origin server IP address. You can specify up to 20 primary origin server IP addresses.
        # 
        #     Each primary origin server IP address contains the following fields:
        # 
        #     - **RealServer**: string. Required. The primary origin server IP address.
        # 
        # - **SecRealServers**: JSON array. Required. The list of secondary origin server IP addresses. Each element in the JSON array represents a secondary origin server IP address. You can specify up to 20 secondary origin server IP addresses.
        # 
        #     Each secondary origin server IP address contains the following fields:
        #     
        #     - **RealServer**: string. Required. The secondary origin server IP address.
        #  
        # - **CurrentRsIndex**: integer. Required. The type of origin server to activate. Valid values:
        #     - **1**: The primary origin server settings take effect. Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the primary origin server IP addresses.
        #     - **2**: The secondary origin server settings take effect. Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the secondary origin server IP addresses.
        # 
        # This parameter is required.
        self.listeners = listeners

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listeners is not None:
            result['Listeners'] = self.listeners

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')

        return self

