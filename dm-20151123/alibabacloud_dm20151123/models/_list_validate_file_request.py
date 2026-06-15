# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListValidateFileRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        file_keyword: str = None,
        page: int = None,
        page_size: int = None,
        start_time: str = None,
    ):
        # The end time. The time is in UTC and follows the RFC 3339 format.
        # 
        # This parameter is required.
        self.end_time = end_time
        # A keyword in the file name.
        self.file_keyword = file_keyword
        # The page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The start time. The time is in UTC and follows the RFC 3339 format.
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

        if self.file_keyword is not None:
            result['FileKeyword'] = self.file_keyword

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FileKeyword') is not None:
            self.file_keyword = m.get('FileKeyword')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

