# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyACLRuleRequest(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acr_id: str = None,
        description: str = None,
        dest_cidr: str = None,
        dest_port_range: str = None,
        direction: str = None,
        dpi_group_ids: List[str] = None,
        dpi_signature_ids: List[str] = None,
        ip_protocol: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        policy: str = None,
        priority: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source_cidr: str = None,
        source_port_range: str = None,
        type: str = None,
    ):
        # The ID of the ACL instance.
        # 
        # This parameter is required.
        self.acl_id = acl_id
        # The ID of the access control rule.
        # 
        # Call the [DescribeACLAttribute](https://help.aliyun.com/document_detail/114017.html) operation to query the IDs of access control rules in an ACL instance.
        # 
        # This parameter is required.
        self.acr_id = acr_id
        # The description of the access control rule.
        # 
        # The description must be **1** to **512** characters in length.
        self.description = description
        # The destination CIDR block.
        # 
        # The destination CIDR block must be in CIDR format. For example: 192.168.10.0/24.
        self.dest_cidr = dest_cidr
        # The destination port range. Valid values: **-1** or **1** to **65535**.
        # 
        # Examples of the destination port range format:
        # 
        # - 1/200: ports 1 to 200.
        # - 80/80: port 80.
        # - -1/-1: all ports.
        self.dest_port_range = dest_port_range
        # The direction in which the access control rule is applied. Valid values:
        # 
        # - **in**: inbound. This is the direction of traffic from an external network to the on-premises network where the Smart Access Gateway instance is deployed.
        # - **out**: outbound. This is the direction of traffic from the on-premises network where the Smart Access Gateway instance is deployed to an external network.
        self.direction = direction
        # A list of application group IDs that the access control rule matches.
        self.dpi_group_ids = dpi_group_ids
        # A list of application IDs that the access control rule matches.
        self.dpi_signature_ids = dpi_signature_ids
        # The protocol used by the access control rule.
        # 
        # For the protocols supported by the access control feature, see the information in the console. The protocol is not case-sensitive.
        self.ip_protocol = ip_protocol
        # The name of the access control rule.
        # 
        # The name must be 2 to 128 characters in length, start with a letter or a Chinese character, and can contain digits, underscores (_), and hyphens (-).
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The authorization policy of the access control rule. Valid values:
        # 
        # - **accept**: allows access.
        # - **drop**: denies access.
        self.policy = policy
        # The priority of the access control rule.
        # 
        # A smaller value indicates a higher priority. If rules have the same priority, the one that is first delivered to the Smart Access Gateway device takes precedence.
        # 
        # Valid values: 1 to **100**. Default value: **1**.
        self.priority = priority
        # The region ID of the access control list (ACL) instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The source CIDR block.
        # 
        # The source CIDR block must be in CIDR format. For example: 192.168.1.0/24.
        self.source_cidr = source_cidr
        # The source port range. Valid values: **-1** or **1** to **65535**.
        # 
        # Examples of the source port range format:
        # 
        # - 1/200: ports 1 to 200.
        # - 80/80: port 80.
        # - -1/-1: all ports.
        self.source_port_range = source_port_range
        # The type of the access control rule. Valid values:
        # 
        # - **LAN**: (Default) private network. This value indicates that the access control rule applies to traffic from private IP addresses.
        # - **WAN**: public network. This value indicates that the access control rule applies to traffic from public IP addresses.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acr_id is not None:
            result['AcrId'] = self.acr_id

        if self.description is not None:
            result['Description'] = self.description

        if self.dest_cidr is not None:
            result['DestCidr'] = self.dest_cidr

        if self.dest_port_range is not None:
            result['DestPortRange'] = self.dest_port_range

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.dpi_group_ids is not None:
            result['DpiGroupIds'] = self.dpi_group_ids

        if self.dpi_signature_ids is not None:
            result['DpiSignatureIds'] = self.dpi_signature_ids

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AcrId') is not None:
            self.acr_id = m.get('AcrId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestCidr') is not None:
            self.dest_cidr = m.get('DestCidr')

        if m.get('DestPortRange') is not None:
            self.dest_port_range = m.get('DestPortRange')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DpiGroupIds') is not None:
            self.dpi_group_ids = m.get('DpiGroupIds')

        if m.get('DpiSignatureIds') is not None:
            self.dpi_signature_ids = m.get('DpiSignatureIds')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

