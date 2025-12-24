# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveStreamsPublishListRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        order_by: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        query_type: str = None,
        region_id: str = None,
        start_time: str = None,
        stream_name: str = None,
        stream_type: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # The ingest domain or main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The end of the time range to query. The time range specified by the StartTime and EndTime parameters cannot exceed 30 days.
        # 
        # Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The sorting method. Valid values:
        # 
        # *   **stream_name_desc**: sorts the entries in descending order by stream name.
        # *   **stream_name_asc**: sorts the entries in ascending order by stream name.
        # *   **publish_time_desc**: sorts the entries in descending order by stream ingest time.
        # *   **publish_time_asc** (default): sorts the entries in ascending order by stream ingest time.
        self.order_by = order_by
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 3000**. Default value: **2000**.
        self.page_size = page_size
        # The mode in which stream names are matched. Valid values:
        # 
        # *   **fuzzy** (default): fuzzy match
        # *   **strict**: exact match
        self.query_type = query_type
        self.region_id = region_id
        # The beginning of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The name of the live stream.
        self.stream_name = stream_name
        # The type of the streams to query. Valid values:
        # 
        # *   An empty value****: source streams
        # *   **all**: all streams
        # *   **trans**: transcoded streams
        self.stream_type = stream_type

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

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        return self

