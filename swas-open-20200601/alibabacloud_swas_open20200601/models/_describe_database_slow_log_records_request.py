# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDatabaseSlowLogRecordsRequest(DaraModel):
    def __init__(
        self,
        database_instance_id: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The ID of the lightweight database instance.
        # 
        # This parameter is required.
        self.database_instance_id = database_instance_id
        # The end of the time range to query. The end time must be later than the start time. The interval between the start time and the end time cannot be longer than 7 days.
        # 
        # The time is in UTC and must be formatted as `yyyy-MM-ddTHH:mm:ssZ` as specified by the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard.
        # 
        # > The console displays this time in the UTC+8 time zone.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The page number.
        # 
        # Starting value: 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 30 to 100.
        # 
        # Default value: 30.
        self.page_size = page_size
        # The region ID of the lightweight database instance.
        # You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to get the latest list of supported Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range to query.
        # 
        # The time is in UTC and must be formatted as `yyyy-MM-ddTHH:mm:ssZ` as specified by the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard.
        # 
        # > The console displays this time in the UTC+8 time zone.
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
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

