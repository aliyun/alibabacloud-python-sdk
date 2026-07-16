# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyQosPolicyRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        dest_cidr: str = None,
        dest_port_range: str = None,
        dpi_group_ids: List[str] = None,
        dpi_signature_ids: List[str] = None,
        end_time: str = None,
        ip_protocol: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        priority: int = None,
        qos_id: str = None,
        qos_policy_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source_cidr: str = None,
        source_port_range: str = None,
        start_time: str = None,
    ):
        # The description of the stream classification rule.
        # 
        # The description must be 1 to 512 characters in length. It must start with a letter and can contain digits, underscores (_), and hyphens (-).
        self.description = description
        # The destination CIDR block.
        # 
        # The destination CIDR block must be in CIDR format. Example: 192.168.10.0/24.
        self.dest_cidr = dest_cidr
        # The destination port range.
        # 
        # Valid values: **-1** or **1** to **65535**.
        # 
        # Examples of how to specify a port range:
        # 
        # - **1/200**: ports 1 through 200.
        # - **80/80**: port 80.
        # - **-1/-1**: all ports.
        self.dest_port_range = dest_port_range
        # The list of application group IDs.
        self.dpi_group_ids = dpi_group_ids
        # The list of application IDs.
        self.dpi_signature_ids = dpi_signature_ids
        # The time when the stream classification rule expires.
        # 
        # Specify the time in the ISO 8601 standard. The time must be in UTC+8. Format: YYYY-MM-DDThh:mm:ss+0800.
        self.end_time = end_time
        # The protocol.
        # 
        # For a list of supported protocols, see the information in the console.
        self.ip_protocol = ip_protocol
        # The name of the stream classification rule.
        # 
        # The name must be 2 to 100 characters in length. It must start with a letter and can contain digits, underscores (_), and hyphens (-).
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The priority of the throttling rule to which the stream classification rule belongs.
        # 
        # Valid values: 1 to **3**. A smaller value indicates a higher priority.
        self.priority = priority
        # The ID of the QoS policy.
        # 
        # This parameter is required.
        self.qos_id = qos_id
        # The ID of the stream classification rule in the QoS policy.
        # 
        # This parameter is required.
        self.qos_policy_id = qos_policy_id
        # The ID of the region where the QoS policy is created.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The source CIDR block.
        # 
        # The source CIDR block must be in CIDR format. Example: 192.168.1.0/24.
        self.source_cidr = source_cidr
        # The source port range.
        # 
        # Valid values: **-1** or **1** to **65535**.
        # 
        # Examples of how to specify a port range:
        # 
        # - **1/200**: ports 1 through 200.
        # - **80/80**: port 80.
        # - **-1/-1**: all ports.
        self.source_port_range = source_port_range
        # The time when the stream classification rule takes effect.
        # 
        # Specify the time in the ISO 8601 standard. The time must be in UTC+8. Format: YYYY-MM-DDThh:mm:ss+0800.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.dest_cidr is not None:
            result['DestCidr'] = self.dest_cidr

        if self.dest_port_range is not None:
            result['DestPortRange'] = self.dest_port_range

        if self.dpi_group_ids is not None:
            result['DpiGroupIds'] = self.dpi_group_ids

        if self.dpi_signature_ids is not None:
            result['DpiSignatureIds'] = self.dpi_signature_ids

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        if self.qos_policy_id is not None:
            result['QosPolicyId'] = self.qos_policy_id

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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestCidr') is not None:
            self.dest_cidr = m.get('DestCidr')

        if m.get('DestPortRange') is not None:
            self.dest_port_range = m.get('DestPortRange')

        if m.get('DpiGroupIds') is not None:
            self.dpi_group_ids = m.get('DpiGroupIds')

        if m.get('DpiSignatureIds') is not None:
            self.dpi_signature_ids = m.get('DpiSignatureIds')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('QosPolicyId') is not None:
            self.qos_policy_id = m.get('QosPolicyId')

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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

