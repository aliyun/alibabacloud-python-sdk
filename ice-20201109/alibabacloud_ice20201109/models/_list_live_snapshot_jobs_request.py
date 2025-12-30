# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLiveSnapshotJobsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        page_no: int = None,
        page_size: int = None,
        search_key_word: str = None,
        sort_by: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # *   By default, EndTime is seven days later than StartTime.
        # *   The time range specified by the StartTime and EndTime parameters cannot exceed 30 days.
        self.end_time = end_time
        # The page number. Valid values: [1,n). Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The search keyword. You can use the job ID or name as the keyword to search for jobs. If you search for jobs by name, fuzzy match is supported.
        # 
        # *   It cannot exceed 128 characters in length.
        self.search_key_word = search_key_word
        # The sorting order. By default, the query results are sorted by creation time in descending order.
        # 
        # Valid values:
        # 
        # *   asc: sorts the query results by creation time in ascending order.
        # *   desc: sorts the query results by creation time in descending order.
        self.sort_by = sort_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # *   The default value is seven days ago.
        # *   The time range specified by the StartTime and EndTime parameters cannot exceed 30 days.
        self.start_time = start_time
        # The job state filter. By default, all jobs are queried.
        # 
        # Valid values:
        # 
        # *   init: The job is not started.
        # *   paused: The job is paused.
        # *   started: The job is in progress.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

