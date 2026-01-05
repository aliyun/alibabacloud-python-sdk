# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class AuthorizeSecurityGroupEgressRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dest_cidr_ip: str = None,
        dest_group_id: str = None,
        dest_group_owner_account: str = None,
        dest_group_owner_id: int = None,
        dest_prefix_list_id: str = None,
        ip_protocol: str = None,
        ipv_6dest_cidr_ip: str = None,
        ipv_6source_cidr_ip: str = None,
        nic_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        permissions: List[main_models.AuthorizeSecurityGroupEgressRequestPermissions] = None,
        policy: str = None,
        port_range: str = None,
        priority: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # This parameter is deprecated. Use `Permissions.N.Description` to specify the description of security group rule N.
        self.description = description
        # This parameter is deprecated. Use `Permissions.N.DestCidrIp` to specify the destination IPv4 CIDR block.
        self.dest_cidr_ip = dest_cidr_ip
        # This parameter is deprecated. Use `Permissions.N.DestGroupId` to specify the ID of the destination security group.
        self.dest_group_id = dest_group_id
        # This parameter is deprecated. Use `Permissions.N.DestGroupOwnerAccount` to specify the Alibaba Cloud account that manages the destination security group.
        self.dest_group_owner_account = dest_group_owner_account
        # This parameter is deprecated. Use `Permissions.N.DestGroupOwnerId` to specify the ID of the Alibaba Cloud account that manages the destination security group.
        self.dest_group_owner_id = dest_group_owner_id
        # This parameter is deprecated. Use `Permissions.N.DestPrefixListId` to specify the ID of the destination prefix list.
        self.dest_prefix_list_id = dest_prefix_list_id
        # This parameter is deprecated. Use `Permissions.N.IpProtocol` to specify the protocol.
        self.ip_protocol = ip_protocol
        # This parameter is deprecated. Use `Permissions.N.Ipv6DestCidrIp` to specify the destination IPv6 CIDR block.
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        # This parameter is deprecated. Use `Permissions.N.Ipv6SourceCidrIp` to specify the source IPv6 CIDR block.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # This parameter is deprecated. Use `Permissions.N.NicType` to specify the NIC type.
        self.nic_type = nic_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # An array of security group rules. You can specify 1 to 100 security group rules.
        self.permissions = permissions
        # This parameter is deprecated. Use `Permissions.N.Policy` to specify whether to allow outbound access.
        self.policy = policy
        # This parameter is deprecated. Use `Permissions.N.PortRange` to specify the range of destination ports.
        self.port_range = port_range
        # This parameter is deprecated. Use `Permissions.N.Priority` to specify the rule priority.
        self.priority = priority
        # The region ID of the source security group. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The security group ID.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # This parameter is deprecated. Use `Permissions.N.SourceCidrIp` to specify the source IPv4 CIDR block.
        self.source_cidr_ip = source_cidr_ip
        # This parameter is deprecated. Use `Permissions.N.SourcePortRange` to specify the range of source ports.
        self.source_port_range = source_port_range

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

        if self.dest_group_id is not None:
            result['DestGroupId'] = self.dest_group_id

        if self.dest_group_owner_account is not None:
            result['DestGroupOwnerAccount'] = self.dest_group_owner_account

        if self.dest_group_owner_id is not None:
            result['DestGroupOwnerId'] = self.dest_group_owner_id

        if self.dest_prefix_list_id is not None:
            result['DestPrefixListId'] = self.dest_prefix_list_id

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

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')

        if m.get('DestGroupId') is not None:
            self.dest_group_id = m.get('DestGroupId')

        if m.get('DestGroupOwnerAccount') is not None:
            self.dest_group_owner_account = m.get('DestGroupOwnerAccount')

        if m.get('DestGroupOwnerId') is not None:
            self.dest_group_owner_id = m.get('DestGroupOwnerId')

        if m.get('DestPrefixListId') is not None:
            self.dest_prefix_list_id = m.get('DestPrefixListId')

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
                temp_model = main_models.AuthorizeSecurityGroupEgressRequestPermissions()
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

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        return self

