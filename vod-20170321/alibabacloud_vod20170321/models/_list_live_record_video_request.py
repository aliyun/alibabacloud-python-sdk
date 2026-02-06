# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLiveRecordVideoRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        page_no: int = None,
        page_size: int = None,
        sort_by: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        # The name of the application that was used to record the live stream.
        self.app_name = app_name
        # The domain name of the recorded live stream.
        self.domain_name = domain_name
        # The end of the time range to query. The query is performed based on the time range during which the required live streams were recorded. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.end_time = end_time
        # The number of the page to return. Default value: **1**.
        self.page_no = page_no
        # The number of entries to return on each page. Maximum value: **100**. Default value: **10**.
        self.page_size = page_size
        # The sorting rule of the results. Valid values:
        # 
        # *   **CreationTime:Desc**: The results are sorted in reverse chronological order based on the creation time.
        # *   **CreationTime:Asc**: The results are sorted in chronological order based on the creation time.
        self.sort_by = sort_by
        # The beginning of the time range to query. The query is performed based on the time range during which the required live streams were recorded. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.start_time = start_time
        # The name of the recorded live stream.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

