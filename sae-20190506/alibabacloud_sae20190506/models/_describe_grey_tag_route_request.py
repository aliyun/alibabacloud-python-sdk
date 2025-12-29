# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGreyTagRouteRequest(DaraModel):
    def __init__(
        self,
        grey_tag_route_id: int = None,
    ):
        # The ID of the canary release rule.
        # 
        # This parameter is required.
        self.grey_tag_route_id = grey_tag_route_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')

        return self

