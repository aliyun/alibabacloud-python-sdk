# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeServiceLogResponseBody(DaraModel):
    def __init__(
        self,
        logs: List[str] = None,
        page_num: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page_num: int = None,
    ):
        # The returned logs.
        self.logs = logs
        # The page number.
        self.page_num = page_num
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The total number of pages returned.
        self.total_page_num = total_page_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logs is not None:
            result['Logs'] = self.logs

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

