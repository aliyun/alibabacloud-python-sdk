# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateSecurityGroupRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        permissions: List[main_models.CreateSecurityGroupRequestPermissions] = None,
        security_group_name: str = None,
    ):
        # The description of the security group. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with `http://` or `https://`.
        self.description = description
        # The rules of the security group. Valid values of N: 0 to 200.
        self.permissions = permissions
        # The name of the security group. The name must be 2 to 128 characters in length, and can contain digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`. By default, this parameter is empty.
        self.security_group_name = security_group_name

    def validate(self):
        if self.permissions:
            for v1 in self.permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        result['Permissions'] = []
        if self.permissions is not None:
            for k1 in self.permissions:
                result['Permissions'].append(k1.to_map() if k1 else None)

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.permissions = []
        if m.get('Permissions') is not None:
            for k1 in m.get('Permissions'):
                temp_model = main_models.CreateSecurityGroupRequestPermissions()
                self.permissions.append(temp_model.from_map(k1))

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

class CreateSecurityGroupRequestPermissions(DaraModel):
    def __init__(
        self,
        description: str = None,
        dest_cidr_ip: str = None,
        direction: str = None,
        ip_protocol: str = None,
        ipv_6dest_cidr_ip: str = None,
        ipv_6source_cidr_ip: str = None,
        policy: str = None,
        port_range: str = None,
        priority: int = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        # The description of the security group rule. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The destination IPv4 CIDR block. CIDR blocks and IPv4 addresses are supported.
        self.dest_cidr_ip = dest_cidr_ip
        # The direction of the security group rule. Valid values:
        # 
        # - egress: outbound
        # 
        # - ingress: inbound
        # 
        # This parameter is required.
        self.direction = direction
        # The transport layer protocol. Valid values:
        # 
        # - TCP
        # 
        # - UDP
        # 
        # - ICMP
        # 
        # - ALL
        # 
        # This parameter is required.
        self.ip_protocol = ip_protocol
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The policy of the security group rule. Valid values:
        # 
        # - Accept: allows access.
        # 
        # - Drop: denies access.
        # 
        # This parameter is required.
        self.policy = policy
        # The range of the destination ports for the security group rule. Valid values:
        # 
        # - If you set the IpProtocol to TCP or UDP, the port range is 1 to 65535. You must use a forward slash (/) to separate the start port and the end port, for example, 1/200.
        # 
        # - If you set the IpProtocol to ICMP, the port range is -1/-1.
        # 
        # - If you set the IpProtocol to ALL, the port range is -1/-1.
        # 
        # This parameter is required.
        self.port_range = port_range
        # The priority of the security group rule. A smaller value indicates a higher priority. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.priority = priority
        # The source IPv4 CIDR block. CIDR blocks and IPv4 addresses are supported.
        self.source_cidr_ip = source_cidr_ip
        # The range of the source ports for the security group rule. Valid values:
        # 
        # - If you set the IpProtocol to TCP or UDP, the port range is 1 to 65535. You must use a forward slash (/) to separate the start port and the end port, for example, 1/200.
        # 
        # - If you set the IpProtocol to ICMP, the port range is -1/-1.
        # 
        # - If you set the IpProtocol to ALL, the port range is -1/-1.
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.ipv_6dest_cidr_ip is not None:
            result['Ipv6DestCidrIp'] = self.ipv_6dest_cidr_ip

        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Ipv6DestCidrIp') is not None:
            self.ipv_6dest_cidr_ip = m.get('Ipv6DestCidrIp')

        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        return self

