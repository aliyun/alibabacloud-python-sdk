# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceSecurityGroupRuleRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        description: str = None,
        ip_protocol: str = None,
        owner_account: str = None,
        owner_id: str = None,
        port_range: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_rule_id: str = None,
        source_cidr_ip: str = None,
    ):
        # The ID of the instance. You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/2628785.html) operation to query the IDs of instances.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The description of the security group rule.
        # 
        # This parameter is required.
        self.description = description
        # The type of the transport layer protocol. Valid values:
        # 
        # *   TCP
        # *   UDP
        # 
        # This parameter is required.
        self.ip_protocol = ip_protocol
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The range of destination ports over which TCP and UDP traffic is allowed in the security group rule.
        # 
        # Valid values: 1 to 65535. Separate the start port number and the end port number with a forward slash (/). Example: 1/200.
        # 
        # This parameter is required.
        self.port_range = port_range
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the security group rule. You can call the [DescribeDBInstanceSecurityGroupRule](https://help.aliyun.com/document_detail/2834044.html) to obtain the ID of the security group rule.
        # 
        # This parameter is required.
        self.security_group_rule_id = security_group_rule_id
        # The range of source IP addresses. CIDR blocks and IPv4 addresses are supported.
        # 
        # This parameter is required.
        self.source_cidr_ip = source_cidr_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.description is not None:
            result['Description'] = self.description

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_group_rule_id is not None:
            result['SecurityGroupRuleId'] = self.security_group_rule_id

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityGroupRuleId') is not None:
            self.security_group_rule_id = m.get('SecurityGroupRuleId')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        return self

