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
        # A client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the security group rule. The description must be 1 to 512 characters in length.
        self.description = description
        # The destination IPv4 Classless Inter-Domain Routing (CIDR) block. CIDR format and IPv4 format IP address range are supported.
        # 
        # Default value: null.
        self.dest_cidr_ip = dest_cidr_ip
        # The network-layer or transport-layer protocol. Two types of values are supported:
        # 1. Case-insensitive protocol names. Valid values:
        # - ICMP
        # - GRE
        # - TCP
        # - UDP
        # - ALL: all protocols are supported.
        # 2. Protocol numbers that comply with IANA specifications, which are integers from 0 to 255. The following regions currently support this feature:
        # - Philippines
        # - UK (London)
        # - Malaysia
        # - China (Hohhot)
        # - China (Qingdao)
        # - US (Virginia)
        # - Singapore.
        self.ip_protocol = ip_protocol
        # Settings for the destination IPv6 CIDR block. CIDR format and IPv6 format IP address range are supported.
        # 
        # > Only VPC-type IP addresses are supported. This parameter and `DestCidrIp` cannot be specified at the same time.
        # 
        # Default value: null.
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        # Settings for the source IPv6 CIDR block for the access permissions. Classless Inter-Domain Routing (CIDR) format and IPv6 format IP address range are supported.
        # 
        # > Only VPC-type IP addresses are supported. This parameter and `SourceCidrIp` cannot be specified at the same time.
        # 
        # Default value: null.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The network interface controller (NIC) type.
        # 
        # > When you modify a rule by specifying the security group rule ID, this parameter cannot be modified. To change this value, add a new rule and then delete the current rule.
        self.nic_type = nic_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The access permissions. Valid values: 
        #          
        # - accept: accepts access.
        # - drop: deny access and does not return a rejection response.
        # 
        # Default value: accept.
        self.policy = policy
        # The range of destination ports that correspond to the transport-layer protocol. Valid values: 
        #          
        # - TCP/UDP: valid values are 1 to 65535. Separate the start port and the end port with a forward slash (/). Example: 1/200.
        # - ICMP: -1/-1.
        # - GRE: -1/-1.
        # - ALL: -1/-1.
        self.port_range = port_range
        # Settings for the port address book ID.
        # You can invoke `DescribePortRangeLists` to query available port address book IDs.
        # - This parameter is ignored if you specify the PortRange parameter.
        # - Port address books are not supported for security groups with the classic network type. For more information about the limits of security groups and port address books, see [Security group limits](~~25412#SecurityGroupQuota1~~).
        self.port_range_list_id = port_range_list_id
        # The priority of the security group rule. Valid values: 1 to 100.
        # 
        # Default value: 1.
        self.priority = priority
        # The region ID of the target security group. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The security group ID.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The security group rule ID. You can call [DescribeSecurityGroupAttribute](https://help.aliyun.com/document_detail/2679845.html) to query security group rule IDs.
        self.security_group_rule_id = security_group_rule_id
        # Settings for the source IPv4 CIDR block for the access permissions. Classless Inter-Domain Routing (CIDR) format and IPv4 format IP address range are supported.
        # 
        # Default value: null.
        self.source_cidr_ip = source_cidr_ip
        # Settings for the ID of the source security group for the access permissions. Specify at least one of `SourceGroupId` and `SourceCidrIp`.
        # 
        # - If `SourceGroupId` is specified but `SourceCidrIp` is not, the `NicType` parameter can only be set to intranet.
        # - If both `SourceGroupId` and `SourceCidrIp` are specified, `SourceCidrIp` takes precedence by default.
        self.source_group_id = source_group_id
        # The Alibaba Cloud account that owns the source security group when you configure a cross-account security group rule. 
        #          
        # - If neither `SourceGroupOwnerAccount` nor `SourceGroupOwnerID` is set, the rule is configured for access permissions of another security group within your account.
        # - If the parameter `SourceCidrIp` is specified, the parameter `SourceGroupOwnerAccount` is ignored.
        self.source_group_owner_account = source_group_owner_account
        # The Alibaba Cloud account that owns the source security group when you configure a cross-account security group rule. 
        #          
        # - If neither `SourceGroupOwnerId` nor `SourceGroupOwnerAccount` is set, the rule is configured for access permissions of another security group within your account.
        # - If the parameter `SourceCidrIp` is specified, the parameter `SourceGroupOwnerId` is ignored.
        self.source_group_owner_id = source_group_owner_id
        # The range of source ports that correspond to the transport-layer protocol. Valid values: 
        #          
        # - TCP/UDP: valid values are 1 to 65535. Separate the start port and the end port with a forward slash (/). Example: 1/200.
        # - ICMP: -1/-1.
        # - GRE: -1/-1.
        # - ALL: -1/-1.
        self.source_port_range = source_port_range
        # Settings for the ID of the source prefix list for the access permissions. You can invoke [DescribePrefixLists](https://help.aliyun.com/document_detail/205046.html) to query available prefix list IDs.
        # 
        # This parameter is ignored if you specify one of the `SourceCidrIp`, `Ipv6SourceCidrIp`, or `SourceGroupId` parameters.
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

