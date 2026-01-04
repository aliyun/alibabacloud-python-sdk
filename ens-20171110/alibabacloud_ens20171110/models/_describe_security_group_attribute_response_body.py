# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityGroupAttributeResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        permissions: main_models.DescribeSecurityGroupAttributeResponseBodyPermissions = None,
        request_id: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
    ):
        # The description of the security group.
        self.description = description
        # Details about the rules.
        self.permissions = permissions
        # The request ID.
        self.request_id = request_id
        # The ID of the destination security group.
        self.security_group_id = security_group_id
        # The name of the destination security group.
        self.security_group_name = security_group_name

    def validate(self):
        if self.permissions:
            self.permissions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.permissions is not None:
            result['Permissions'] = self.permissions.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Permissions') is not None:
            temp_model = main_models.DescribeSecurityGroupAttributeResponseBodyPermissions()
            self.permissions = temp_model.from_map(m.get('Permissions'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

class DescribeSecurityGroupAttributeResponseBodyPermissions(DaraModel):
    def __init__(
        self,
        permission: List[main_models.DescribeSecurityGroupAttributeResponseBodyPermissionsPermission] = None,
    ):
        self.permission = permission

    def validate(self):
        if self.permission:
            for v1 in self.permission:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Permission'] = []
        if self.permission is not None:
            for k1 in self.permission:
                result['Permission'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.permission = []
        if m.get('Permission') is not None:
            for k1 in m.get('Permission'):
                temp_model = main_models.DescribeSecurityGroupAttributeResponseBodyPermissionsPermission()
                self.permission.append(temp_model.from_map(k1))

        return self

class DescribeSecurityGroupAttributeResponseBodyPermissionsPermission(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
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
        # The time at which the security group rule was created. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description.
        self.description = description
        # The range of destination IP addresses for outbound access control.
        self.dest_cidr_ip = dest_cidr_ip
        # The direction in which the security group rule is applied.
        self.direction = direction
        # The transport layer protocol.
        self.ip_protocol = ip_protocol
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The policy.
        self.policy = policy
        # The source port range.
        self.port_range = port_range
        # The priority of the rule.
        self.priority = priority
        # The range of source IP addresses for inbound access control.
        self.source_cidr_ip = source_cidr_ip
        # The source port number range for the security group.
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

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
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

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

