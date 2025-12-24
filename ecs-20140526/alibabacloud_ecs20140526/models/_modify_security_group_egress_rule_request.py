# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySecurityGroupEgressRuleRequest(DaraModel):
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
        policy: str = None,
        port_range: str = None,
        port_range_list_id: str = None,
        priority: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        security_group_rule_id: str = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.**** For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the security group rule. The description must be 1 to 512 characters in length.
        self.description = description
        # The destination IPv4 CIDR block. IPv4 CIDR blocks and IPv4 addresses are supported.
        # 
        # By default, this parameter is left empty.
        self.dest_cidr_ip = dest_cidr_ip
        # The ID of the destination security group. You must specify at least one of `DestGroupId` and `DestCidrIp`.
        # 
        # *   At least one of DestGroupId, DestCidrIp, Ipv6DestCidrIp, and DestPrefixListId must be specified.
        # *   If DestGroupId is specified but DestCidrIp is not specified, the NicType parameter can be set only to intranet.
        # *   If both DestGroupId and DestCidrIp are specified, DestCidrIp takes precedence.
        self.dest_group_id = dest_group_id
        # The Alibaba Cloud account that manages the destination security group when you set security group rule N across accounts.
        self.dest_group_owner_account = dest_group_owner_account
        # The ID of the Alibaba Cloud account that manages the destination security group when you set security group rule N across accounts.
        self.dest_group_owner_id = dest_group_owner_id
        # The ID of the destination prefix list. You can call the [DescribePrefixLists](https://help.aliyun.com/document_detail/205046.html) operation to query the IDs of available prefix lists.
        # 
        # If you specify `DestCidrIp`, `Ipv6DestCidrIp`, or `DestGroupId`, this parameter is ignored.
        self.dest_prefix_list_id = dest_prefix_list_id
        # Network Layer /transport layer protocol. Two types of assignments are supported:
        # 
        # 1.  The case-insensitive protocol name. Valid values:
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
        # The destination IPv6 CIDR block. IPv6 CIDR blocks and IPv6 addresses are supported.
        # 
        # >  Only the IP addresses of instances in virtual private clouds (VPCs) are supported. You cannot specify both Ipv6DestCidrIp and `DestCidrIp`.
        # 
        # By default, this parameter is left empty.
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        # The source IPv6 CIDR block. IPv6 CIDR blocks and IPv6 addresses are supported.
        # 
        # >  Only the IP addresses of instances in VPCs are supported. You cannot specify both Ipv6SourceCidrIp and `SourceCidrIp`.
        # 
        # By default, this parameter is left empty.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The network interface controller (NIC) type.
        # 
        # >  You cannot modify this parameter when you modify a security group rule by specifying the ID of the rule. If you want to change the NIC type of a security group rule, you can create a security group rule of a desired NIC type and delete the existing rule.
        self.nic_type = nic_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The action of the security group rule. Valid values:
        # 
        # *   accept: allows access.
        # *   drop: denies access and returns no responses.
        # 
        # Default value: accept.
        self.policy = policy
        # The range of destination ports that correspond to the transport layer protocol. Valid values:
        # 
        # *   If you set IpProtocol to TCP or UDP, the port number range is 1 to 65535. Separate the start port number and the end port number with a forward slash (/). Example: 1/200.
        # *   If you set IpProtocol to ICMP, the port number range is -1/-1.
        # *   If you set IpProtocol to GRE, the port number range is -1/-1.
        # *   If you set IpProtocol to ALL, the port number range is -1/-1.
        self.port_range = port_range
        # The ID of the port list. You can call the `DescribePortRangeLists` operation to query the IDs of available prefix lists.
        # 
        # *   If you specify PortRange, the value of this parameter is ignored.
        # *   If the security group is of the classic network type, you cannot reference port lists in the security group rules. For information about the limits on security groups and port lists, see the [Security groups](~~25412#SecurityGroupQuota1~~) section of the "Limits and quotas" topic.
        self.port_range_list_id = port_range_list_id
        # The priority of the security group rule. Valid values: 1 to 100.
        # 
        # Default value: 1.
        self.priority = priority
        # The region ID of the security group. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the security group.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The ID of the security group rule. You can call the [DescribeSecurityGroupAttribute](https://help.aliyun.com/document_detail/2679845.html) operation to query the IDs of security group rules in a security group.
        self.security_group_rule_id = security_group_rule_id
        # The source IPv4 CIDR block. IPv4 CIDR blocks and IPv4 addresses are supported.
        # 
        # By default, this parameter is left empty.
        self.source_cidr_ip = source_cidr_ip
        # The range of source ports that correspond to the transport layer protocol. Valid values:
        # 
        # *   If you set IpProtocol to TCP or UDP, the port number range is 1 to 65535. Separate the start port number and the end port number with a forward slash (/). Example: 1/200.
        # *   If you set IpProtocol to ICMP, the port number range is -1/-1.
        # *   If you set IpProtocol to GRE, the port number range is -1/-1.
        # *   If you set IpProtocol to ALL, the port number range is -1/-1.
        self.source_port_range = source_port_range

    def validate(self):
        pass

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

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.port_range_list_id is not None:
            result['PortRangeListId'] = self.port_range_list_id

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

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('PortRangeListId') is not None:
            self.port_range_list_id = m.get('PortRangeListId')

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

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        return self

