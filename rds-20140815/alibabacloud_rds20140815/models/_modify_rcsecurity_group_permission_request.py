# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRCSecurityGroupPermissionRequest(DaraModel):
    def __init__(
        self,
        dest_cidr_ip: str = None,
        direction: str = None,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: str = None,
        region_id: str = None,
        security_group_id: str = None,
        security_group_rule_id: str = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        self.dest_cidr_ip = dest_cidr_ip
        self.direction = direction
        self.ip_protocol = ip_protocol
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.region_id = region_id
        self.security_group_id = security_group_id
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_rule_id is not None:
            result['SecurityGroupRuleId'] = self.security_group_rule_id

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupRuleId') is not None:
            self.security_group_rule_id = m.get('SecurityGroupRuleId')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        return self

