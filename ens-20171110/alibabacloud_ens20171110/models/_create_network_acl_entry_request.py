# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNetworkAclEntryRequest(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        destination_cidr_block: str = None,
        direction: str = None,
        network_acl_entry_name: str = None,
        network_acl_id: str = None,
        policy: str = None,
        port_range: str = None,
        priority: int = None,
        protocol: str = None,
    ):
        # The source CIDR block.
        # 
        # This parameter is required.
        self.cidr_block = cidr_block
        # The description of the network ACL.
        # 
        # The description must be 1 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        self.destination_cidr_block = destination_cidr_block
        # The direction in which the rule is applied. Valid values:
        # 
        # *   **ingress**
        # *   **egress**
        # 
        # This parameter is required.
        self.direction = direction
        # The name of the rule.
        # 
        # The name must be 1 to 128 characters in length and cannot start with http:// or https://.
        self.network_acl_entry_name = network_acl_entry_name
        # The ID of the network ACL.
        # 
        # This parameter is required.
        self.network_acl_id = network_acl_id
        # The action that is performed on network traffic that matches the rule. Valid values:
        # 
        # *   **accept**: allows network traffic.
        # *   **drop**: blocks network traffic.
        # 
        # This parameter is required.
        self.policy = policy
        # The port range.
        # 
        # *   If you set **Protocol** to **all** or **icmp**, set this parameter to -1/-1, which specifies all ports.
        # *   If you set **Protocol** to **tcp** or **udp**, the port can be **1 to 65535**. You can set this parameter to **1/200** or **80/80**, which specifies ports 1 to 200 or port 80.
        # 
        # This parameter is required.
        self.port_range = port_range
        # The priority of the rule. Valid values: **1 to 100**. Default value: **1**.
        # 
        # This parameter is required.
        self.priority = priority
        # The type of the protocol. Valid values:
        # 
        # *   **icmp**: ICMP
        # *   **tcp**: TCP
        # *   **udp**: UDP
        # *   **all**: all protocols
        # 
        # This parameter is required.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.description is not None:
            result['Description'] = self.description

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.network_acl_entry_name is not None:
            result['NetworkAclEntryName'] = self.network_acl_entry_name

        if self.network_acl_id is not None:
            result['NetworkAclId'] = self.network_acl_id

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('NetworkAclEntryName') is not None:
            self.network_acl_entry_name = m.get('NetworkAclEntryName')

        if m.get('NetworkAclId') is not None:
            self.network_acl_id = m.get('NetworkAclId')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

