# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class AttachToPolicyRequest(DaraModel):
    def __init__(
        self,
        ip_port_protocol_list: List[main_models.AttachToPolicyRequestIpPortProtocolList] = None,
        policy_id: str = None,
        port_version: str = None,
    ):
        # The list of protection objects.
        # 
        # This parameter is required.
        self.ip_port_protocol_list = ip_port_protocol_list
        # The policy ID.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The version of the port-specific mitigation policy. Valid values:
        # 
        # - **Not specified**: Binds the default surf protection engine policy.
        # - **2**: Binds the new stream protection engine policy.
        # > Only port-specific mitigation policies support this parameter.
        self.port_version = port_version

    def validate(self):
        if self.ip_port_protocol_list:
            for v1 in self.ip_port_protocol_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpPortProtocolList'] = []
        if self.ip_port_protocol_list is not None:
            for k1 in self.ip_port_protocol_list:
                result['IpPortProtocolList'].append(k1.to_map() if k1 else None)

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.port_version is not None:
            result['PortVersion'] = self.port_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_port_protocol_list = []
        if m.get('IpPortProtocolList') is not None:
            for k1 in m.get('IpPortProtocolList'):
                temp_model = main_models.AttachToPolicyRequestIpPortProtocolList()
                self.ip_port_protocol_list.append(temp_model.from_map(k1))

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PortVersion') is not None:
            self.port_version = m.get('PortVersion')

        return self

class AttachToPolicyRequestIpPortProtocolList(DaraModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
        port_range: str = None,
        protocol: str = None,
    ):
        # The IP address of the protection object.
        # > Prerequisite: The IP address must be added to the Anti-DDoS Origin instance by calling the AddIp operation in advance, and you must call the DescribeInstanceList operation to verify that the IP address has been added to the Anti-DDoS Origin instance.
        # 
        # This parameter is required.
        self.ip = ip
        # The port number of the protection object.
        # > Only port-specific mitigation policies support this parameter.
        self.port = port
        # The port range of the protection object.
        # > Only port-specific mitigation policies support this parameter.
        self.port_range = port_range
        # The protocol type of the protection object. Valid values:
        # 
        # - **tcp**: Transmission Control Protocol.
        # - **udp**: User Datagram Protocol.
        # > Only port-specific mitigation policies support this parameter.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.port is not None:
            result['Port'] = self.port

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

