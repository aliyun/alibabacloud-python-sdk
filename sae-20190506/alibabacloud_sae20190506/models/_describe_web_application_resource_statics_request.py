# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWebApplicationResourceStaticsRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        namespace_id: str = None,
        region_id: str = None,
        start_time: int = None,
    ):
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The namespace ID.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # The region ID.
        self.region_id = region_id
        # The time when the task was created.
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

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

