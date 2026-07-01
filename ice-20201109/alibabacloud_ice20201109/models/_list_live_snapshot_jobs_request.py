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
        # The end of the time range to query. Specify the time in the ISO 8601 format: `yyyy-MM-ddTHH:mm:ssZ`. The time must be in UTC.
        # 
        # - If this parameter is not specified, the default is the current time.
        # 
        # -
        self.end_time = end_time
        # The page number to return. The value must be an integer greater than or equal to 1. Default value: 1.
        self.page_no = page_no
        # The number of jobs to return on each page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The search keyword. You can search by Job ID or Job Name. Fuzzy search is supported for Job Name.
        # 
        # - The maximum length is 128 characters.
        self.search_key_word = search_key_word
        # The sort order. The results are sorted by `CreateTime`. Default: `desc` (Descending).
        self.sort_by = sort_by
        # The start of the time range to query. Specify the time in the ISO 8601 format: `yyyy-MM-ddTHH:mm:ssZ`. The time must be in UTC.
        # 
        # - If this parameter is not specified, the default is 7 days ago.
        # 
        # - The interval between `StartTime` and `EndTime` cannot exceed 30 days.
        self.start_time = start_time
        # The job status to filter by. If omitted, jobs of all statuses are returned.
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

