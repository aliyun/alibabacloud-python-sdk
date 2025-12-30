# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLiveTranscodeJobsRequest(DaraModel):
    def __init__(
        self,
        key_word: str = None,
        page_no: int = None,
        page_size: int = None,
        sort_by: str = None,
        start_mode: int = None,
        status: int = None,
        type: str = None,
    ):
        # The search keyword. You can use the job ID or name as the keyword to search for jobs. If you search for jobs by name, fuzzy match is supported.
        self.key_word = key_word
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The sorting order. By default, the query results are sorted by creation time in descending order. Valid values:
        # 
        # *   asc
        # *   desc
        self.sort_by = sort_by
        # The start mode of the transcoding job.
        # 
        # *   0: The transcoding job immediately starts.
        # *   1: The transcoding job starts at the scheduled time.
        self.start_mode = start_mode
        # The state of the job.
        # 
        # 0: The job is not started. 1: The job is in progress. 2: The job is stopped.
        self.status = status
        # The type of the template used by the transcoding job.
        # 
        # *   normal
        # *   narrow-band
        # *   audio-only
        # *   origin
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_mode is not None:
            result['StartMode'] = self.start_mode

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartMode') is not None:
            self.start_mode = m.get('StartMode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

