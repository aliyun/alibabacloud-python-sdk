# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConsumerAccessOverviewRequest(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
    ):
        # The target AI gateway instance ID. Quotas and resources are isolated by instance.
        # 
        # This parameter is required.
        self.gateway_id = gateway_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        return self

