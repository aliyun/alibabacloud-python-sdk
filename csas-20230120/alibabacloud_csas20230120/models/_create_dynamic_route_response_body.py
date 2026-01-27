# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDynamicRouteResponseBody(DaraModel):
    def __init__(
        self,
        dynamic_route_id: str = None,
        request_id: str = None,
    ):
        self.dynamic_route_id = dynamic_route_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

