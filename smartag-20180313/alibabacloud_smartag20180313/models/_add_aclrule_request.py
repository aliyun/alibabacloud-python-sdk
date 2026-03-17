# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddACLRuleRequest(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
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
        # The ID of the ACL.
        # 
        # This parameter is required.
        self.acl_id = acl_id
        # The description of the ACL rule.
        # 
        # The description must be **1 to 512** characters in length.
        self.description = description
        # The range of the destination IP addresses.
        # 
        # Specify the value of this parameter in CIDR notation. Example: 192.168.10.0/24.
        # 
        # This parameter is required.
        self.dest_cidr = dest_cidr
        # The destination port range.
        # 
        # Valid values: **1** to **65535** and **-1**.
        # 
        # Set the destination port range in one of the following formats: 1/200 or 80/80. A value of -1/-1 indicates all ports.
        # 
        # This parameter is required.
        self.dest_port_range = dest_port_range
        # The direction of traffic in which the ACL rule is applied. Valid values:
        # 
        # *   **in**: The ACL rule controls inbound network traffic of the on-premises network that is associated with the Smart Access Gateway (SAG) instance.
        # *   **out**: The ACL rule controls outbound network traffic of the on-premises network that is associated with the SAG instance.
        # 
        # This parameter is required.
        self.direction = direction
        self.dpi_group_ids = dpi_group_ids
        self.dpi_signature_ids = dpi_signature_ids
        # The protocol used by the ACL rule.
        # 
        # The protocols that are provided in this topic are for reference only. The protocols available in the SAG console may vary. The value of the parameter is not case-sensitive.
        # 
        # This parameter is required.
        self.ip_protocol = ip_protocol
        # The name of the ACL rule.
        # 
        # The name must be 2 to 100 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The action policy of the ACL rule. Valid values:
        # 
        # *   **accept**: allows network traffic.
        # *   **drop**: blocks the network traffic.
        # 
        # This parameter is required.
        self.policy = policy
        # The priority of the ACL rule.
        # 
        # A smaller value indicates a higher priority. If rules have the same priority, whichever applied to the SAG devices earlier takes effect.
        # 
        # Valid values: **1 to 100**. Default value: **1**.
        self.priority = priority
        # The ID of the region where the ACL is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/69813.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The range of the source IP addresses.
        # 
        # Specify the value of this parameter in CIDR notation. Example: 192.168.1.0/24.
        # 
        # This parameter is required.
        self.source_cidr = source_cidr
        # The source port range.
        # 
        # Valid values: **1** to **65535** and **-1**.
        # 
        # Set the source port range in one of the following formats: 1/200 or 80/80. A value of -1/-1 indicates all ports.
        # 
        # This parameter is required.
        self.source_port_range = source_port_range
        # The type of the ACL rule: Valid values:
        # 
        # *   **LAN**: The ACL rule controls network traffic transmitted through private IP addresses.
        # *   **WAN**: The ACL rule controls network traffic transmitted through public IP addresses.
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

