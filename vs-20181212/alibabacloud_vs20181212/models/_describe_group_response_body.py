# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupResponseBody(DaraModel):
    def __init__(
        self,
        alias_id: str = None,
        app: str = None,
        callback: str = None,
        created_time: str = None,
        description: str = None,
        enabled: bool = None,
        gb_id: str = None,
        gb_ip: str = None,
        gb_port: int = None,
        gb_tcp_ports: List[str] = None,
        gb_udp_ports: List[str] = None,
        id: str = None,
        in_protocol: str = None,
        lazy_pull: bool = None,
        name: str = None,
        out_protocol: str = None,
        play_domain: str = None,
        push_domain: str = None,
        region: str = None,
        request_id: str = None,
        stats: main_models.DescribeGroupResponseBodyStats = None,
        status: str = None,
    ):
        self.alias_id = alias_id
        self.app = app
        self.callback = callback
        self.created_time = created_time
        self.description = description
        self.enabled = enabled
        self.gb_id = gb_id
        self.gb_ip = gb_ip
        self.gb_port = gb_port
        self.gb_tcp_ports = gb_tcp_ports
        self.gb_udp_ports = gb_udp_ports
        self.id = id
        self.in_protocol = in_protocol
        self.lazy_pull = lazy_pull
        self.name = name
        self.out_protocol = out_protocol
        self.play_domain = play_domain
        self.push_domain = push_domain
        self.region = region
        self.request_id = request_id
        self.stats = stats
        self.status = status

    def validate(self):
        if self.stats:
            self.stats.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_id is not None:
            result['AliasId'] = self.alias_id

        if self.app is not None:
            result['App'] = self.app

        if self.callback is not None:
            result['Callback'] = self.callback

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.gb_id is not None:
            result['GbId'] = self.gb_id

        if self.gb_ip is not None:
            result['GbIp'] = self.gb_ip

        if self.gb_port is not None:
            result['GbPort'] = self.gb_port

        if self.gb_tcp_ports is not None:
            result['GbTcpPorts'] = self.gb_tcp_ports

        if self.gb_udp_ports is not None:
            result['GbUdpPorts'] = self.gb_udp_ports

        if self.id is not None:
            result['Id'] = self.id

        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol

        if self.lazy_pull is not None:
            result['LazyPull'] = self.lazy_pull

        if self.name is not None:
            result['Name'] = self.name

        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol

        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain

        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain

        if self.region is not None:
            result['Region'] = self.region

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stats is not None:
            result['Stats'] = self.stats.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasId') is not None:
            self.alias_id = m.get('AliasId')

        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('Callback') is not None:
            self.callback = m.get('Callback')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')

        if m.get('GbIp') is not None:
            self.gb_ip = m.get('GbIp')

        if m.get('GbPort') is not None:
            self.gb_port = m.get('GbPort')

        if m.get('GbTcpPorts') is not None:
            self.gb_tcp_ports = m.get('GbTcpPorts')

        if m.get('GbUdpPorts') is not None:
            self.gb_udp_ports = m.get('GbUdpPorts')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')

        if m.get('LazyPull') is not None:
            self.lazy_pull = m.get('LazyPull')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')

        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')

        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Stats') is not None:
            temp_model = main_models.DescribeGroupResponseBodyStats()
            self.stats = temp_model.from_map(m.get('Stats'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeGroupResponseBodyStats(DaraModel):
    def __init__(
        self,
        device_num: int = None,
        ied_num: int = None,
        ipc_num: int = None,
        platform_num: int = None,
    ):
        self.device_num = device_num
        self.ied_num = ied_num
        self.ipc_num = ipc_num
        self.platform_num = platform_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_num is not None:
            result['DeviceNum'] = self.device_num

        if self.ied_num is not None:
            result['IedNum'] = self.ied_num

        if self.ipc_num is not None:
            result['IpcNum'] = self.ipc_num

        if self.platform_num is not None:
            result['PlatformNum'] = self.platform_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceNum') is not None:
            self.device_num = m.get('DeviceNum')

        if m.get('IedNum') is not None:
            self.ied_num = m.get('IedNum')

        if m.get('IpcNum') is not None:
            self.ipc_num = m.get('IpcNum')

        if m.get('PlatformNum') is not None:
            self.platform_num = m.get('PlatformNum')

        return self

