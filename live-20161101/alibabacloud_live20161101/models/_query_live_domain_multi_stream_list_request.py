# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryLiveDomainMultiStreamListRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        end_time: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain = domain
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # The end time must be later than the start time. The time range specified by the StartTime and EndTime parameters cannot exceed seven days. If the two parameters are not specified, data of the last 24 hours is queried by default.
        self.end_time = end_time
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        # 
        # Valid values: 1 to 100.
        self.page_size = page_size
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC. The time range specified by the StartTime and EndTime parameters cannot exceed seven days.
        self.start_time = start_time
        # The name of the live stream. This parameter is used for exact match.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

