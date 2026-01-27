# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListPrivateAccessTagsForDynamicRouteRequest(DaraModel):
    def __init__(
        self,
        dynamic_route_ids: List[str] = None,
    ):
        # This parameter is required.
        self.dynamic_route_ids = dynamic_route_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_route_ids is not None:
            result['DynamicRouteIds'] = self.dynamic_route_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicRouteIds') is not None:
            self.dynamic_route_ids = m.get('DynamicRouteIds')

        return self

