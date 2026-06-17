# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNatFirewallControlPolicyPositionRequest(DaraModel):
    def __init__(
        self,
        acl_uuid: str = None,
        direction: str = None,
        lang: str = None,
        nat_gateway_id: str = None,
        new_order: int = None,
    ):
        # The unique ID of the access control policy.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The traffic direction of the access control policy.
        # 
        # Valid value:
        # 
        # - **out**: outbound traffic.
        self.direction = direction
        # The language of the response message. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The ID of the NAT Gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The new priority for the IPv4 access control policy of the NAT firewall.
        # Priorities are represented by numbers. A smaller number indicates a higher priority. The value 1 indicates the highest priority.
        # 
        # > The new priority must be within the range of existing priorities for IPv4 policies of the NAT firewall. Otherwise, the call fails.
        # 
        # Before calling this operation, call the DescribeNatFirewallPolicyPriorUsed operation to query the priority range of existing IPv4 policies for the specified traffic direction of the NAT firewall.
        # 
        # This parameter is required.
        self.new_order = new_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.new_order is not None:
            result['NewOrder'] = self.new_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')

        return self

