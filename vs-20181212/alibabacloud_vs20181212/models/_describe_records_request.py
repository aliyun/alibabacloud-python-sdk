# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRecordsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        private_bucket: bool = None,
        sort_by: str = None,
        sort_direction: str = None,
        start_time: str = None,
        stream_id: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.private_bucket = private_bucket
        self.sort_by = sort_by
        self.sort_direction = sort_direction
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.stream_id = stream_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.private_bucket is not None:
            result['PrivateBucket'] = self.private_bucket

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_id is not None:
            result['StreamId'] = self.stream_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrivateBucket') is not None:
            self.private_bucket = m.get('PrivateBucket')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

