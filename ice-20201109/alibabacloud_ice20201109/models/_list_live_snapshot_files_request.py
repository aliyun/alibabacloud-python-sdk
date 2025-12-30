# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLiveSnapshotFilesRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        job_id: str = None,
        limit: int = None,
        sort_by: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # *   The maximum time range that can be specified is one day.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the snapshot job.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The number of results to return each time. Valid values: 1 to 100. Default value: 10.
        self.limit = limit
        # The sorting order. Default value: asc.
        # 
        # Valid values:
        # 
        # *   asc: sorts the query results by creation time in ascending order.
        # *   desc: sorts the query results by creation time in descending order.
        self.sort_by = sort_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
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

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

