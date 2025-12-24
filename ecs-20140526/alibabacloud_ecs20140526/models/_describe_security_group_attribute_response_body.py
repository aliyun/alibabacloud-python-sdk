# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityGroupAttributeResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        inner_access_policy: str = None,
        next_token: str = None,
        permissions: main_models.DescribeSecurityGroupAttributeResponseBodyPermissions = None,
        region_id: str = None,
        request_id: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
        snapshot_policy_ids: main_models.DescribeSecurityGroupAttributeResponseBodySnapshotPolicyIds = None,
        vpc_id: str = None,
    ):
        # The description of the security group.
        self.description = description
        # The access control policy of the security group. Valid values:
        # 
        # *   Accept: All instances in the security group can communicate with each other.
        # *   Drop: All instances in the security group are isolated from each other.
        self.inner_access_policy = inner_access_policy
        # A pagination token. It can be used in the next request to retrieve a new page of results. If the return value of this parameter is empty when you specify `MaxResults` and `NextToken` for a paged query, no more results are to be returned.
        self.next_token = next_token
        # Details about the security group rules.
        self.permissions = permissions
        # The ID of the region.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The name of the security group.
        self.security_group_name = security_group_name
        self.snapshot_policy_ids = snapshot_policy_ids
        # The ID of the VPC. If a VPC ID is returned, the network type of the security group is VPC. If no VPC ID is returned, the network type of the security group is classic network.
        self.vpc_id = vpc_id

    def validate(self):
        if self.permissions:
            self.permissions.validate()
        if self.snapshot_policy_ids:
            self.snapshot_policy_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.inner_access_policy is not None:
            result['InnerAccessPolicy'] = self.inner_access_policy

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.permissions is not None:
            result['Permissions'] = self.permissions.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        if self.snapshot_policy_ids is not None:
            result['SnapshotPolicyIds'] = self.snapshot_policy_ids.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InnerAccessPolicy') is not None:
            self.inner_access_policy = m.get('InnerAccessPolicy')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Permissions') is not None:
            temp_model = main_models.DescribeSecurityGroupAttributeResponseBodyPermissions()
            self.permissions = temp_model.from_map(m.get('Permissions'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        if m.get('SnapshotPolicyIds') is not None:
            temp_model = main_models.DescribeSecurityGroupAttributeResponseBodySnapshotPolicyIds()
            self.snapshot_policy_ids = temp_model.from_map(m.get('SnapshotPolicyIds'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeSecurityGroupAttributeResponseBodySnapshotPolicyIds(DaraModel):
    def __init__(
        self,
        snapshot_policy_id: List[str] = None,
    ):
        self.snapshot_policy_id = snapshot_policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.snapshot_policy_id is not None:
            result['SnapshotPolicyId'] = self.snapshot_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnapshotPolicyId') is not None:
            self.snapshot_policy_id = m.get('SnapshotPolicyId')

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
        create_time: str = None,
        description: str = None,
        dest_cidr_ip: str = None,
        dest_group_id: str = None,
        dest_group_name: str = None,
        dest_group_owner_account: str = None,
        dest_prefix_list_id: str = None,
        dest_prefix_list_name: str = None,
        direction: str = None,
        ip_protocol: str = None,
        ipv_6dest_cidr_ip: str = None,
        ipv_6source_cidr_ip: str = None,
        nic_type: str = None,
        policy: str = None,
        port_range: str = None,
        port_range_list_id: str = None,
        port_range_list_name: str = None,
        priority: str = None,
        security_group_rule_id: str = None,
        source_cidr_ip: str = None,
        source_group_id: str = None,
        source_group_name: str = None,
        source_group_owner_account: str = None,
        source_port_range: str = None,
        source_prefix_list_id: str = None,
        source_prefix_list_name: str = None,
    ):
        # The time when the security group rule was created. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the security group.
        self.description = description
        # The destination CIDR block for outbound access control.
        self.dest_cidr_ip = dest_cidr_ip
        # The ID of the destination security group for outbound access control.
        self.dest_group_id = dest_group_id
        # The name of the destination security group.
        self.dest_group_name = dest_group_name
        # The ID of the Alibaba Cloud account to which the destination security group belongs.
        self.dest_group_owner_account = dest_group_owner_account
        # The ID of the destination prefix list for outbound access control.
        self.dest_prefix_list_id = dest_prefix_list_id
        # The name of the destination prefix list.
        self.dest_prefix_list_name = dest_prefix_list_name
        # The direction in which the security group rule is applied.
        self.direction = direction
        # The transport layer protocol.
        self.ip_protocol = ip_protocol
        # The destination IPv6 CIDR block.
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        # The source IPv6 CIDR block.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The network type.
        self.nic_type = nic_type
        # The access control policy.
        self.policy = policy
        # The port range.
        self.port_range = port_range
        # The ID of the port list.
        self.port_range_list_id = port_range_list_id
        # The name of the port list.
        self.port_range_list_name = port_range_list_name
        # The priority of the rule.
        self.priority = priority
        # The ID of the security group rule.
        self.security_group_rule_id = security_group_rule_id
        # The source CIDR block for inbound access control.
        self.source_cidr_ip = source_cidr_ip
        # The source security group for inbound access control.
        self.source_group_id = source_group_id
        # The name of the source security group.
        self.source_group_name = source_group_name
        # The ID of the Alibaba Cloud account to which the source security group belongs.
        self.source_group_owner_account = source_group_owner_account
        # The source port range.
        self.source_port_range = source_port_range
        # The ID of the source prefix list for inbound access control.
        self.source_prefix_list_id = source_prefix_list_id
        # The name of the source prefix list.
        self.source_prefix_list_name = source_prefix_list_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip

        if self.dest_group_id is not None:
            result['DestGroupId'] = self.dest_group_id

        if self.dest_group_name is not None:
            result['DestGroupName'] = self.dest_group_name

        if self.dest_group_owner_account is not None:
            result['DestGroupOwnerAccount'] = self.dest_group_owner_account

        if self.dest_prefix_list_id is not None:
            result['DestPrefixListId'] = self.dest_prefix_list_id

        if self.dest_prefix_list_name is not None:
            result['DestPrefixListName'] = self.dest_prefix_list_name

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.ipv_6dest_cidr_ip is not None:
            result['Ipv6DestCidrIp'] = self.ipv_6dest_cidr_ip

        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip

        if self.nic_type is not None:
            result['NicType'] = self.nic_type

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.port_range_list_id is not None:
            result['PortRangeListId'] = self.port_range_list_id

        if self.port_range_list_name is not None:
            result['PortRangeListName'] = self.port_range_list_name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.security_group_rule_id is not None:
            result['SecurityGroupRuleId'] = self.security_group_rule_id

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        if self.source_group_id is not None:
            result['SourceGroupId'] = self.source_group_id

        if self.source_group_name is not None:
            result['SourceGroupName'] = self.source_group_name

        if self.source_group_owner_account is not None:
            result['SourceGroupOwnerAccount'] = self.source_group_owner_account

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        if self.source_prefix_list_id is not None:
            result['SourcePrefixListId'] = self.source_prefix_list_id

        if self.source_prefix_list_name is not None:
            result['SourcePrefixListName'] = self.source_prefix_list_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')

        if m.get('DestGroupId') is not None:
            self.dest_group_id = m.get('DestGroupId')

        if m.get('DestGroupName') is not None:
            self.dest_group_name = m.get('DestGroupName')

        if m.get('DestGroupOwnerAccount') is not None:
            self.dest_group_owner_account = m.get('DestGroupOwnerAccount')

        if m.get('DestPrefixListId') is not None:
            self.dest_prefix_list_id = m.get('DestPrefixListId')

        if m.get('DestPrefixListName') is not None:
            self.dest_prefix_list_name = m.get('DestPrefixListName')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Ipv6DestCidrIp') is not None:
            self.ipv_6dest_cidr_ip = m.get('Ipv6DestCidrIp')

        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')

        if m.get('NicType') is not None:
            self.nic_type = m.get('NicType')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('PortRangeListId') is not None:
            self.port_range_list_id = m.get('PortRangeListId')

        if m.get('PortRangeListName') is not None:
            self.port_range_list_name = m.get('PortRangeListName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('SecurityGroupRuleId') is not None:
            self.security_group_rule_id = m.get('SecurityGroupRuleId')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        if m.get('SourceGroupId') is not None:
            self.source_group_id = m.get('SourceGroupId')

        if m.get('SourceGroupName') is not None:
            self.source_group_name = m.get('SourceGroupName')

        if m.get('SourceGroupOwnerAccount') is not None:
            self.source_group_owner_account = m.get('SourceGroupOwnerAccount')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        if m.get('SourcePrefixListId') is not None:
            self.source_prefix_list_id = m.get('SourcePrefixListId')

        if m.get('SourcePrefixListName') is not None:
            self.source_prefix_list_name = m.get('SourcePrefixListName')

        return self

