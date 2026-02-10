# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListOperationProcessDetailRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        lang: str = None,
        page_size: int = None,
        start_time: int = None,
        status_codes: List[int] = None,
        task_ids: List[str] = None,
    ):
        # The page number. Default value: 1.
        self.current_page = current_page
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English.
        self.lang = lang
        # The number of entries per page.
        self.page_size = page_size
        # The beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time
        # The subtask status codes.
        self.status_codes = status_codes
        # The IDs of operation tasks.
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status_codes is not None:
            result['StatusCodes'] = self.status_codes

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatusCodes') is not None:
            self.status_codes = m.get('StatusCodes')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        return self

