# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class AuthorizeRCSecurityGroupPermissionRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        region_id: str = None,
        security_group_id: str = None,
        security_group_permissions: List[main_models.AuthorizeRCSecurityGroupPermissionRequestSecurityGroupPermissions] = None,
    ):
        # The direction of the rule. Valid values:
        # 
        # *   **ingress**: the inbound security group rule.
        # *   **egress**: the outbound security group rule.
        self.direction = direction
        # The region ID.
        self.region_id = region_id
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The information about the security group.
        self.security_group_permissions = security_group_permissions

    def validate(self):
        if self.security_group_permissions:
            for v1 in self.security_group_permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        result['SecurityGroupPermissions'] = []
        if self.security_group_permissions is not None:
            for k1 in self.security_group_permissions:
                result['SecurityGroupPermissions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        self.security_group_permissions = []
        if m.get('SecurityGroupPermissions') is not None:
            for k1 in m.get('SecurityGroupPermissions'):
                temp_model = main_models.AuthorizeRCSecurityGroupPermissionRequestSecurityGroupPermissions()
                self.security_group_permissions.append(temp_model.from_map(k1))

        return self

class AuthorizeRCSecurityGroupPermissionRequestSecurityGroupPermissions(DaraModel):
    def __init__(
        self,
        dest_cidr_ip: str = None,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: int = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        # The destination CIDR block for outbound access control. CIDR blocks and IPv4 addresses are supported.
        self.dest_cidr_ip = dest_cidr_ip
        # The protocol type supported by the rule. The value is not case-sensitive. Valid values:
        # 
        # *   **ICMP**
        # *   **GRE**
        # *   **TCP**
        # *   **UDP**
        # *   **ALL**: All protocols are supported.
        self.ip_protocol = ip_protocol
        # The action that you want to specify in the rule.
        self.policy = policy
        # The range of destination ports that correspond to the transport layer protocol of the destination security group. Valid values:
        # 
        # *   The value is in the X/Y format when IpProtocol is set to TCP or UDP. X specifies the start port number and Y specifies the end port number. X and Y range from **1** to **65535**. The start port number and the end port number are separated by a forward slash (/). Correct example: **1/200**. Incorrect example: **200/1**.
        # *   Valid value when IpProtocol is set to ICMP: **-1/-1**.
        # *   Valid value when IpProtocol is set to GRE: **-1/-1**.
        # *   Valid value when IpProtocol is set to ALL: **-1/-1**.
        self.port_range = port_range
        # The priority of the rule. Valid values: 1 to 100. A smaller value indicates a higher priority. When multiple security group rules have the same priority, drop rules take precedence.
        self.priority = priority
        # The source CIDR block for inbound access control. CIDR blocks and IPv4 addresses are supported.
        self.source_cidr_ip = source_cidr_ip
        # The range of port numbers that correspond to the transport layer protocol for the source security group. Valid values:
        # 
        # *   The value is in the X/Y format when IpProtocol is set to TCP or UDP. X specifies the start port number and Y specifies the end port number. X and Y range from **1** to **65535**. The start port number and the end port number are separated by a forward slash (/). Correct example: **1/200**. Incorrect example: **200/1**.
        # *   Valid value when IpProtocol is set to ICMP: **-1/-1**.
        # *   Valid value when IpProtocol is set to GRE: **-1/-1**.
        # *   Valid value when IpProtocol is set to ALL: **-1/-1**.
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

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
        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

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

