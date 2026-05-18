# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFileSystemsRequest(DaraModel):
    def __init__(
        self,
        input_region_id: str = None,
        limit: int = None,
        next_token: str = None,
        order_by: str = None,
        order_type: str = None,
        start_offset: int = None,
    ):
        # This parameter is required.
        self.input_region_id = input_region_id
        self.limit = limit
        self.next_token = next_token
        self.order_by = order_by
        self.order_type = order_type
        self.start_offset = start_offset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.start_offset is not None:
            result['StartOffset'] = self.start_offset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('StartOffset') is not None:
            self.start_offset = m.get('StartOffset')

        return self

