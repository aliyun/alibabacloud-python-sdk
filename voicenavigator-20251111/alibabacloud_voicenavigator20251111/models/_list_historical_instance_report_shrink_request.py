# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHistoricalInstanceReportShrinkRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_ids_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
    ):
        # The end time for the query. The server rounds this value up to the next hour.
        self.end_time = end_time
        # A JSON array of instance IDs. The array can contain up to 100 IDs.
        self.instance_ids_shrink = instance_ids_shrink
        # The number of the page to return. The maximum value is 100.
        self.page_number = page_number
        # The number of entries to return on each page. The maximum value is 100.
        self.page_size = page_size
        # The start time for the query. The server rounds this value up to the next hour.
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

        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

