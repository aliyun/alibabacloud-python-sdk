# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetMultipleTraceRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: int = None,
        trace_ids: List[str] = None,
    ):
        # The time when the trace ends. The value is a timestamp. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The number of the page to return. Default value: `1`.
        self.page_number = page_number
        # The number of entries to return per page, the maximum value is 1000.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The start time of the trace. The value is a timestamp. Unit: milliseconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The trace IDs.
        # 
        # This parameter is required.
        self.trace_ids = trace_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.trace_ids is not None:
            result['TraceIDs'] = self.trace_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TraceIDs') is not None:
            self.trace_ids = m.get('TraceIDs')

        return self

