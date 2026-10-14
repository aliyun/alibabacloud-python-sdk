# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreatePortRequest(DaraModel):
    def __init__(
        self,
        backend_port: str = None,
        frontend_port: str = None,
        frontend_protocol: str = None,
        instance_id: str = None,
        ip_mode: str = None,
        proxy_enable: int = None,
        real_servers: List[str] = None,
    ):
        # The origin server port. Valid values: **0** to **65535**.
        self.backend_port = backend_port
        # The forward port. Valid values: **0** to **65535**.
        # 
        # This parameter is required.
        self.frontend_port = frontend_port
        # The forwarding protocol type. Valid values:
        # 
        # - **tcp**: TCP protocol.
        # - **udp**: UDP protocol.
        # 
        # This parameter is required.
        self.frontend_protocol = frontend_protocol
        # The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance to which the port forwarding rule belongs.
        # 
        # > You can call [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) to query the IDs of all Anti-DDoS Pro or Anti-DDoS Premium instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.ip_mode = ip_mode
        # The traffic redirection switch. Valid values:
        # - **0**: disabled.
        # - **1**: enabled.
        self.proxy_enable = proxy_enable
        # The list of origin server IP addresses.
        # 
        # This parameter is required.
        self.real_servers = real_servers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_port is not None:
            result['BackendPort'] = self.backend_port

        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port

        if self.frontend_protocol is not None:
            result['FrontendProtocol'] = self.frontend_protocol

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip_mode is not None:
            result['IpMode'] = self.ip_mode

        if self.proxy_enable is not None:
            result['ProxyEnable'] = self.proxy_enable

        if self.real_servers is not None:
            result['RealServers'] = self.real_servers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')

        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')

        if m.get('FrontendProtocol') is not None:
            self.frontend_protocol = m.get('FrontendProtocol')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IpMode') is not None:
            self.ip_mode = m.get('IpMode')

        if m.get('ProxyEnable') is not None:
            self.proxy_enable = m.get('ProxyEnable')

        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')

        return self

