# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigLayer4RulePolicyRequest(DaraModel):
    def __init__(
        self,
        listeners: str = None,
    ):
        # The port forwarding rule that you want to manage.
        # 
        # This parameter is a string that consists of JSON arrays. Each element in a JSON array indicates a port forwarding rule. You can perform this operation only on one port forwarding rule at a time.
        # 
        # > You can call the [DescribeNetworkRules](https://help.aliyun.com/document_detail/157484.html) to query existing port forwarding rules.
        # 
        # Each port forwarding rule contains the following fields:
        # 
        # *   **InstanceId**: the ID of the instance. This field is required and must be of the STRING type.
        # 
        # *   **Protocol**: the forwarding protocol. This field is required and must be of the STRING type. Valid values: **tcp** and **udp**.
        # 
        # *   **FrontendPort**: the forwarding port. This field is required and must be of the INTEGER type.
        # 
        # *   **BackendPort**: the port of the origin server. This field is required and must be of the INTEGER type.
        # 
        # *   **PriRealServers**: the IP addresses of the primary origin server. This field is required and must be a JSON array. Each element in a JSON array indicates an IP address of the primary origin server. You can configure a maximum of 20 IP addresses.
        # 
        #     Each element in the JSON array contains the following field:
        # 
        #     *   **RealServer**: the IP address of the primary origin server. This field is required and must be of the STRING type.
        # 
        # *   **SecRealServers**: the IP addresses of the secondary origin server. This field is required and must be a JSON array. Each element in a JSON array indicates an IP address of the secondary origin server. You can configure a maximum of 20 IP addresses.
        # 
        #     Each element in the JSON array contains the following field:
        # 
        #     *   **RealServer**: the IP address of the secondary origin server. This field is required and must be of the STRING type.
        # 
        # *   **CurrentRsIndex**: the origin server that you want to use to receive service traffic. This field is required and must be of the INTEGER type. Valid values:
        # 
        #     *   **1**: the primary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the primary origin server.
        #     *   **2**: the secondary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the secondary origin server.
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

