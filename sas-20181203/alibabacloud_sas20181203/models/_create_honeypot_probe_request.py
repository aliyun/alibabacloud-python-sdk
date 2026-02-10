# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateHoneypotProbeRequest(DaraModel):
    def __init__(
        self,
        arp: bool = None,
        business_group_id: str = None,
        control_node_id: str = None,
        display_name: str = None,
        honeypot_bind_list: List[main_models.CreateHoneypotProbeRequestHoneypotBindList] = None,
        ping: bool = None,
        probe_type: str = None,
        probe_version: str = None,
        proxy_ip: str = None,
        uuid: str = None,
        vpc_id: str = None,
    ):
        # Specifies whether to enable Address Resolution Protocol (ARP) spoofing. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.arp = arp
        # The ID of the business group.
        self.business_group_id = business_group_id
        # The ID of the management node.
        # 
        # > You can call the [ListHoneypotNode](~~ListHoneypotNode~~) operation to query the IDs of management nodes.
        # 
        # This parameter is required.
        self.control_node_id = control_node_id
        # The name of the probe.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The configuration of the probe.
        self.honeypot_bind_list = honeypot_bind_list
        # Specifies whether to enable ping scan. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.ping = ping
        # The type of the probe. Valid values:
        # 
        # *   **host_probe**: host probe
        # *   **vpc_black_hole_probe**: virtual private cloud (VPC) probe
        # 
        # This parameter is required.
        self.probe_type = probe_type
        # The version of the probe.
        self.probe_version = probe_version
        # The IP address of the proxy.
        self.proxy_ip = proxy_ip
        # The UUID of the instance.
        # 
        # > If **ProbeType** is set to **host_probe**, this parameter is required.
        self.uuid = uuid
        # The ID of the VPC.
        # 
        # > If **ProbeType** is set to **vpc_black_hole_probe**, this parameter is required. You can call the [DescribeVpcHoneyPotList](~~DescribeVpcHoneyPotList~~) operation to query the IDs of VPCs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.honeypot_bind_list:
            for v1 in self.honeypot_bind_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arp is not None:
            result['Arp'] = self.arp

        if self.business_group_id is not None:
            result['BusinessGroupId'] = self.business_group_id

        if self.control_node_id is not None:
            result['ControlNodeId'] = self.control_node_id

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        result['HoneypotBindList'] = []
        if self.honeypot_bind_list is not None:
            for k1 in self.honeypot_bind_list:
                result['HoneypotBindList'].append(k1.to_map() if k1 else None)

        if self.ping is not None:
            result['Ping'] = self.ping

        if self.probe_type is not None:
            result['ProbeType'] = self.probe_type

        if self.probe_version is not None:
            result['ProbeVersion'] = self.probe_version

        if self.proxy_ip is not None:
            result['ProxyIp'] = self.proxy_ip

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arp') is not None:
            self.arp = m.get('Arp')

        if m.get('BusinessGroupId') is not None:
            self.business_group_id = m.get('BusinessGroupId')

        if m.get('ControlNodeId') is not None:
            self.control_node_id = m.get('ControlNodeId')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        self.honeypot_bind_list = []
        if m.get('HoneypotBindList') is not None:
            for k1 in m.get('HoneypotBindList'):
                temp_model = main_models.CreateHoneypotProbeRequestHoneypotBindList()
                self.honeypot_bind_list.append(temp_model.from_map(k1))

        if m.get('Ping') is not None:
            self.ping = m.get('Ping')

        if m.get('ProbeType') is not None:
            self.probe_type = m.get('ProbeType')

        if m.get('ProbeVersion') is not None:
            self.probe_version = m.get('ProbeVersion')

        if m.get('ProxyIp') is not None:
            self.proxy_ip = m.get('ProxyIp')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateHoneypotProbeRequestHoneypotBindList(DaraModel):
    def __init__(
        self,
        bind_port_list: List[main_models.CreateHoneypotProbeRequestHoneypotBindListBindPortList] = None,
        honeypot_id: str = None,
    ):
        # The listener ports.
        self.bind_port_list = bind_port_list
        # The ID of the honeypot.
        # 
        # > You can call the [ListHoneypot](~~ListHoneypot~~) operation to query the IDs of honeypots.
        self.honeypot_id = honeypot_id

    def validate(self):
        if self.bind_port_list:
            for v1 in self.bind_port_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BindPortList'] = []
        if self.bind_port_list is not None:
            for k1 in self.bind_port_list:
                result['BindPortList'].append(k1.to_map() if k1 else None)

        if self.honeypot_id is not None:
            result['HoneypotId'] = self.honeypot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bind_port_list = []
        if m.get('BindPortList') is not None:
            for k1 in m.get('BindPortList'):
                temp_model = main_models.CreateHoneypotProbeRequestHoneypotBindListBindPortList()
                self.bind_port_list.append(temp_model.from_map(k1))

        if m.get('HoneypotId') is not None:
            self.honeypot_id = m.get('HoneypotId')

        return self

class CreateHoneypotProbeRequestHoneypotBindListBindPortList(DaraModel):
    def __init__(
        self,
        bind_port: bool = None,
        end_port: int = None,
        fixed: bool = None,
        start_port: int = None,
        target_port: int = None,
    ):
        # Specifies whether to bind a port. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.bind_port = bind_port
        # The end of the port range.
        self.end_port = end_port
        # Specifies whether the port is a fixed port. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.fixed = fixed
        # The start of the port range.
        self.start_port = start_port
        # The destination port.
        # 
        # > If **HoneypotId** is specified, this parameter is required.
        self.target_port = target_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_port is not None:
            result['BindPort'] = self.bind_port

        if self.end_port is not None:
            result['EndPort'] = self.end_port

        if self.fixed is not None:
            result['Fixed'] = self.fixed

        if self.start_port is not None:
            result['StartPort'] = self.start_port

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindPort') is not None:
            self.bind_port = m.get('BindPort')

        if m.get('EndPort') is not None:
            self.end_port = m.get('EndPort')

        if m.get('Fixed') is not None:
            self.fixed = m.get('Fixed')

        if m.get('StartPort') is not None:
            self.start_port = m.get('StartPort')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        return self

