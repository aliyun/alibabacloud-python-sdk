# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSwimmingLaneGatewayRoutesRequest(DaraModel):
    def __init__(
        self,
        gateway_unique_id: str = None,
        namespace_id: str = None,
    ):
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The ID of the namespace.
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        return self

