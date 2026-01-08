# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteNatFirewallControlPolicyBatchRequest(DaraModel):
    def __init__(
        self,
        acl_uuid_list: List[str] = None,
        direction: str = None,
        lang: str = None,
        nat_gateway_id: str = None,
    ):
        # The UUIDs of access control policies.
        # 
        # This parameter is required.
        self.acl_uuid_list = acl_uuid_list
        # The direction of the traffic to which the access control policy applies. Valid values:
        # 
        # *   **out**: outbound traffic
        self.direction = direction
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_uuid_list is not None:
            result['AclUuidList'] = self.acl_uuid_list

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuidList') is not None:
            self.acl_uuid_list = m.get('AclUuidList')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        return self

