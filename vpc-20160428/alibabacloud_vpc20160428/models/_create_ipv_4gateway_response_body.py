# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIpv4GatewayResponseBody(DaraModel):
    def __init__(
        self,
        ipv_4gateway_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the IPv4 gateway.
        self.ipv_4gateway_id = ipv_4gateway_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4gateway_id is not None:
            result['Ipv4GatewayId'] = self.ipv_4gateway_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4GatewayId') is not None:
            self.ipv_4gateway_id = m.get('Ipv4GatewayId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

