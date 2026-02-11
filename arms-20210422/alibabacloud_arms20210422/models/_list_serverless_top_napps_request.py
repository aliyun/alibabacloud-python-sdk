# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServerlessTopNAppsRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        limit: int = None,
        order_by: str = None,
        region_id: str = None,
        start_time: int = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        self.limit = limit
        self.order_by = order_by
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

