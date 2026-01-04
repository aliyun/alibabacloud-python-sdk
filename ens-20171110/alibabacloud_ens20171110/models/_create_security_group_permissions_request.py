# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateSecurityGroupPermissionsRequest(DaraModel):
    def __init__(
        self,
        permissions: List[main_models.CreateSecurityGroupPermissionsRequestPermissions] = None,
        security_group_id: str = None,
    ):
        # The security group rules.
        # 
        # This parameter is required.
        self.permissions = permissions
        # The IDs of the security groups.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id

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
        result['Permissions'] = []
        if self.permissions is not None:
            for k1 in self.permissions:
                result['Permissions'].append(k1.to_map() if k1 else None)

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.permissions = []
        if m.get('Permissions') is not None:
            for k1 in m.get('Permissions'):
                temp_model = main_models.CreateSecurityGroupPermissionsRequestPermissions()
                self.permissions.append(temp_model.from_map(k1))

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

class CreateSecurityGroupPermissionsRequestPermissions(DaraModel):
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
        # The description of the storage gateway. It must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The destination IPv4 CIDR block. CIDR blocks and IPv4 addresses are supported.
        self.dest_cidr_ip = dest_cidr_ip
        # The direction in which the security group rule is applied.
        # 
        # *   egress
        # *   ingress
        # 
        # This parameter is required.
        self.direction = direction
        # Protocol type. Valid values:
        # 
        # *   TCP
        # *   UDP
        # *   ICMP: the ICMP protocol
        # *   ICMPv6: the ICMP protocol for IPv6.
        # *   ALL: All protocols are supported.
        # 
        # This parameter is required.
        self.ip_protocol = ip_protocol
        # The destination IPv6 CIDR block. IPv6 CIDR blocks and IPv6 addresses are supported.
        # 
        # >  This parameter and the `DestCidrIp` parameter cannot be set at the same time.
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        # The source IPv6 CIDR block of the security group rule. or IPv6 address.
        # 
        # >  This parameter and the `DestCidrIp` parameter cannot be set at the same time.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The action specified in the security group rule. Valid values:
        # 
        # *   Accept
        # *   Drop
        # 
        # This parameter is required.
        self.policy = policy
        # The destination port range of the security group rule. Valid values:
        # 
        # *   If you set IpProtocol to TCP or UDP, the valid values of this parameter are 1 to 65535. Specify a port range in the format of \\<Start port number>/\\<End port number>. Example: 1/200.
        # *   If you set IpProtocol to ICMP, the port range is -1/-1.
        # *   ICMPv6:-1/-1.
        # *   If you set IpProtocol to ALL, the port number range is -1/-1.
        # 
        # This parameter is required.
        self.port_range = port_range
        # The priority of the security group rule. A smaller value specifies a higher priority. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.priority = priority
        # The source IPv4 CIDR block. CIDR blocks and IPv4 addresses are supported.
        self.source_cidr_ip = source_cidr_ip
        # The range of source port numbers for the protocols specified in the security group rule. Valid values:
        # 
        # *   If you set IpProtocol to TCP or UDP, the valid values of this parameter are 1 to 65535. Specify a port range in the format of \\<Start port number>/\\<End port number>. Example: 1/200.
        # *   If you set IpProtocol to ICMP, the port range is -1/-1.
        # *   ICMPv6:-1/-1.
        # *   If you set IpProtocol to ALL, the port range is -1/-1.
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

