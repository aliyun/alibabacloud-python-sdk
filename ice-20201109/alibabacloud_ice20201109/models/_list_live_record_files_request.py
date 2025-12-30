# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListLiveRecordFilesRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        job_ids: List[str] = None,
        page_no: int = None,
        page_size: int = None,
        record_format: str = None,
        sort_by: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. The maximum time range to query is four days. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The list of job IDs.
        self.job_ids = job_ids
        # The page number of the page to return. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Valid values: 5 to 30. Default value: 10.
        self.page_size = page_size
        # The format of the recording file. Valid values:
        # 
        # M3U8, FLV, and MP4
        self.record_format = record_format
        # The sorting order of the index files by creation time. Valid values:
        # 
        # asc: The query results are displayed in ascending order. This is the default value.
        # 
        # desc: The query results are displayed in descending order.
        self.sort_by = sort_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
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

        if self.job_ids is not None:
            result['JobIds'] = self.job_ids

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.record_format is not None:
            result['RecordFormat'] = self.record_format

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecordFormat') is not None:
            self.record_format = m.get('RecordFormat')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

