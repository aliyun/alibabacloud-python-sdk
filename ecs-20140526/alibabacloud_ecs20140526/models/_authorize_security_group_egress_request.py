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
        # A client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # Deprecated. Use `Permissions.N.Description` to specify the rule description.
        self.description = description
        # Deprecated. Use `Permissions.N.DestCidrIp` to specify the destination IPv4 Classless Inter-Domain Routing (CIDR) block.
        self.dest_cidr_ip = dest_cidr_ip
        # Deprecated. Use `Permissions.N.DestGroupId` to specify the destination security group ID.
        self.dest_group_id = dest_group_id
        # Deprecated. Use `Permissions.N.DestGroupOwnerAccount` to specify the Alibaba Cloud account that manages the destination security group.
        self.dest_group_owner_account = dest_group_owner_account
        # Deprecated. Use `Permissions.N.DestGroupOwnerId` to specify the ID of the Alibaba Cloud account that manages the destination security group.
        self.dest_group_owner_id = dest_group_owner_id
        # Deprecated. Use `Permissions.N.DestPrefixListId` to specify the source prefix list ID.
        self.dest_prefix_list_id = dest_prefix_list_id
        # Deprecated. Use `Permissions.N.IpProtocol` to specify the protocol type.
        self.ip_protocol = ip_protocol
        # Deprecated. Use `Permissions.N.Ipv6DestCidrIp` to specify the destination IPv6 Classless Inter-Domain Routing (CIDR) block.
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        # Deprecated. Use `Permissions.N.Ipv6SourceCidrIp` to specify the source IPv6 CIDR block.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # Deprecated. Use `Permissions.N.NicType` to specify the NIC type.
        self.nic_type = nic_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The security group rules. Array length: 1 to 100.
        self.permissions = permissions
        # Deprecated. Use `Permissions.N.Policy` to configure the access permission settings.
        self.policy = policy
        # Deprecated. Use `Permissions.N.PortRange` to specify the port range.
        self.port_range = port_range
        # Deprecated. Use `Permissions.N.Priority` to specify the rule priority.
        self.priority = priority
        # The region ID of the source security group. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The security group ID.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # Deprecated. Use `Permissions.N.SourceCidrIp` to specify the source IPv4 CIDR block.
        self.source_cidr_ip = source_cidr_ip
        # Deprecated. Use `Permissions.N.SourcePortRange` to specify the source port range.
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
        # The description of the security group rule. The description must be 1 to 512 characters in length.
        self.description = description
        # The destination IPv4 Classless Inter-Domain Routing (CIDR) block for which you want to configure access permission settings. Both CIDR format and IPv4 format address ranges are supported.
        self.dest_cidr_ip = dest_cidr_ip
        # The ID of the destination security group for which you want to set access permissions.
        # 
        # - You must specify at least one of the following parameters: `DestGroupId`, `DestCidrIp`, `Ipv6DestCidrIp`, or `DestPrefixListId`.
        # 
        # - If `DestGroupId` is specified but `DestCidrIp` is not, the `NicType` parameter can only be set to intranet.
        # 
        # - If both `DestGroupId` and `DestCidrIp` are specified, `DestCidrIp` takes precedence.
        self.dest_group_id = dest_group_id
        # The Alibaba Cloud account that manages the destination security group when you configure a cross-account security group rule settings. 
        #          
        # - If neither `DestGroupOwnerAccount` nor `DestGroupOwnerId` is specified, the access permissions are configured for another security group within your account.
        # - If the `DestCidrIp` parameter is specified, the `DestGroupOwnerAccount` parameter is ignored.
        self.dest_group_owner_account = dest_group_owner_account
        # The ID of the Alibaba Cloud account that manages the destination security group when you configure a cross-account security group rule settings. 
        #          
        # - If neither `DestGroupOwnerId` nor `DestGroupOwnerAccount` is specified, the access permissions are configured for another security group within your account.
        # - If the `DestCidrIp` parameter is specified, the `DestGroupOwnerId` parameter is ignored.
        self.dest_group_owner_id = dest_group_owner_id
        # The ID of the destination prefix list for which you want to set access permissions. You can call [DescribePrefixLists](https://help.aliyun.com/document_detail/205046.html) to query available prefix list IDs.
        # 
        # Notes:
        # 
        # If you specify one of the `DestCidrIp`, `Ipv6DestCidrIp`, or `DestGroupId` parameters, this parameter is ignored.
        # 
        # For more information, see [Security group limits](~~25412#SecurityGroupQuota1~~).
        self.dest_prefix_list_id = dest_prefix_list_id
        # The network-layer or transport-layer protocol. Two types of values are supported:
        # 1. Case-insensitive protocol names. Valid values:
        # - ICMP
        # - GRE
        # - TCP
        # - UDP
        # - ALL: All protocols are supported.
        # 2. Protocol numbers that comply with IANA specifications, which are integers from 0 to 255. The following regions currently support this feature:
        # - Philippines
        # - UK
        # - Malaysia
        # - Hohhot
        # - Qingdao
        # - US West
        # - Singapore
        self.ip_protocol = ip_protocol
        # The destination IPv6 Classless Inter-Domain Routing (CIDR) block for which you want to configure access permission settings. Both CIDR format and IPv6 format address ranges are supported.
        # 
        # > This parameter is valid only for VPC-type ECS instances that support IPv6. This parameter and `DestCidrIp` cannot be specified at the same time.
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        # The source IPv6 CIDR block. Both CIDR format and IPv6 format address ranges are supported. 
        # 
        # This parameter is used to support quintuple rules. For more information, see [Security group quintuple rules](https://help.aliyun.com/document_detail/97439.html).
        # 
        # > This parameter is valid only for VPC-type ECS instances that support IPv6. This parameter and `DestCidrIp` cannot be specified at the same time.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The network interface controller (NIC) type settings for a classic network security group rule. Valid values: 
        #          
        # - internet: public network interface controller (NIC).
        # - intranet: internal network interface controller (NIC).
        #     - For VPC-type security group rules, you do not need to configure the network interface controller (NIC) type settings. The default value is intranet.
        #     - When you configure security groups to access each other, meaning only the DestGroupId parameter is specified, the value can only be intranet.
        # 
        # Default value: internet.
        self.nic_type = nic_type
        # The access permission settings. Valid values: 
        #          
        # - accept: Accepts access.
        # - drop: Denies access and does not return a deny message. The request times out or a timeout error similar to a connection failure is returned.
        # 
        # Default value: accept.
        self.policy = policy
        # The range of destination ports that correspond to the protocol for the security group. Valid values:
        #          
        # - TCP/UDP: Valid values are 1 to 65535. Separate the start port and the end port with a forward slash (/). Example: 1/200.
        # - ICMP: -1/-1.
        # - GRE: -1/-1.
        # - ALL: -1/-1.
        self.port_range = port_range
        # The port list ID.
        # You can invoke `DescribePortRangeLists` to query available port list IDs.
        # - If you specify `Permissions.N.PortRange`, this parameter is ignored.
        # - Port lists are not supported for classic network security group settings. For more information about security group and port list limits, see [Security group limits](~~25412#SecurityGroupQuota1~~).
        self.port_range_list_id = port_range_list_id
        # The priority of the security group rule. A smaller value indicates a higher priority. Valid values: 1 to 100.
        # 
        # Default value: 1.
        self.priority = priority
        # The source IPv4 CIDR block. Both CIDR format and IPv4 format address ranges are supported.
        # 
        # This parameter is used to support quintuple rules. For more information, see [Security group quintuple rules](https://help.aliyun.com/document_detail/97439.html).
        self.source_cidr_ip = source_cidr_ip
        # The range of source ports that correspond to the protocol for the security group. Valid values:
        #          
        # - TCP/UDP: Valid values are 1 to 65535. Separate the start port and the end port with a forward slash (/). Example: 1/200.
        # - ICMP: -1/-1.
        # - GRE: -1/-1.
        # - ALL: -1/-1.
        # 
        # This parameter is used to support quintuple rules. For more information, see [Security group quintuple rules](https://help.aliyun.com/document_detail/97439.html).
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

