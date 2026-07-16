# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class AuthorizeSecurityGroupRequest(DaraModel):
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
        permissions: List[main_models.AuthorizeSecurityGroupRequestPermissions] = None,
        policy: str = None,
        port_range: str = None,
        priority: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        source_cidr_ip: str = None,
        source_group_id: str = None,
        source_group_owner_account: str = None,
        source_group_owner_id: int = None,
        source_port_range: str = None,
        source_prefix_list_id: str = None,
    ):
        # A client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # Deprecated. Use `Permissions.N.Description` to specify the description of the security group rule.
        self.description = description
        # Deprecated. Use `Permissions.N.DestCidrIp` to specify the destination IPv4 CIDR block.
        self.dest_cidr_ip = dest_cidr_ip
        # Deprecated. Use `Permissions.N.IpProtocol` to specify the protocol type.
        self.ip_protocol = ip_protocol
        # Deprecated. Use `Permissions.N.Ipv6DestCidrIp` to specify the destination IPv6 CIDR block.
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        # Deprecated. Use `Permissions.N.Ipv6SourceCidrIp` to specify the source IPv6 Classless Inter-Domain Routing block.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # Deprecated. Use `Permissions.N.NicType` to specify the NIC type.
        self.nic_type = nic_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The security group rules. Array length: 1 to 100.
        self.permissions = permissions
        # Deprecated. Use `Permissions.N.Policy` to set access permissions.
        self.policy = policy
        # Deprecated. Use `Permissions.N.PortRange` to specify the port range.
        self.port_range = port_range
        # Deprecated. Use `Permissions.N.Priority` to specify the security group rule priority.
        self.priority = priority
        # The region ID of the security group. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The security group ID.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # Deprecated. Use `Permissions.N.SourceCidrIp` to specify the source IPv4 Classless Inter-Domain Routing block.
        self.source_cidr_ip = source_cidr_ip
        # Deprecated. Use `Permissions.N.SourceGroupId` to specify the source security group ID.
        self.source_group_id = source_group_id
        # Deprecated. Use `Permissions.N.SourceGroupOwnerAccount` to specify the Alibaba Cloud account that owns the source security group.
        self.source_group_owner_account = source_group_owner_account
        # Deprecated. Use `Permissions.N.SourceGroupOwnerId` to specify the ID of the Alibaba Cloud account that owns the source security group.
        self.source_group_owner_id = source_group_owner_id
        # Deprecated. Use `Permissions.N.SourcePortRange` to specify the source port range.
        self.source_port_range = source_port_range
        # Deprecated. Use `Permissions.N.SourcePrefixListId` to specify the source prefix list ID.
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
                temp_model = main_models.AuthorizeSecurityGroupRequestPermissions()
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

