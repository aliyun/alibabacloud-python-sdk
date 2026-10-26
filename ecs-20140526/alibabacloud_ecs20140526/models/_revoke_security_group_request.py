# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class RevokeSecurityGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dest_cidr_ip: str = None,
        ip_protocol: str = None,
        ipv_6dest_cidr_ip: str = None,
        ipv_6source_cidr_ip: str = None,
        nic_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        permissions: List[main_models.RevokeSecurityGroupRequestPermissions] = None,
        policy: str = None,
        port_range: str = None,
        priority: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        security_group_rule_id: List[str] = None,
        source_cidr_ip: str = None,
        source_group_id: str = None,
        source_group_owner_account: str = None,
        source_group_owner_id: int = None,
        source_port_range: str = None,
        source_prefix_list_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # **[Deprecated]** Use `Permissions.N.Description` to specify the description of the rule.
        self.description = description
        # **[Deprecated]** Use `Permissions.N.DestCidrIp` to specify the destination IPv4 CIDR block.
        self.dest_cidr_ip = dest_cidr_ip
        # **[Deprecated]** Use `Permissions.N.IpProtocol` to specify the protocol type.
        self.ip_protocol = ip_protocol
        # **[Deprecated]** Use `Permissions.N.Ipv6DestCidrIp` to specify the destination IPv6 CIDR block.
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        # **[Deprecated]** Use `Permissions.N.Ipv6SourceCidrIp` to specify the source IPv6 Classless Inter-Domain Routing.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # **[Deprecated]** Use `Permissions.N.NicType` to specify the NIC type.
        self.nic_type = nic_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The array of security group rules. Array length: 0 to 100.
        self.permissions = permissions
        # **[Deprecated]** Use `Permissions.N.Policy` for the Settings of access permissions.
        self.policy = policy
        # **[Deprecated]** Use `Permissions.N.PortRange` to specify the port range.
        self.port_range = port_range
        # **[Deprecated]** Use `Permissions.N.Priority` to specify the rule priority.
        self.priority = priority
        # The region ID of the security group. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The security group ID.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The array of security group rule IDs. Array length: 0 to 100.
        self.security_group_rule_id = security_group_rule_id
        # **[Deprecated]** Use `Permissions.N.SourceCidrIp` to specify the source IPv4 Classless Inter-Domain Routing.
        self.source_cidr_ip = source_cidr_ip
        # **[Deprecated]** Use `Permissions.N.SourceGroupId` to specify the source security group ID.
        self.source_group_id = source_group_id
        # **[Deprecated]** Use `Permissions.N.SourceGroupOwnerAccount` to specify the Alibaba Cloud account to which the source security group belongs.
        self.source_group_owner_account = source_group_owner_account
        # **[Deprecated]** Use `Permissions.N.SourceGroupOwnerId` to specify the ID of the Alibaba Cloud account to which the source security group belongs.
        self.source_group_owner_id = source_group_owner_id
        # **[Deprecated]** Use `Permissions.N.SourcePortRange` to specify the source port range.
        self.source_port_range = source_port_range
        # **[Deprecated]** Use `Permissions.N.SourcePrefixListId` to specify the source prefix list ID.
        self.source_prefix_list_id = source_prefix_list_id

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.ipv_6dest_cidr_ip is not None:
            result['Ipv6DestCidrIp'] = self.ipv_6dest_cidr_ip

        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip

        if self.nic_type is not None:
            result['NicType'] = self.nic_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        result['Permissions'] = []
        if self.permissions is not None:
            for k1 in self.permissions:
                result['Permissions'].append(k1.to_map() if k1 else None)

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_rule_id is not None:
            result['SecurityGroupRuleId'] = self.security_group_rule_id

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        if self.source_group_id is not None:
            result['SourceGroupId'] = self.source_group_id

        if self.source_group_owner_account is not None:
            result['SourceGroupOwnerAccount'] = self.source_group_owner_account

        if self.source_group_owner_id is not None:
            result['SourceGroupOwnerId'] = self.source_group_owner_id

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        if self.source_prefix_list_id is not None:
            result['SourcePrefixListId'] = self.source_prefix_list_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Ipv6DestCidrIp') is not None:
            self.ipv_6dest_cidr_ip = m.get('Ipv6DestCidrIp')

        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')

        if m.get('NicType') is not None:
            self.nic_type = m.get('NicType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        self.permissions = []
        if m.get('Permissions') is not None:
            for k1 in m.get('Permissions'):
                temp_model = main_models.RevokeSecurityGroupRequestPermissions()
                self.permissions.append(temp_model.from_map(k1))

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupRuleId') is not None:
            self.security_group_rule_id = m.get('SecurityGroupRuleId')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        if m.get('SourceGroupId') is not None:
            self.source_group_id = m.get('SourceGroupId')

        if m.get('SourceGroupOwnerAccount') is not None:
            self.source_group_owner_account = m.get('SourceGroupOwnerAccount')

        if m.get('SourceGroupOwnerId') is not None:
            self.source_group_owner_id = m.get('SourceGroupOwnerId')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        if m.get('SourcePrefixListId') is not None:
            self.source_prefix_list_id = m.get('SourcePrefixListId')

        return self

class RevokeSecurityGroupRequestPermissions(DaraModel):
    def __init__(
        self,
        description: str = None,
        dest_cidr_ip: str = None,
        ip_protocol: str = None,
        ipv_6dest_cidr_ip: str = None,
        ipv_6source_cidr_ip: str = None,
        nic_type: str = None,
        policy: str = None,
        port_range: str = None,
        port_range_list_id: str = None,
        priority: str = None,
        source_cidr_ip: str = None,
        source_group_id: str = None,
        source_group_owner_account: str = None,
        source_group_owner_id: int = None,
        source_port_range: str = None,
        source_prefix_list_id: str = None,
    ):
        # The description of the security group rule. The description must be 1 to 512 characters in length.
        self.description = description
        # The destination IPv4 CIDR block. CIDR blocks and IPv4 address ranges are supported.
        # 
        # This parameter is used to support quintuple rules. For more information, see [Quintuple rules for security groups](https://help.aliyun.com/document_detail/97439.html).
        self.dest_cidr_ip = dest_cidr_ip
        # The protocol type. The value is not case-sensitive. Valid values: 
        #          
        # - TCP.
        # - UDP.
        # - ICMP.
        # - ICMPv6.
        # - GRE.
        # - ALL: all protocols.
        self.ip_protocol = ip_protocol
        # The destination IPv6 CIDR block. CIDR blocks and IPv6 address ranges are supported. 
        # 
        # This parameter is used to support quintuple rules. For more information, see [Quintuple rules for security groups](https://help.aliyun.com/document_detail/97439.html).
        # 
        #          
        # > This parameter is valid only for VPC-type ECS instances that support IPv6. You cannot specify both this parameter and the `DestCidrIp` parameter at the same time.
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        # The source IPv6 Classless Inter-Domain Routing from which you want to revoke access permissions. CIDR format and IPv6 format IP address ranges are supported.
        # 
        # 
        # > This parameter is valid only for VPC-type ECS instances that support IPv6. Settings for this parameter and the `SourceCidrIp` parameter cannot be applied at the same time.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The network interface controller (NIC) type of the security group rule. You do not need to specify the network interface controller (NIC) type for security group rules in a VPC. The default value is intranet, and only intranet is supported.
        # 
        # > The classic network feature has been taken offline. For details, see [Offline notice](https://help.aliyun.com/document_detail/2833134.html). The network interface controller (NIC) type for classic network security group rules. Valid values:
        # > - internet: public network interface controller (NIC).
        # > - intranet: internal network interface controller (NIC).
        self.nic_type = nic_type
        # The access permissions. Valid values: 
        #          
        # - accept: allows access.
        # - drop: deny access without returning a rejection message. The initiator receives a message indicating that the request timeout or the connection failed.
        # 
        # Default value: accept.
        self.policy = policy
        # The destination port range for the protocol specified in the security group rule. Valid values:
        #          
        # - For TCP or UDP: 1 to 65535. Use a forward slash (/) to separate the start port and the end port. Example: 1/200.
        # - For ICMP: -1/-1.
        # - For GRE: -1/-1.
        # - For ALL: -1/-1.
        self.port_range = port_range
        # The ID of the port list.
        # 
        # You can call the `DescribePortRangeLists` operation to query the IDs of available port lists.
        # 
        # If you specify the `Permissions.N.PortRange` parameter, this parameter is ignored.
        # 
        # For more information, see [Security group limits](~~25412#SecurityGroupQuota1~~).
        self.port_range_list_id = port_range_list_id
        # The priority of the security group rule. A smaller value indicates a higher priority. Valid values: 1 to 100.
        # 
        # Default value: 1.
        self.priority = priority
        # The source IPv4 Classless Inter-Domain Routing from which you want to revoke access permissions. CIDR format and IPv4 format IP address ranges are supported.
        self.source_cidr_ip = source_cidr_ip
        # The ID of the source security group from which you want to revoke access permissions.
        # 
        # - You must specify at least one of the following parameters: `SourceGroupId`, `SourceCidrIp`, `Ipv6SourceCidrIp`, and `SourcePrefixListId`.
        # 
        # - If you specify `SourceGroupId` but do not specify `SourceCidrIp` or `Ipv6SourceCidrIp`, you must set the NicType parameter to intranet.
        # 
        # - If you specify both `SourceGroupId` and `SourceCidrIp`, `SourceCidrIp` takes precedence by default.
        # 
        # Take note of the following items:
        # 
        # - Advanced security groups do not support authorization between security groups.
        # 
        # - A basic security group can be authorized to access a maximum of 20 other security groups.
        self.source_group_id = source_group_id
        # The Alibaba Cloud account to which the source security group belongs when you revoke a cross-account authorization security group rule.
        # 
        # - If Settings for neither `SourceGroupOwnerAccount` nor `SourceGroupOwnerId` are applied, it is considered that you are revoking the access permissions from your other security groups.
        # - If `SourceCidrIp` is specified, the `SourceGroupOwnerAccount` parameter is invalid.
        self.source_group_owner_account = source_group_owner_account
        # The ID of the Alibaba Cloud account to which the source security group belongs when you revoke a cross-account authorization security group rule.
        # 
        # - If Settings for neither `SourceGroupOwnerId` nor `SourceGroupOwnerAccount` are applied, it is considered that you are revoking the access permissions from your other security groups.
        # - If `SourceCidrIp` is specified, the `SourceGroupOwnerId` parameter is invalid.
        self.source_group_owner_id = source_group_owner_id
        # The source port range for the protocol specified in the security group rule. Valid values: 
        #          
        # - For TCP or UDP: 1 to 65535. Use a forward slash (/) to separate the start port and the end port. Example: 1/200.
        # - For ICMP: -1/-1.
        # - For GRE: -1/-1.
        # - For ALL: -1/-1.
        # 
        # This parameter is used to support quintuple rules. For more information, see [Quintuple rules for security groups](https://help.aliyun.com/document_detail/97439.html).
        self.source_port_range = source_port_range
        # The ID of the source prefix list from which you want to revoke access permissions. You can call the [DescribePrefixLists](https://help.aliyun.com/document_detail/205046.html) operation to query the IDs of available prefix lists.
        # 
        # Precautions:
        # 
        # If you specify one of the `SourceCidrIp`, `Ipv6SourceCidrIp`, and `SourceGroupId` parameters, this parameter is ignored.
        # 
        # For more information, see [Security group limits](~~25412#SecurityGroupQuota1~~).
        self.source_prefix_list_id = source_prefix_list_id

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

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        if self.source_group_id is not None:
            result['SourceGroupId'] = self.source_group_id

        if self.source_group_owner_account is not None:
            result['SourceGroupOwnerAccount'] = self.source_group_owner_account

        if self.source_group_owner_id is not None:
            result['SourceGroupOwnerId'] = self.source_group_owner_id

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        if self.source_prefix_list_id is not None:
            result['SourcePrefixListId'] = self.source_prefix_list_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')

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

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        if m.get('SourceGroupId') is not None:
            self.source_group_id = m.get('SourceGroupId')

        if m.get('SourceGroupOwnerAccount') is not None:
            self.source_group_owner_account = m.get('SourceGroupOwnerAccount')

        if m.get('SourceGroupOwnerId') is not None:
            self.source_group_owner_id = m.get('SourceGroupOwnerId')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        if m.get('SourcePrefixListId') is not None:
            self.source_prefix_list_id = m.get('SourcePrefixListId')

        return self

