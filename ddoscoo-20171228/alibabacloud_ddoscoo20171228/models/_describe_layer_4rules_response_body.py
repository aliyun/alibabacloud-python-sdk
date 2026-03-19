# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeLayer4RulesResponseBody(DaraModel):
    def __init__(
        self,
        listeners: List[main_models.DescribeLayer4RulesResponseBodyListeners] = None,
        request_id: str = None,
        total: int = None,
    ):
        # Detailed configuration of port forwarding rules, including the forwarding port, forwarding protocol, and origin server addresses, etc.
        self.listeners = listeners
        # The ID of the current request.
        self.request_id = request_id
        # The number of returned results.
        self.total = total

    def validate(self):
        if self.listeners:
            for v1 in self.listeners:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Listeners'] = []
        if self.listeners is not None:
            for k1 in self.listeners:
                result['Listeners'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listeners = []
        if m.get('Listeners') is not None:
            for k1 in m.get('Listeners'):
                temp_model = main_models.DescribeLayer4RulesResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeLayer4RulesResponseBodyListeners(DaraModel):
    def __init__(
        self,
        backend_port: int = None,
        bak_mode: int = None,
        current_index: int = None,
        eip: str = None,
        frontend_port: int = None,
        instance_id: str = None,
        is_auto_create: bool = None,
        payload_rule_enable: int = None,
        protocol: str = None,
        proxy_enable: int = None,
        proxy_status: str = None,
        real_servers: List[str] = None,
        remark: str = None,
        us_timeout: main_models.DescribeLayer4RulesResponseBodyListenersUsTimeout = None,
    ):
        # The origin server port.
        self.backend_port = backend_port
        # The origin mode. Values:
        # 
        # - **0**: Indicates the default origin mode.
        # - **1**: Indicates the primary/backup origin mode.
        self.bak_mode = bak_mode
        # The currently effective origin server type. Values:
        # 
        # - **1**: Indicates that the primary origin server settings are in effect (DDoS protection forwards business traffic to the primary origin server IP address).
        # - **2**: Indicates that the backup origin server settings are in effect (DDoS protection forwards business traffic to the backup origin server IP address).
        self.current_index = current_index
        # The IP address of the DDoS protection instance.
        self.eip = eip
        # The forwarding port.
        self.frontend_port = frontend_port
        # The ID of the DDoS protection instance.
        self.instance_id = instance_id
        # Indicates whether the rule was automatically created. Values:
        # 
        # - **true**: Indicates that the rule was automatically created by DDoS protection.
        # - **false**: Indicates that the rule was manually created by you.
        self.is_auto_create = is_auto_create
        # Payload rule module switch. Values:
        # 
        # - 1: Enabled
        # - 0: Disabled
        self.payload_rule_enable = payload_rule_enable
        # The type of forwarding protocol.
        self.protocol = protocol
        # Traffic diversion switch. Values:
        # - **0** Off.
        # - **1** On.
        self.proxy_enable = proxy_enable
        # Traffic diversion status. Values:
        # 
        # - on: Diversion is effective
        # - off: Diversion is ineffective
        self.proxy_status = proxy_status
        # The list of origin server IP addresses.
        self.real_servers = real_servers
        # The remarks for the port forwarding rule.
        self.remark = remark
        self.us_timeout = us_timeout

    def validate(self):
        if self.us_timeout:
            self.us_timeout.validate()

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

        if self.eip is not None:
            result['Eip'] = self.eip

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

        if self.us_timeout is not None:
            result['UsTimeout'] = self.us_timeout.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')

        if m.get('BakMode') is not None:
            self.bak_mode = m.get('BakMode')

        if m.get('CurrentIndex') is not None:
            self.current_index = m.get('CurrentIndex')

        if m.get('Eip') is not None:
            self.eip = m.get('Eip')

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

        if m.get('UsTimeout') is not None:
            temp_model = main_models.DescribeLayer4RulesResponseBodyListenersUsTimeout()
            self.us_timeout = temp_model.from_map(m.get('UsTimeout'))

        return self

class DescribeLayer4RulesResponseBodyListenersUsTimeout(DaraModel):
    def __init__(
        self,
        connect_timeout: int = None,
        rs_timeout: int = None,
    ):
        self.connect_timeout = connect_timeout
        self.rs_timeout = rs_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout

        if self.rs_timeout is not None:
            result['RsTimeout'] = self.rs_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')

        if m.get('RsTimeout') is not None:
            self.rs_timeout = m.get('RsTimeout')

        return self

