# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribePortResponseBody(DaraModel):
    def __init__(
        self,
        network_rules: List[main_models.DescribePortResponseBodyNetworkRules] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of port forwarding rules.
        self.network_rules = network_rules
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The number of port forwarding rules returned.
        self.total_count = total_count

    def validate(self):
        if self.network_rules:
            for v1 in self.network_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkRules'] = []
        if self.network_rules is not None:
            for k1 in self.network_rules:
                result['NetworkRules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_rules = []
        if m.get('NetworkRules') is not None:
            for k1 in m.get('NetworkRules'):
                temp_model = main_models.DescribePortResponseBodyNetworkRules()
                self.network_rules.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePortResponseBodyNetworkRules(DaraModel):
    def __init__(
        self,
        backend_port: int = None,
        frontend_port: int = None,
        frontend_protocol: str = None,
        instance_id: str = None,
        is_auto_create: bool = None,
        real_servers: List[str] = None,
    ):
        # The port of the origin server.
        self.backend_port = backend_port
        # The forwarding port.
        self.frontend_port = frontend_port
        # The type of the protocol. Valid values:
        # 
        # *   **tcp**
        # *   **udp**
        self.frontend_protocol = frontend_protocol
        # The ID of the instance to which the port forwarding rule is applied.
        self.instance_id = instance_id
        # Indicates whether the port forwarding rule is automatically created by the instance. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.is_auto_create = is_auto_create
        # An array that consists of IP addresses of origin servers.
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

        if self.is_auto_create is not None:
            result['IsAutoCreate'] = self.is_auto_create

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

        if m.get('IsAutoCreate') is not None:
            self.is_auto_create = m.get('IsAutoCreate')

        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')

        return self

