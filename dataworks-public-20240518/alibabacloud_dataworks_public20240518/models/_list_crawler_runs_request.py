# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCrawlerRunsRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        page_number: int = None,
        page_size: int = None,
        start_time_from: int = None,
        start_time_to: int = None,
        status: str = None,
    ):
        # The ID of the metadata crawler. You can call ListCrawlers to obtain the ID.
        # 
        # This parameter is required.
        self.id = id
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.page_size = page_size
        # The lower bound of the run start time, in millisecond-level UNIX timestamp. The value must be within the last 30 days. If not specified, the default value is 30 days before the current time.
        self.start_time_from = start_time_from
        # The upper bound of the run start time, in millisecond-level UNIX timestamp. The value must be within the last 30 days. If not specified, the default value is the current time.
        self.start_time_to = start_time_to
        # The run status. Valid values: WAITING, RUNNING, SUCCESS, ERROR, SHUTDOWN.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time_from is not None:
            result['StartTimeFrom'] = self.start_time_from

        if self.start_time_to is not None:
            result['StartTimeTo'] = self.start_time_to

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTimeFrom') is not None:
            self.start_time_from = m.get('StartTimeFrom')

        if m.get('StartTimeTo') is not None:
            self.start_time_to = m.get('StartTimeTo')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

