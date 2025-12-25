# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceOverviewRequest(DaraModel):
    def __init__(
        self,
        gateway_type: str = None,
    ):
        self.gateway_type = gateway_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        return self

