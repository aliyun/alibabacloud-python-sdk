# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeLayer4RulePolicyResponseBody(DaraModel):
    def __init__(
        self,
        backend_port: int = None,
        bak_mode: str = None,
        current_index: int = None,
        forward_protocol: str = None,
        frontend_port: int = None,
        instance_id: str = None,
        pri_real_servers: List[main_models.DescribeLayer4RulePolicyResponseBodyPriRealServers] = None,
        request_id: str = None,
        sec_real_servers: List[main_models.DescribeLayer4RulePolicyResponseBodySecRealServers] = None,
    ):
        # The port of the origin server.
        self.backend_port = backend_port
        # The mode that is used to forward service traffic. Valid values:
        # 
        # *   0: the default mode. In this mode, Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the origin IP address that you specified when you created the port forwarding rule. You can call the [CreateNetworkRules](https://help.aliyun.com/document_detail/157482.html) operation to create a port forwarding rule.
        # *   1: the origin redundancy mode. In this mode, Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the primary or secondary origin servers. You can call the [ConfigLayer4RulePolicy](https://help.aliyun.com/document_detail/312684.html) operation to configure IP addresses.
        self.bak_mode = bak_mode
        # The origin server that is used to receive service traffic. Valid values:
        # 
        # *   **1**: the primary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the primary origin server.
        # *   **2**: the secondary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the secondary origin server.
        self.current_index = current_index
        # The type of the protocol.
        self.forward_protocol = forward_protocol
        # The forwarding port.
        self.frontend_port = frontend_port
        # The ID of the instance.
        self.instance_id = instance_id
        # An array that consists of the information about the primary origin server, including the IP addresses, forwarding protocol, and forwarding port.
        self.pri_real_servers = pri_real_servers
        # The ID of the request.
        self.request_id = request_id
        # An array that consists of the information about the secondary origin server, including the IP addresses, forwarding protocol, and forwarding port.
        self.sec_real_servers = sec_real_servers

    def validate(self):
        if self.pri_real_servers:
            for v1 in self.pri_real_servers:
                 if v1:
                    v1.validate()
        if self.sec_real_servers:
            for v1 in self.sec_real_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_port is not None:
            result['BackendPort'] = self.backend_port

        if self.bak_mode is not None:
            result['BakMode'] = self.bak_mode

        if self.current_index is not None:
            result['CurrentIndex'] = self.current_index

        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol

        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['PriRealServers'] = []
        if self.pri_real_servers is not None:
            for k1 in self.pri_real_servers:
                result['PriRealServers'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SecRealServers'] = []
        if self.sec_real_servers is not None:
            for k1 in self.sec_real_servers:
                result['SecRealServers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')

        if m.get('BakMode') is not None:
            self.bak_mode = m.get('BakMode')

        if m.get('CurrentIndex') is not None:
            self.current_index = m.get('CurrentIndex')

        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')

        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.pri_real_servers = []
        if m.get('PriRealServers') is not None:
            for k1 in m.get('PriRealServers'):
                temp_model = main_models.DescribeLayer4RulePolicyResponseBodyPriRealServers()
                self.pri_real_servers.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sec_real_servers = []
        if m.get('SecRealServers') is not None:
            for k1 in m.get('SecRealServers'):
                temp_model = main_models.DescribeLayer4RulePolicyResponseBodySecRealServers()
                self.sec_real_servers.append(temp_model.from_map(k1))

        return self

class DescribeLayer4RulePolicyResponseBodySecRealServers(DaraModel):
    def __init__(
        self,
        current_index: int = None,
        eip: str = None,
        frontend_port: int = None,
        instance_id: str = None,
        protocol: str = None,
        real_server: str = None,
    ):
        # The origin server that is used to receive service traffic. Valid values:
        # 
        # *   **1**: the primary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the primary origin server.
        # *   **2**: the secondary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the secondary origin server.
        self.current_index = current_index
        # The IP address of the instance.
        self.eip = eip
        # The forwarding port.
        self.frontend_port = frontend_port
        # The ID of the instance.
        self.instance_id = instance_id
        # The type of the protocol.
        self.protocol = protocol
        # The IP address of the secondary origin server.
        self.real_server = real_server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_index is not None:
            result['CurrentIndex'] = self.current_index

        if self.eip is not None:
            result['Eip'] = self.eip

        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.real_server is not None:
            result['RealServer'] = self.real_server

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentIndex') is not None:
            self.current_index = m.get('CurrentIndex')

        if m.get('Eip') is not None:
            self.eip = m.get('Eip')

        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')

        return self

class DescribeLayer4RulePolicyResponseBodyPriRealServers(DaraModel):
    def __init__(
        self,
        current_index: int = None,
        eip: str = None,
        frontend_port: int = None,
        instance_id: str = None,
        protocol: str = None,
        real_server: str = None,
    ):
        # The origin server that is used to receive service traffic. Valid values:
        # 
        # *   **1**: the primary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the primary origin server.
        # *   **2**: the secondary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the secondary origin server.
        self.current_index = current_index
        # The IP address of the instance.
        self.eip = eip
        # The forwarding port.
        self.frontend_port = frontend_port
        # The ID of the instance.
        self.instance_id = instance_id
        # The type of the protocol.
        self.protocol = protocol
        # The IP address of the primary origin server.
        self.real_server = real_server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_index is not None:
            result['CurrentIndex'] = self.current_index

        if self.eip is not None:
            result['Eip'] = self.eip

        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.real_server is not None:
            result['RealServer'] = self.real_server

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentIndex') is not None:
            self.current_index = m.get('CurrentIndex')

        if m.get('Eip') is not None:
            self.eip = m.get('Eip')

        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')

        return self