class AuthorizeSecurityGroupRequestPermissions(DaraModel):
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
        # This parameter is used to support quintuple rules. For more information, see [Security group quintuple rules](https://help.aliyun.com/document_detail/97439.html).
        self.dest_cidr_ip = dest_cidr_ip
        # The network layer or transport layer protocol. Two types of values are supported:
        # 1. Case-insensitive protocol names. Valid values:
        # - ICMP
        # - GRE
        # - TCP
        # - UDP
        # - ALL: all protocols.
        # 2. Protocol numbers that comply with IANA specifications, which are integers from 0 to 255. The following regions currently support this feature:
        # - Philippines
        # - UK
        # - Malaysia
        # - China (Hohhot)
        # - China (Qingdao)
        # - US (Virginia)
        # - Singapore
        self.ip_protocol = ip_protocol
        # The destination IPv6 CIDR block. CIDR format and IPv6 format address ranges are supported.
        # 
        # This parameter is used to support quintuple rules. For more information, see [Security group quintuple rules](https://help.aliyun.com/document_detail/97439.html).
        # 
        # > This parameter is valid only for VPC-connected ECS instances that support IPv6. This parameter and `DestCidrIp` cannot be specified at the same time.
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        # The source IPv6 CIDR block for which you want to set access permissions. Settings for CIDR format and IPv6 format address ranges are supported.
        # 
        # > This parameter is valid only for VPC-connected ECS instances that support IPv6. This parameter and `SourceCidrIp` cannot be specified at the same time.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The network interface controller (NIC) type for a classic network type security group rule. Valid values:
        # 
        # - internet: public network interface controller (NIC).
        # 
        # - intranet: internal network interface controller (NIC).
        # 
        # For VPC security group rules, you do not need to set the network interface controller (NIC) type parameter. The default value is intranet, and only intranet is supported.
        # 
        # When you set security groups to access each other (only DestGroupId is specified), only intranet is supported.
        # 
        # Default value: internet.
        self.nic_type = nic_type
        # Settings for access permissions. Valid values:
        # 
        # - accept: accepts access.
        # 
        # - drop: denies access and does not return a deny message. The request appears to timeout or the connection cannot be established.
        # 
        # Default value: accept.
        self.policy = policy
        # The range of destination ports that correspond to the protocol for the security group. Valid values:
        # 
        # - TCP/UDP: Valid values are 1 to 65535. Separate the start port and the stop port with a forward slash (/). Example: 1/200.
        # - ICMP: -1/-1.
        # - GRE: -1/-1.
        # - ALL: -1/-1.
        # 
        # For more information about common ports, see [Common scenarios for ports](https://help.aliyun.com/document_detail/40724.html).
        self.port_range = port_range
        # The port address book ID.
        # You can invoke `DescribePortRangeLists` to query available port address book IDs.
        # - If you specify `Permissions.N.PortRange`, this parameter is ignored.
        # - Port address books are not supported for security groups with the classic network type. For more information about security group and port address book limits, see [Security group limits](~~25412#SecurityGroupQuota1~~). Settings for port address books are not available for classic network security groups.
        self.port_range_list_id = port_range_list_id
        # The priority of the security group rule. A smaller value indicates a higher priority. Valid values: 1 to 100.
        # 
        # Default value: 1.
        self.priority = priority
        # The source IPv4 CIDR block for which you want to set access permissions. Settings for CIDR format and IPv4 format address ranges are supported.
        self.source_cidr_ip = source_cidr_ip
        # The ID of the source security group for which you want to set access permissions.
        # 
        # - You must specify at least one of the following parameters: `SourceGroupId`, `SourceCidrIp`, `Ipv6SourceCidrIp`, or `SourcePrefixListId`.
        # 
        # - If `SourceGroupId` is specified but `SourceCidrIp` or `Ipv6SourceCidrIp` is not specified, the `NicType` parameter can only be set to `intranet`.
        # 
        # - If both `SourceGroupId` and `SourceCidrIp` are specified, `SourceCidrIp` takes precedence.
        self.source_group_id = source_group_id
        # The Alibaba Cloud account that owns the source security group when you set a cross-account security group rule.
        # 
        # - If neither `SourceGroupOwnerAccount` nor `SourceGroupOwnerId` is set, access permissions are configured for another security group within your account.
        # 
        # - If the `SourceCidrIp` parameter is set, the `SourceGroupOwnerAccount` parameter is ignored.
        self.source_group_owner_account = source_group_owner_account
        # The ID of the Alibaba Cloud account that owns the source security group when you set a cross-account security group rule.
        # 
        # - If neither `SourceGroupOwnerAccount` nor `SourceGroupOwnerId` is set, access permissions are configured for another security group within your account.
        # 
        # - If the `SourceCidrIp` parameter is set, the `SourceGroupOwnerAccount` parameter is ignored.
        self.source_group_owner_id = source_group_owner_id
        # The range of source ports that correspond to the protocol for the security group. Valid values:
        # 
        # - TCP/UDP: Valid values are 1 to 65535. Separate the start port and the end port with a forward slash (/). Example: 1/200.
        # - ICMP: -1/-1.
        # - GRE: -1/-1.
        # - ALL: -1/-1.
        # 
        # This parameter is used to support quintuple rules. For more information, see [Security group quintuple rules](https://help.aliyun.com/document_detail/97439.html).
        self.source_port_range = source_port_range
        # The ID of the source prefix list for which you want to set access permissions. You can call [DescribePrefixLists](https://help.aliyun.com/document_detail/205046.html) to query available prefix list IDs.
        # 
        # Notes:
        # 
        # If you specify `SourceCidrIp`, `Ipv6SourceCidrIp`, or `SourceGroupId`, this parameter is ignored.
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

