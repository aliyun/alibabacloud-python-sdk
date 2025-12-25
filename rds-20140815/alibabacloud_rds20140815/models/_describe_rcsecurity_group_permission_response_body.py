# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCSecurityGroupPermissionResponseBody(DaraModel):
    def __init__(
        self,
        inner_access_policy: str = None,
        region_id: str = None,
        request_id: str = None,
        security_group_id: str = None,
        security_group_permissions: List[main_models.DescribeRCSecurityGroupPermissionResponseBodySecurityGroupPermissions] = None,
        vpc_id: str = None,
    ):
        self.inner_access_policy = inner_access_policy
        self.region_id = region_id
        self.request_id = request_id
        self.security_group_id = security_group_id
        self.security_group_permissions = security_group_permissions
        self.vpc_id = vpc_id

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
        if self.inner_access_policy is not None:
            result['InnerAccessPolicy'] = self.inner_access_policy

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        result['SecurityGroupPermissions'] = []
        if self.security_group_permissions is not None:
            for k1 in self.security_group_permissions:
                result['SecurityGroupPermissions'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InnerAccessPolicy') is not None:
            self.inner_access_policy = m.get('InnerAccessPolicy')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        self.security_group_permissions = []
        if m.get('SecurityGroupPermissions') is not None:
            for k1 in m.get('SecurityGroupPermissions'):
                temp_model = main_models.DescribeRCSecurityGroupPermissionResponseBodySecurityGroupPermissions()
                self.security_group_permissions.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeRCSecurityGroupPermissionResponseBodySecurityGroupPermissions(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        dest_cidr_ip: str = None,
        direction: str = None,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: str = None,
        security_group_rule_id: str = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        self.create_time = create_time
        self.dest_cidr_ip = dest_cidr_ip
        self.direction = direction
        self.ip_protocol = ip_protocol
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.security_group_rule_id = security_group_rule_id
        self.source_cidr_ip = source_cidr_ip
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.security_group_rule_id is not None:
            result['SecurityGroupRuleId'] = self.security_group_rule_id

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('SecurityGroupRuleId') is not None:
            self.security_group_rule_id = m.get('SecurityGroupRuleId')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        return self

