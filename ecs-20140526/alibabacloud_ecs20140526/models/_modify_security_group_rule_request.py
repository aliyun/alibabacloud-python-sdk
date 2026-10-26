# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySecurityGroupRuleRequest(DaraModel):
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
        source_group_id: str = None,
        source_group_owner_account: str = None,
        source_group_owner_id: int = None,
        source_port_range: str = None,
        source_prefix_list_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the security group rule. The description must be 1 to 512 characters in length.
        self.description = description
        # The destination IPv4 CIDR block. CIDR format and IPv4 format IP address ranges are supported.
        # 
        # Default value: none.
        self.dest_cidr_ip = dest_cidr_ip
        # The network layer or transport layer protocol. Two types of values are supported:
        # 1. Case-insensitive protocol names. Valid values:
        # - ICMP
        # - GRE
        # - TCP
        # - UDP
        # - ALL: all protocols.
        # 2. Protocol numbers that comply with the IANA standard, which are integers from 0 to 255. Supported regions:
        # - Philippines
        # - UK
        # - Malaysia
        # - Hohhot
        # - Qingdao
        # - US West
        # - Singapore
        self.ip_protocol = ip_protocol
        # The destination IPv6 CIDR block. CIDR format and IPv6 format IP address ranges are supported.
        # 
        # > Only VPC-type IP addresses are supported. This parameter and the DestCidrIp parameter cannot be specified at the same time.
        # 
        # Default value: none.
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        # The source IPv6 CIDR block. CIDR format and IPv6 format IP address ranges are supported.
        # 
        # > Only VPC-type IP addresses are supported. This parameter and the SourceCidrIp parameter cannot be specified at the same time.
        # 
        # Default value: none.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The NIC type.
        # 
        # 
        # > You cannot modify this parameter when you modify a rule by specifying the security group rule ID. To modify this parameter, add a new rule and then delete the current rule.
        self.nic_type = nic_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The access permission. Valid values: 
        #          
        # - accept: allows access.
        # - drop: denies access and does not return a rejection message.
        # 
        # Default value: accept.
        self.policy = policy
        # The range of destination ports that are open for the transport layer protocol in the destination security group. Valid values: 
        #          
        # - For TCP and UDP: 1 to 65535. Use a forward slash (/) to separate the start port and the end port. Example: 1/200.
        # - For ICMP: -1/-1.
        # - For GRE: -1/-1.
        # - For ALL: -1/-1.
        self.port_range = port_range
        # The ID of the port list.
        # 
        # You can call the DescribePortRangeLists operation to query the IDs of available port lists.
        # 
        # If you specify the PortRange parameter, this parameter is ignored.
        # 
        # For more information, see [Security group limits](~~25412#SecurityGroupQuota1~~).
        self.port_range_list_id = port_range_list_id
        # The priority of the security group rule. Valid values: 1 to 100.
        # 
        # Default value: 1.
        self.priority = priority
        # The region ID of the target security group. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the security group.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The ID of the security group rule. You can call the [DescribeSecurityGroupAttribute](https://help.aliyun.com/document_detail/2679845.html) operation to query the security group rule ID.
        self.security_group_rule_id = security_group_rule_id
        # The source IPv4 CIDR block. CIDR format and IPv4 format IP address ranges are supported.
        # 
        # Default value: none.
        self.source_cidr_ip = source_cidr_ip
        # The ID of the source security group. You must specify at least one of the SourceGroupId and SourceCidrIp parameters.
        # 
        # - If you specify SourceGroupId but do not specify SourceCidrIp, the NicType parameter can only be set to intranet.
        # - If you specify both SourceGroupId and SourceCidrIp, SourceCidrIp takes precedence by default.
        self.source_group_id = source_group_id
        # The Alibaba Cloud account to which the source security group belongs when you configure a security group rule across accounts. 
        #          
        # - If neither SourceGroupOwnerAccount nor SourceGroupOwnerId is specified, the rule is considered to configure the access permissions for another security group of your own.
        # - If the SourceCidrIp parameter is specified, the SourceGroupOwnerAccount parameter is invalid.
        self.source_group_owner_account = source_group_owner_account
        # The Alibaba Cloud account to which the source security group belongs when you configure a security group rule across accounts. 
        #          
        # - If neither SourceGroupOwnerId nor SourceGroupOwnerAccount is specified, the rule is considered to configure the access permissions for another security group of your own.
        # - If the SourceCidrIp parameter is specified, the SourceGroupOwnerId parameter is invalid.
        self.source_group_owner_id = source_group_owner_id
        # The range of source ports that are open for the transport layer protocol in the source security group. Valid values: 
        #          
        # - For TCP and UDP: 1 to 65535. Use a forward slash (/) to separate the start port and the end port. Example: 1/200.
        # - For ICMP: -1/-1.
        # - For GRE: -1/-1.
        # - For ALL: -1/-1.
        self.source_port_range = source_port_range
        # The ID of the source prefix list. You can call the [DescribePrefixLists](https://help.aliyun.com/document_detail/205046.html) operation to query the IDs of available prefix lists.
        # 
        # If you specify one of the SourceCidrIp, Ipv6SourceCidrIp, or SourceGroupId parameters, this parameter is ignored.
        self.source_prefix_list_id = source_prefix_list_id

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