class AuthorizeSecurityGroupEgressRequestPermissions(DaraModel):
    def __init__(
        self,
        description: str = None,
        dest_cidr_ip: str = None,
        dest_group_id: str = None,
        dest_group_owner_account: str = None,
        dest_group_owner_id: int = None,
        dest_prefix_list_id: str = None,
        ip_protocol: str = None,
        ipv_6dest_cidr_ip: str = None,
        ipv_6source_cidr_ip: str = None,
        nic_type: str = None,
        policy: str = None,
        port_range: str = None,
        port_range_list_id: str = None,
        priority: str = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        # The description of the security group rule. The description can be up to 1 to 512 characters in length.
        self.description = description
        # The destination IPv4 CIDR block of the security group rule. IPv4 CIDR blocks and IPv4 addresses are supported.
        self.dest_cidr_ip = dest_cidr_ip
        # The ID of the destination security group that is specified in the security group rule.
        # 
        # *   You must specify at least one of the following parameters: `DestGroupId`, `DestCidrIp`, `Ipv6DestCidrIp`, and `DestPrefixListId`.
        # *   If you specify `DestGroupId` but do not specify `DestCidrIp`, you must set `NicType` to intranet.
        # *   If you specify both `DestGroupId` and `DestCidrIp`, `DestCidrIp` takes precedence.
        self.dest_group_id = dest_group_id
        # The Alibaba Cloud account that manages the destination security group.
        # 
        # *   If both `DestGroupOwnerAccount` and `DestGroupOwnerId` are empty, the rule is created to control access to another security group in your Alibaba Cloud account.
        # *   If `DestCidrIp` is configured, `DestGroupOwnerAccount` is ignored.
        self.dest_group_owner_account = dest_group_owner_account
        # The ID of the Alibaba Cloud account that manages the destination security group.
        # 
        # *   If both `DestGroupOwnerId` and `DestGroupOwnerAccount` are empty, the rule is created to control access to another security group in your Alibaba Cloud account.
        # *   If you specify `DestCidrIp`, `DestGroupOwnerId` is ignored.
        self.dest_group_owner_id = dest_group_owner_id
        # The ID of the destination prefix list. You can call the [DescribePrefixLists](https://help.aliyun.com/document_detail/205046.html) operation to query the IDs of available prefix lists.
        # 
        # Notes:
        # 
        # *   If a security group resides in the classic network, you cannot specify prefix lists in the rules of the security group. For information about the limits on security groups and prefix lists, see the [Security groups](~~25412#SecurityGroupQuota1~~) section of the "Limits and quotas on ECS" topic.
        # *   If you specify `DestCidrIp`, `Ipv6DestCidrIp`, or `DestGroupId`, this parameter is ignored.
        self.dest_prefix_list_id = dest_prefix_list_id
        # Network Layer /transport layer protocol. Two types of assignments are supported:
        # 
        # 1.  The case-insensitive protocol name. Valid value:
        # 
        # *   ICMP
        # *   GRE
        # *   TCP
        # *   UDP
        # *   ALL: supports all protocols.
        # 
        # 2.  The value of the IANA-compliant protocol number, which is an integer from 0 to 255. List of regions currently available:
        # 
        # *   Philippines (Manila)
        # *   UK (London)
        # *   Malaysia (Kuala Lumpur)
        # *   China (Hohhot)
        # *   China (Qingdao)
        # *   US (Silicon Valley)
        # *   Singapore
        self.ip_protocol = ip_protocol
        # The destination IPv6 CIDR block of the security group rule. IPv6 CIDR blocks and IPv6 addresses are supported.
        # 
        # >  This parameter is valid only for VPC-type ECS instances that support IPv6. This parameter and the `DestCidrIp` parameter cannot be set at the same time.
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        # The source IPv6 CIDR block of the security group rule. or IPv6 address.
        # 
        # This property is used to support quintuple rules. For more information, see [Security group quintuple rules](https://help.aliyun.com/document_detail/97439.html).
        # 
        # >  This parameter is valid only for ECS instances that reside in virtual private clouds (VPCs) and support IPv6 CIDR blocks. You cannot specify this parameter and `DestCidrIp` in the same request.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The network interface controller (NIC) type of the security group rule if the security group resides in the classic network. Valid values:
        # 
        # *   internet: public NIC.
        # 
        # *   intranet: internal NIC.
        # 
        #     *   If the security group resides in a VPC, this parameter is set to intranet by default and cannot be changed.
        #     *   If you specify only DestGroupId to create a rule that controls access to the specified security group, you must set this parameter to intranet.
        # 
        # Default value: internet.
        self.nic_type = nic_type
        # The action of the security group rule. Valid values:
        # 
        # *   accept: allows outbound access.
        # *   drop: denies outbound access and returns no responses. In this case, the request times out or the connection cannot be established.
        # 
        # Default value: accept.
        self.policy = policy
        # The destination port range of the security group rule. Valid values:
        # 
        # *   TCP/UDP: Valid values: 1 to 65535. Use a forward slash (/) to separate the start and end ports. Example: 1/200.
        # *   ICMP:-1/-1.
        # *   GRE:-1/-1.
        # *   ALL:-1/-1.
        self.port_range = port_range
        # The ID of the port list. You can call the `DescribePortRangeLists` operation to query the IDs of available prefix lists.
        # 
        # *   If you specify `Permissions.N.PortRange`, this parameter is ignored.
        # *   If a security group resides in the classic network, you cannot reference port lists in the rules of the security group. For more information about limits on security groups and ports, see [Limits on security groups](~~25412#SecurityGroupQuota1~~).
        self.port_range_list_id = port_range_list_id
        # The priority of security group rule N. A smaller value specifies a higher priority. Valid values: 1 to 100.
        # 
        # Default value: 1.
        self.priority = priority
        # The source IPv4 CIDR block of the security group rule. IPv4 CIDR blocks and IPv4 addresses are supported.
        # 
        # This property is used to support quintuple rules. For more information, see [Security group quintuple rules](https://help.aliyun.com/document_detail/97439.html).
        self.source_cidr_ip = source_cidr_ip
        # The source port range of the security group rule. Valid values:
        # 
        # *   TCP/UDP protocol: 1 to 65535. Use a forward slash (/) to separate the start and end ports. Example: 1/200.
        # *   ICMP protocol:-1/-1.
        # *   GRE protocol:-1/-1.
        # *   ALL:-1/-1.
        # 
        # This property is used to support quintuple rules. For more information, see [Security group quintuple rules](https://help.aliyun.com/document_detail/97439.html).
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

        if self.dest_group_id is not None:
            result['DestGroupId'] = self.dest_group_id

        if self.dest_group_owner_account is not None:
            result['DestGroupOwnerAccount'] = self.dest_group_owner_account

        if self.dest_group_owner_id is not None:
            result['DestGroupOwnerId'] = self.dest_group_owner_id

        if self.dest_prefix_list_id is not None:
            result['DestPrefixListId'] = self.dest_prefix_list_id

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

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')

        if m.get('DestGroupId') is not None:
            self.dest_group_id = m.get('DestGroupId')

        if m.get('DestGroupOwnerAccount') is not None:
            self.dest_group_owner_account = m.get('DestGroupOwnerAccount')

        if m.get('DestGroupOwnerId') is not None:
            self.dest_group_owner_id = m.get('DestGroupOwnerId')

        if m.get('DestPrefixListId') is not None:
            self.dest_prefix_list_id = m.get('DestPrefixListId')

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

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        return self

