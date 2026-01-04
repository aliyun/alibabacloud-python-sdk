# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkRulesResponseBody(DaraModel):
    def __init__(
        self,
        network_rules: List[main_models.DescribeNetworkRulesResponseBodyNetworkRules] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the port forwarding rules.
        self.network_rules = network_rules
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of returned port forwarding rules.
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
                temp_model = main_models.DescribeNetworkRulesResponseBodyNetworkRules()
                self.network_rules.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNetworkRulesResponseBodyNetworkRules(DaraModel):
    def __init__(
        self,
        backend_port: int = None,
        frontend_port: int = None,
        instance_id: str = None,
        is_auto_create: bool = None,
        payload_rule_enable: int = None,
        protocol: str = None,
        proxy_enable: int = None,
        proxy_status: str = None,
        real_servers: List[str] = None,
        remark: str = None,
    ):
        # The port of the origin server.
        self.backend_port = backend_port
        # The forwarding port.
        self.frontend_port = frontend_port
        # The ID of the instance.
        self.instance_id = instance_id
        # Indicates whether the port forwarding rule is automatically created. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_auto_create = is_auto_create
        # Indicates whether the payload filtering rule is enabled. Valid values:
        # 
        # *   1: enabled.
        # *   0: disabled.
        self.payload_rule_enable = payload_rule_enable
        # The forwarding protocol. Valid values:
        # 
        # *   **tcp**
        # *   **udp**
        self.protocol = protocol
        # Indicates whether the traffic diversion switch is on. Valid values:
        # 
        # *   0: on.
        # *   1: off.
        self.proxy_enable = proxy_enable
        # The status of traffic diversion. Valid values:
        # 
        # *   on: Traffic diversion takes effect.
        # *   off: Traffic diversion does not take effect.
        self.proxy_status = proxy_status
        # The IP addresses of origin servers.
        self.real_servers = real_servers
        # The remarks of the port forwarding rule.
        self.remark = remark

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_auto_create is not None:
            result['IsAutoCreate'] = self.is_auto_create

        if self.payload_rule_enable is not None:
            result['PayloadRuleEnable'] = self.payload_rule_enable

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.proxy_enable is not None:
            result['ProxyEnable'] = self.proxy_enable

        if self.proxy_status is not None:
            result['ProxyStatus'] = self.proxy_status

        if self.real_servers is not None:
            result['RealServers'] = self.real_servers

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')

        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsAutoCreate') is not None:
            self.is_auto_create = m.get('IsAutoCreate')

        if m.get('PayloadRuleEnable') is not None:
            self.payload_rule_enable = m.get('PayloadRuleEnable')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('ProxyEnable') is not None:
            self.proxy_enable = m.get('ProxyEnable')

        if m.get('ProxyStatus') is not None:
            self.proxy_status = m.get('ProxyStatus')

        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

