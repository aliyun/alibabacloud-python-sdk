# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDynamicRouteRequest(DaraModel):
    def __init__(
        self,
        dynamic_route_id: str = None,
    ):
        # This parameter is required.
        self.dynamic_route_id = dynamic_route_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')

        return self

