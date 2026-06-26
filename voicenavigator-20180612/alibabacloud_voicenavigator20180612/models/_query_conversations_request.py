# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryConversationsRequest(DaraModel):
    def __init__(
        self,
        begin_time_left_range: int = None,
        begin_time_right_range: int = None,
        calling_number: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The start of the time range to query. This value is a Unix timestamp in milliseconds.
        self.begin_time_left_range = begin_time_left_range
        # The end of the time range to query. This value is a Unix timestamp in milliseconds.
        self.begin_time_right_range = begin_time_right_range
        # The calling number.
        self.calling_number = calling_number
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time_left_range is not None:
            result['BeginTimeLeftRange'] = self.begin_time_left_range

        if self.begin_time_right_range is not None:
            result['BeginTimeRightRange'] = self.begin_time_right_range

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTimeLeftRange') is not None:
            self.begin_time_left_range = m.get('BeginTimeLeftRange')

        if m.get('BeginTimeRightRange') is not None:
            self.begin_time_right_range = m.get('BeginTimeRightRange')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

